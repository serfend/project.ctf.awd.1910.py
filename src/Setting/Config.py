#use utf-8
import hashlib
import base64
import time
import json
import os
import sys
# import Celery

class Config:
    defaultSettingPath='setting'
    root=os.getcwd()
    exepath=sys.path[0]
    def __init__(self,settingPath=''):
        self.load(settingPath)
    def load(self,settingPath=''):
        if settingPath!='':
            self.settingPath=settingPath
        if self.settingPath=='':
            raise Exception("setting path is null")
        path=f'{sys.path[0]}/{Config.defaultSettingPath}/{self.settingPath}'
        print(f'Config.loadSetting:{path}')
        with open(path,'r',encoding='utf-8') as file:
            self.obj=json.load(file)
        self.autoReload()
    def autoReload(self):
        self.interval=self.obj['system']['reloadSettingInterval']
    def __getitem__(self,index):
        return self.obj
    def __setitem__(self,index,v):
        self.obj=v