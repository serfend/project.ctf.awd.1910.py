import requests
import random
import json
import threading
import time
class GiftResult:
    msg=''
    code=''
    codeDic={
        '424':True,
        '417':True
    }
    def __init__(self,dic):
        self.msg=dic['msg']
        self.code=dic['code']
    def valid(self):
        #print(f'{self.code} in {GiftResult.codeDic}-> {str(self.code) in GiftResult.codeDic}' )
        return not str(self.code) in GiftResult.codeDic
dicMap="abcdefghijklmnopqrstuvwxyz0123456789"
usedMap={}
lock=threading.Lock()
threadPool=[]
totalCount=0
thisRoundCount=100000
def generateKey():
    result=''
    for i in range(9):
        index=random.randrange(0,len(dicMap))
        result+=dicMap[index:index+1]
    return result
class Runner(threading.Thread):
    hdlCount=0
    def __init__(self,threadName):
        super(Runner,self).__init__(name = threadName)
    def run(self):
        global totalCount
        try:
            while True:
                code=generateKey()
                lock.acquire()
                totalCount=totalCount+1
                self.hdlCount+=1
                if usedMap.__contains__(code):
                    print(f'already contains{code}')
                    lock.release()
                    continue 
                lock.release()
                r=requests.get(f'http://statistics.pandadastudio.com/player/giftCode?uid=524926596&code={code}')
                j=json.loads(r.text)
                lock.acquire()
                usedMap[code]=GiftResult(j)
                if usedMap[code].valid(): 
                    print(f"success:{code}->{usedMap[code].msg}")
                else:
                    pass#print(f"fail:{code}:{j['code']}")
                
                lock.release()
                if totalCount>thisRoundCount:
                    break
        except :
            pass
if __name__ == "__main__":
    for i in range(80):
        threadPool.append(Runner(str(i)))
        threadPool[i].start()
    lastTimeHdlCount=[]
    for i in range(len(threadPool)+2):
        lastTimeHdlCount.append(0)
    while True:
        time.sleep(1)
        tmpResult=''
        
        for i in range(len(threadPool)):
            if not threadPool[i].isAlive():
                threadPool[i]=Runner(str(i))
                threadPool[i].start()
            tmpResult=f'{tmpResult} {threadPool[i].hdlCount-lastTimeHdlCount[i+1]}'
            lastTimeHdlCount[i+1]=threadPool[i].hdlCount
        # print(f'{totalCount} ： {totalCount-lastTimeHdlCount[0]} -> {tmpResult}')
        lastTimeHdlCount[0]=totalCount
    pass
