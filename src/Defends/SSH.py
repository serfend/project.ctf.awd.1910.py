import paramiko
import os
import time
import Tools.CmdExec
import Setting
class DbConfig:
    sqlConnectCmd={
        'mysql':'mysql '
    }
    def __init__(self, dbName,username,password,sqlType='mysql'):
        self.dbName=dbName
        self.username=username
        self.password=password
        self.sqlType=sqlType
        pass
    @property
    def connectCmd():
        return f'1'
class SSH_Config:
    def __init__(self,hostname,port,username,password,pfile):
        self.hostname=hostname
        self.port=port
        self.username=username
        self.password=password
        self.pfile=pfile
class ServerConfig:
    def __init__(self,sshConfig, dbConfig,webrootPath,localBkPath='',localCodeReviewPath='',permissionWebPath=''):
        self.sshConfig=sshConfig
        self.dbConfig=dbConfig
        self.webrootPath=webrootPath
        self.localBkPath=localBkPath
        self.permissionWebPath=permissionWebPath
        self.localCodeReviewPath=localCodeReviewPath
class CmdResult:
    def getResult(self):
        return self.result
    def getMsg(self):
        return self.msg
    def execCmd(self,cmd):
        self.stdin.write(cmd)
        self.stdin.flush()
        self.hdlStream()
    def __init__(self,stdin,stdout,stderr):
        self.stdin=stdin
        self.stdout=stdout
        self.stderr=stderr
        self.hdlStream()
    def hdlStream(self):
        self.result=self.stderr.read().decode()
        self.msg=self.stdout.read().decode()
class SSH:
    bckPath=[]
    @staticmethod
    def configStart(config):
        return ServerConfig(
            SSH_Config(
                config['self']['sshConfig']['hostname'],
                config['self']['sshConfig']['port'],
                config['self']['sshConfig']['username'],
                config['self']['sshConfig']['password'],
                config['self']['sshConfig']['pfile']
            ),
            DbConfig(
                config['self']['dbConfig']['dbName'],
                config['self']['dbConfig']['username'],
                config['self']['dbConfig']['password']
                ),
            config['self']['webrootPath'],
            config['self']['localBkPath'],
            config['self']['localCodeReviewPath'],
            config['self']['permissionWebPath'])
    def connect(self):
        print(f'sshing:{self.sshConfig.hostname}:{self.sshConfig.port}')
        try:
            self.transport = paramiko.Transport((self.sshConfig.hostname, int(self.sshConfig.port)))
            self.transport.connect(username=self.sshConfig.username, password=self.sshConfig.password)
            self.ssh = paramiko.SSHClient()
            self.ssh._transport = self.transport
            self.sftp = paramiko.SFTPClient.from_transport(self.transport)
            self.connected=True
        except Exception as e:
            print(e)
    def disconnect(self):
        print('ssh.disconnect()')
        self.connected=False
        try:
            self.transport.close()
        except Exception as e:
            print(e)
    def execCmd(self,cmd):
        cmd=cmd.replace(';', ';\n')
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        result= CmdResult(stdin,stdout,stderr)
        showstr='' if result.getResult()=='' else f'\n-->{result.getResult()}'
        print(f"ssh.execCmd:{cmd} {showstr}")
        return result
    def getLocalPath(self,childPath):
        return f'{Setting.Config.root}/{self.localBkPath}/{childPath}'
    def getPermissionWebPath(self,childPath):
        if self.permissionWebPath=='':
            return ''
        return f'{self.permissionWebPath}/{childPath}'
    def getWebPath(self,childPath):
        return f'{self.webrootPath}/{childPath}'
    def getBckName(self):
        return 'bck.tar'
    def upload(self,filepath,serverpath):
        lf=self.getLocalPath(filepath)
        wf=self.getWebPath(serverpath)
        
        permissionPath=self.getPermissionWebPath(serverpath)
        print(permissionPath)
        des=f'with permissionPath:{permissionPath}' if (permissionPath!='') else ''
        print(f'ssh.uploadFile:{lf}->{wf} {des}')
        if permissionPath=='':
            self.sftp.put(self.getLocalPath(filepath),self.getWebPath(serverpath))
        else:
            self.sftp.put(self.getLocalPath(filepath),permissionPath)
            self.execCmd(f'mv {permissionPath} {wf}')
    def download(self,serverpath,filepath):
        lf=self.getLocalPath(filepath)
        wf=self.getWebPath(serverpath)
        print(f'ssh.downloadFile:{wf}->{lf}')
        self.sftp.get(wf,lf)
    def appendBckFile(self):
        cur_time=time.strftime("%Y%m%d_%H%M%S", time.localtime())
        cur_path=f'bck_{cur_time}.bck'
        self.bckPath.append(cur_path)
        return cur_path
    def backupserver(self):
        cur_path=self.appendBckFile()
        print(f'ssh.backupFile:{cur_path}')
        self.execCmd(f'tar czf {self.webrootPath}/{self.getBckName()} {self.webrootPath}/*')  
        self.download(f'{self.getBckName()}',cur_path)
        self.execCmd(f'rm -rf {self.webrootPath}/{self.getBckName()}')
        return cur_path
    def extractBackup(self,bck_path):
        bckpath=self.getLocalPath(bck_path)
        zxvfPath=f'{Setting.Config.root}/{self.localCodeReviewPath}'
        anyError=Tools.CmdExec().execCmd(f'tar zxf  {bckpath} -C {zxvfPath}')
    def deploy(self,bckPath,cleardir=False):
        print(f'ssh.deploy:{bckPath}{" with clear previous path" if cleardir else ""}')
        if cleardir:
            self.execCmd(f'rm -rf {self.webrootPath}')
        self.upload(bckPath,f'{self.getBckName()}')
        self.execCmd(f'tar zxf {self.webrootPath}/{self.getBckName()} -C /') 
        self.execCmd(f'rm -rf {self.webrootPath}/{self.getBckName()}')
    def __del__(self):
        self.disconnect()
    def __init__(self,serverConfig):
        self.connected=False
        self.serverConfig=serverConfig
        self.webrootPath=self.serverConfig.webrootPath
        self.localBkPath=self.serverConfig.localBkPath
        self.localCodeReviewPath=self.serverConfig.localCodeReviewPath
        self.permissionWebPath=self.serverConfig.permissionWebPath
        self.serverConfig=serverConfig
        self.sshConfig=self.serverConfig.sshConfig
        self.dbConfig=self.serverConfig.dbConfig
        paramiko.util.log_to_file('paramiko.log')
        pass
    def __del__(self):
        self.ssh.close()
        pass
    def start(self):
        pass
    


