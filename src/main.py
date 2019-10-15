
import Weapons
import Defends
import Tools
import Setting
import hashlib,random


def bckDoor(w):
    print(w.eachIp(w.trojTime))
    print(w.eachIpArgs(w.runCmd,'*.php'))
    print(w.eachIpArgs(w.runCmd,'ls -al'))
    print(w.eachIpArgs(w.runTeamCmd,'system(\'whoami\')'))
if __name__ == "__main__":
    print('script start')
    config=Setting.Config('default.json')[0]
    webtroj=Weapons.WebTroj(random.randint(1000,9999),config)
    
    ssh=Defends.SSH(Defends.SSH.configStart(config))
    while not ssh.connected:
        ssh.connect()
    
    cur_path=ssh.backupserver()
    ssh.extractBackup(cur_path)
    codeReview=Defends.CodeReview(config)
    codeReview.start()
    
    #ssh.deploy('bck_20191013_151029.bck')
    # ssh.reDeploy()
    #print(ssh.execCmd('cd /app;ls -al').getMsg())
    pass


