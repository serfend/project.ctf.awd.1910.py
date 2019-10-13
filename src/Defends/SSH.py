import paramiko
import os
import time
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
    def __init__(self,sshConfig, dbConfig,webrootPath,localBkPath=''):
        self.sshConfig=sshConfig
        self.dbConfig=dbConfig
        self.webrootPath=webrootPath
        self.localBkPath=localBkPath
class CmdResult:
    def getResult(self):
        return self.msg.decode()
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
        self.errinfo=self.stderr.read()
        if len(self.errinfo)>0:
            self.msg=self.errinfo
            return
        self.msg=self.stdout.read()
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
            config['self']['localBkPath'])
    def connect(self):
        print(f'sshing:{self.sshConfig.hostname}:{self.sshConfig.port}')
        self.transport = paramiko.Transport((self.sshConfig.hostname, int(self.sshConfig.port)))
        self.transport.connect(username=self.sshConfig.username, password=self.sshConfig.password)
        self.ssh = paramiko.SSHClient()
        self.ssh._transport = self.transport
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)
    def disconnect(self):
        self.transport.close()
    def execCmd(self,cmd):
        print(f"ssh.execCmd:{cmd}")
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        return CmdResult(stdin,stdout,stderr)
    def getLocalPath(self,childPath):
        return f'{self.root}/{self.localBkPath}/{childPath}'
    def getWebPath(self,childPath):
        return f'{self.webrootPath}/{childPath}'
    def getBckName(self):
        return 'bck.tar'
    def upload(self,filepath,serverpath):
        lf=self.getLocalPath(filepath)
        wf=self.getWebPath(serverpath)
        print(f'ssh.uploadFile:{wf}->{lf}')
        self.sftp.put(self.getLocalPath(filepath),self.getWebPath(serverpath))
    def download(self,serverpath,filepath):
        lf=self.getLocalPath(filepath)
        wf=self.getWebPath(serverpath)
        print(f'ssh.downloadFile:{wf}->{lf}')
        self.sftp.get(wf,lf)
    def backupserver(self):
        cur_time=time.strftime("%Y%m%d_%H%M%S", time.localtime())
        cur_path=f'bck_{cur_time}.bck'
        print(f'ssh.backupFile:{cur_path}')
        self.execCmd(f'tar cvzf {self.webRoot}/{self.getBckName()} {self.webRoot}/*')
        self.download(f'{self.getBckName()}',cur_path)
        self.bckPath.append(cur_path)
        self.execCmd(f'rm -rf {self.webRoot}/{self.getBckName()}')
    def deploy(self,bckPath):
        print(f'ssh.deploy:{bckPath}')
        self.execCmd(f'rm -rf {self.webRoot}')
        self.upload(bckPath,f'{self.getBckName()}')
        self.execCmd(f'tar zxvf {self.webRoot}/{self.getBckName()}') 
        self.execCmd(f'rm -rf {self.webRoot}/{self.getBckName()}')
    def reDeploy(self,index=-1):
        if index==-1:
            index=len(self.bckPath)-1
        cur_path=self.bckPath[index]
        return self.deploy(cur_path)
    def __del__(self):
        self.disconnect()
    def __init__(self,serverConfig):
        self.root=os.getcwd()
        self.serverConfig=serverConfig
        self.webRoot=self.serverConfig.webrootPath
        self.localBkPath=self.serverConfig.localBkPath
        self.serverConfig=serverConfig
        self.sshConfig=self.serverConfig.sshConfig
        self.dbConfig=self.serverConfig.dbConfig
        self.webrootPath=self.serverConfig.webrootPath
        
        paramiko.util.log_to_file('paramiko.log')
        pass
    def __del__(self):
        self.ssh.close()
        pass
    def start(self):
        pass
    


