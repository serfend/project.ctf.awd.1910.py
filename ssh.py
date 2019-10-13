import paramiko
import config
import os
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
class sshConfig:
    def __init__(self,hostname,port,username,password,pfile):
        self.hostname=hostname
        self.port=port
        self.username=username
        self.password=password
        self.pfile=pfile
class ServerConfig:
    def __init__(self,sshConfig, dbConfig,webPath,localBkPath=''):
        self.sshConfig=sshConfig
        self.dbConfig=dbConfig
        self.webPath=webPath
        self.localBkPath=localBkPath

class SSHserver:
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
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        return stdin,stdout,stderr
    def getLocalPath(self,childPath):
        return f'{self.root}/{config.localBkPath}/{childPath}'
    def getWebPath(self,childPath):
        return f'{config.webrootPath}/{childPath}'
    def upload(self,filepath,serverpath):
        self.sftp.put(self.getLocalPath(filepath),self.getWebPath(serverpath))
    def download(self,serverpath,filepath):
        self.sftp.get(self.getWebPath(serverpath),self.getLocalPath(filepath))
    def __del__(self):
        self.disconnect()
    def __init__(self,serverConfig):
        self.root=os.getcwd()
        self.serverConfig=serverConfig
        self.sshConfig=self.serverConfig.sshConfig
        self.dbConfig=self.serverConfig.dbConfig
        self.webPath=self.serverConfig.webPath
        self.localBkPath=self.serverConfig.localBkPath
        paramiko.util.log_to_file('paramiko.log')
        pass
    def __del__(self):
        self.ssh.close()
        pass
    def start(self):
        pass
    


