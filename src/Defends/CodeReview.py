#执行代码审计
import os
import json
import Setting
import re
import chardet
import Tools
class ReviewResult:
    def __init__(self, path, line,patch,payload,desc):
          self.path=path
          self.line=line
          self.patch=patch
          self.payload=payload
          self.desc=desc
          print (f"hole was found at {Tools.CC.WARNING}{path}:{line+1}{Tools.CC.ENDC} : {Tools.CC.HEADER}{desc}{Tools.CC.ENDC}")
class CodeReview:
    
    def __init__(self,config):
        self.localCodeReviewPath=config['self']['localCodeReviewPath']
        self.webrootPath=config['self']['webrootPath'] 
        self.review_checklist=config['self']['review_checklist']
        self.rules={}
        self.fileReviewCounter=0
        self.holes=[]
        with open(f'{Setting.Config.exepath}/{Setting.Config.defaultSettingPath}/{self.review_checklist}','r+') as f:
            tmp=json.load(f)[0]
            for items in tmp:
                tmpItem=[]
                for item in tmp[items]:
                    if item['enable']=='1':
                        tmpItem.append(item)
                self.rules[items]=tmpItem
    def start(self):
        reviewPath=f'{Setting.Config.root}/{self.localCodeReviewPath}'
        startTxt=Tools.CC.showHeader(f'{self.__class__.__name__}.start')
        print(f'{startTxt} at {reviewPath}')
        result= self.review(reviewPath)
        print(f'{startTxt} {reviewPath} completed with {self.fileReviewCounter} file{"s" if self.fileReviewCounter>1 else ""}')
        return result
    def reviewSingleFile(self,fpath):
        self.fileReviewCounter+=1
        extname=os.path.splitext(fpath)[1]
        if extname.replace('.', '') in self.rules:
            #print(f'{self.__class__.__name__}.reviewSingleFile:{fpath}')
            with open(fpath, 'rb') as f:
                cur_encoding = chardet.detect(f.read())['encoding']
            f=open(fpath,'r',encoding=cur_encoding)
            content=f.read()
            f.close()
            return self.reviewContent(extname,content,fpath)
    def reviewContent(self,ftype,content,path=''):
        ftype=ftype.replace('.', '')
        rule=self.rules[ftype]
        for r in rule:
            g=re.finditer(r['pattern'], content, re.MULTILINE|re.IGNORECASE)
        for matchNum, match in enumerate(g, start=1):
            self.holes.append(
                ReviewResult(path,content.count('\n',0,match.end()),r.get('patch'),r.get('payload'),r.get('desc'))
            )
            
    def review(self,path):
        for root,dirs,files in os.walk(path):
            for tfile in files:
                self.reviewSingleFile(f'{root}/{tfile}')