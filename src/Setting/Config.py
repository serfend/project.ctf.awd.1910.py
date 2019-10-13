#use utf-8
import hashlib
import base64
import time
import json
import os
import sys
class Config:
    __defaultSettingPath='setting/default.json'
    
    def __init__(self,settingPath=''):
        self.load(settingPath)
        pass
    def load(self,settingPath=''):
        
        if settingPath!='':
            self.settingPath=settingPath
        if self.settingPath=='':
            raise Exception("setting path is null")
        path=f'{sys.path[0]}/{self.settingPath}'
        print(f'Config.loadSetting:{path}')
        file=open(path,'r',encoding='utf-8')
        content=file.read()
        self.obj=json.loads(content)
        file.close()
    def __getitem__(self,index):
        return self.obj
    def __setitem__(self,index,v):
        self.obj=v