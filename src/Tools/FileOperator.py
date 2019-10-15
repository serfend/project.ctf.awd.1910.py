import Tools
import Setting
import os
import shutil
class FileOperator:
    def __init__(self,config):
        self.localCodeReviewPath=config['self']['localCodeReviewPath']
        self.localBkPath=config['self']['localBkPath']
        self.webrootPath=config['self']['webrootPath']
        self.permissionWebPath= config['self']['permissionWebPath']
        self.packagePath=f'{self.localCodeReviewPath}/package'
    def extractBackup(self,bck_path):
        bckpath=self.getLocalPath(bck_path)
        zxvfPath=f'{Setting.Config.root}/{self.localCodeReviewPath}'
        anyError=Tools.CmdExec().execCmd(f'tar zxf  {bckpath} -C {zxvfPath}')
    """
    添加本地包(压缩文件)到codereview文件夹，方便后续打包到服务器
    """
    def addSelfPackage(self,packagePath):
        print(f'{self.__class__.__name__}.addSelfPackage:{packagePath}')
        if not os.path.exists(self.packagePath):
            os.makedirs(self.packagePath)
        shutil.copy(packagePath,self.packagePath)



    def getLocalPath(self,childPath):
        return f'{Setting.Config.root}/{self.localBkPath}/{childPath}'
    def getPermissionWebPath(self,childPath):
        if self.permissionWebPath=='':
            return ''
        return f'{self.permissionWebPath}/{childPath}'
    def getWebPath(self,childPath):
        return f'{self.webrootPath}/{childPath}'