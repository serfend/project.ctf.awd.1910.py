
#通过ssh运维实现主动防御
#通防 文件监控 
class Defender:
    def __init__(self,ssh,config):
        self.ssh=ssh
        self.killer=config["env"]["troj"]["killer"]
        
        pass
    def killTroj(self):
        #使用ssh创建临时马，killall -uwww-data，ssh.deploy(#rawBck#)，删除临时马
        
        self.ssh.execCmd(self.killer)
        ssh.deploy(ssh.rawBck)
    def deployDefender(self):
        pass