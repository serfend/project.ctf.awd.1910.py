import paramiko
import config
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
    bckPath=[]
    def configStart():
        return ssh.ServerConfig(
            ssh.sshConfig(
                config.sshConfig['hostname'],
                config.sshConfig['port'],
                config.sshConfig['username'],
                config.sshConfig['password'],
                config.sshConfig['pfile']
            ),
            ssh.DbConfig(
                config.dbConfig['dbName'],
                config.dbConfig['username'],
                config.dbConfig['password']
                ),
            config.localBkPath,
            config.webrootPath)
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
        return f'{{self.webRoot}}/{childPath}'
    def getBckName(self):
        return 'bck.tar'
    def upload(self,filepath,serverpath):
        lf=self.getLocalPath(filepath)
        wf=self.getWebPath(serverpath)
        print(f'upload file:{wf}->{lf}')
        self.sftp.put(self.getLocalPath(filepath),self.getWebPath(serverpath))
    def download(self,serverpath,filepath):
        lf=self.getLocalPath(filepath)
        wf=self.getWebPath(serverpath)
        print(f'download file:{wf}->{lf}')
        self.sftp.get(wf,lf)
    def backupserver(self):
        cur_time=time.strftime("%Y%m%d_%H%M%S", time.localtime())
        cur_path=f'bck_{cur_time}.bck'
        print(f'backup file start:{cur_path}')
        self.execCmd(f'tar cvzf {self.webRoot}/{self.getBckName()} {self.webRoot}')
        self.download(f'{self.webRoot}/{self.getBckName()}',cur_path)
        self.bckPath.append(cur_path)
        self.execCmd(f'rm -rf {self.webRoot}/{self.getBckName()}')
    def reDeploy(self,index=-1):
        if index==-1:
            index=len(self.bckPath)-1
        cur_path=self.bckPath[index]
        self.execCmd(f'rm -rf {self.webRoot}*')
        self.upload(cur_path,f'{self.webRoot}/{self.getBckName()}')
        self.execCmd('tar zxvf {self.webRoot}/{self.getBckName()} {self.webRoot}') 
        self.execCmd('rm -rf {self.webRoot}/{self.getBckName()}')
    def __del__(self):
        self.disconnect()
    def __init__(self,serverConfig):
        self.root=os.getcwd()
        self.webRoot=config.webrootPath
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
    


