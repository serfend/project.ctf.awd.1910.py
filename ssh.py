import paramiko
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
class ServerConfig:
    def __init__(self, dbConfig,webPath,localBkPath):
        pass
class SSHserver:
    def __init__(self,serverConfig):
        self.interval=60000
        #创建一个ssh的客户端，用来连接服务器
        self.ssh = paramiko.SSHClient()
        #创建一个ssh的白名单
        self.know_host = paramiko.AutoAddPolicy()
        #加载创建的白名单
        self.ssh.set_missing_host_key_policy(self.know_host)
        #连接服务器
        pkey=paramiko.RSAKey.from_private_key_file('kali')
        
        paramiko.util.log_to_file('paramiko.log')
        print('ssh ing')
        self.ssh.connect(
            hostname = "47.74.238.240",
            port = 2201,
            username = "ctf",
            pkey='a356229c3c7686abaa85e893d86f672'
        )
        print('ssh ing')
        #执行命令
        stdin,stdout,stderr = ssh.exec_command("ls")
        #stdin  标准格式的输入，是一个写权限的文件对象
        #stdout 标准格式的输出，是一个读权限的文件对象
        #stderr 标准格式的错误，是一个写权限的文件对象
        
        print(stdout.read().decode())
        
        pass
    def __del__(self):
        self.ssh.close()
        pass
    def start(self):
        pass
    


