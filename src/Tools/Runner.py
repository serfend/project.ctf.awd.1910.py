import threading
'''
创建一个执行器
args:
    callback:当function调用完成后返回，并传回self'
returns:

'''
class Runner(threading.Thread):
    def __init__(self,function,args,callback,constantRun=False):
        super(Runner,self).__init__()
        self.args=args
        self.callback=callback
        if self.callback==None:self.callback=lambda r:False
        self.function=function
        self.constantRun=constantRun
    def runWithArg0(self):
        self.function()
    def runWithArg1(self):
        self.function(self.args[0])
    def runWithArg2(self):
        self.function(self.args[0],self.args[1])
    def runWithArg3(self):
        self.function(self.args[0],self.args[1],self.args[2])
    def runWithArg4(self):
        self.function(self.args[0],self.args[1],self.args[2],self.args[3])
    def runWithArg5(self):
        self.function(self.args[0],self.args[1],self.args[2],self.args[3],self.args[4])
    #wo hao han pi a
    def run(self):
        self.arg_len=len(self.args)
        haveArgs=self.arg_len>0
        self.useFunc=[self.runWithArg0,self.runWithArg1,self.runWithArg2,self.runWithArg3,self.runWithArg4,self.runWithArg5]
        if self.arg_len>len(self.useFunc):
            raise Exception('咱不支持')
        self.nf=self.useFunc[self.arg_len]
        while True:
            self.Result=self.nf()
            if not self.callback(self):
                if not self.constantRun:
                    return self.Result