import paramiko
import os
import time
import Tools
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
    def __init__(self,sshConfig, dbConfig,fileOperator):
        self.sshConfig=sshConfig
        self.dbConfig=dbConfig
        self.fileOperator=fileOperator
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
        configself=config['self']
        sshConfig=configself['sshConfig']
        dbConfig=configself['dbConfig']
        return ServerConfig(
            SSH_Config(
                sshConfig['hostname'],
                sshConfig['port'],
                sshConfig['username'],
                sshConfig['password'],
                sshConfig['pfile']
            ),
            DbConfig(
                dbConfig['dbName'],
                dbConfig['username'],
                dbConfig['password']
                ),
            Tools.FileOperator(config)
            )
    def connect(self):
        Tools.CC.i(f'sshing:{self.sshConfig.hostname}:{self.sshConfig.port}->{self.sshConfig.password}',1)
        try:
            self.transport = paramiko.Transport((self.sshConfig.hostname, int(self.sshConfig.port)))
            self.transport.connect(username=self.sshConfig.username, password=self.sshConfig.password)
            self.ssh = paramiko.SSHClient()
            self.ssh._transport = self.transport
            self.sftp = paramiko.SFTPClient.from_transport(self.transport)
            self.connected=True
        except Exception as e:
            if e=='Authentication failed.':
                self.connected=False
            else:
                Tools.CC.i(e,1)
        finally:
            return self.connected
    def disconnect(self):
        Tools.CC.i('ssh.disconnect()')
        self.connected=False
        try:
            self.transport.close()
        except Exception as e:
            pass
    def execCmd(self,cmd):
        cmd=cmd.replace(';', ';\n')
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        result= CmdResult(stdin,stdout,stderr)
        showstr='' if result.getResult()=='' else f'\n-->{result.getResult()}'
        Tools.CC.i(f"ssh.execCmd:{cmd} {showstr}")
        return result
 
    def getBckName(self):
        return 'bck.tar'
    def upload(self,filepath,serverpath):
        lf=self.fileOperator.getLocalPath(filepath)
        wf=self.fileOperator.getWebPath(serverpath)
        
        permissionPath=self.fileOperator.getPermissionWebPath(serverpath)
        Tools.CC.i(permissionPath)
        des=f'with permissionPath:{permissionPath}' if (permissionPath!='') else ''
        Tools.CC.i(f'ssh.uploadFile:{lf}->{wf} {des}')
        if permissionPath=='':
            self.sftp.put(self.fileOperator.getLocalPath(filepath),self.fileOperator.getWebPath(serverpath))
        else:
            self.sftp.put(self.fileOperator.getLocalPath(filepath),permissionPath)
            self.execCmd(f'mv {permissionPath} {wf}')
    def download(self,serverpath,filepath):
        lf=self.fileOperator.getLocalPath(filepath)
        wf=self.fileOperator.getWebPath(serverpath)
        Tools.CC.i(f'ssh.downloadFile:{wf}->{lf}')
        self.sftp.get(wf,lf)
    def appendBckFile(self):
        cur_time=Tools.CmdBuilder.StandardTime()
        cur_path=f'bck_{cur_time}.bck'
        self.bckPath.append(cur_path)
        return cur_path
    def redeploy(self):
        return self.deploy(self.bckPath[len(self.bckPath)-1])
    """
    将codereview文件夹打包到备份文件
    Returns:
        新的备份文件的路径
    """
    def packToBckFile(self):
        Tools.CC.i(f'{self.__class__.__name__}.packToBckFile')
        newBckFilename=self.appendBckFile()
        Tools.CmdExec().execCmd(f'tar czf  {self.localBkPath}/{newBckFilename} -C {self.localCodeReviewPath}/*')
    def backupserver(self):
        cur_path=self.appendBckFile()
        Tools.CC.i(f'ssh.backupFile:{cur_path}')
        self.execCmd(f'tar czf {self.fileOperator.webrootPath}/{self.getBckName()} {self.fileOperator.webrootPath}/*')  
        self.download(f'{self.getBckName()}',cur_path)
        self.execCmd(f'rm -rf {self.fileOperator.webrootPath}/{self.getBckName()}')
        return cur_path
    def extractBackup(self,cur_path):
        return self.fileOperator.extractBackup(cur_path)
    def deploy(self,bckPath,cleardir=False):
        Tools.CC.i(f'ssh.deploy:{bckPath}{" with clear previous path" if cleardir else ""}')
        if cleardir:
            self.execCmd(f'rm -rf {self.fileOperator.webrootPath}')
        self.upload(bckPath,f'{self.getBckName()}')
        self.execCmd(f'tar zxf {self.fileOperator.webrootPath}/{self.getBckName()} -C /') 
        self.execCmd(f'rm -rf {self.fileOperator.webrootPath}/{self.getBckName()}')
    def __del__(self):
        self.disconnect()
    def __init__(self,serverConfig):
        self.fileOperator=serverConfig.fileOperator
        self.connected=False
        self.serverConfig=serverConfig
        self.sshConfig=self.serverConfig.sshConfig
        self.dbConfig=self.serverConfig.dbConfig
        pass
    def start(self):
        pass
    


