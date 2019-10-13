#执行代码审计
import os
class CodeReview:
    def __init__(self,config):
        self.root=os.getcwd()
        self.webRoot=config['webrootPath']
        self.localBkPath=self.serverConfig.localBkPath
    def reviewSingleFile(self,fpath):
        pass
    def review(self,path):
        pass