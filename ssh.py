import paramiko
 
#创建一个ssh的客户端，用来连接服务器
ssh = paramiko.SSHClient()
#创建一个ssh的白名单
know_host = paramiko.AutoAddPolicy()
#加载创建的白名单
ssh.set_missing_host_key_policy(know_host)
 
#连接服务器
ssh.connect(
    hostname = "10.10.21.177",
    port = 22,
    username = "root",
    password = "123"
)
 
#执行命令
stdin,stdout,stderr = ssh.exec_command("rm -rf /root/Desktop/mv")
#stdin  标准格式的输入，是一个写权限的文件对象
#stdout 标准格式的输出，是一个读权限的文件对象
#stderr 标准格式的错误，是一个写权限的文件对象
 
print(stdout.read().decode())
ssh.close()