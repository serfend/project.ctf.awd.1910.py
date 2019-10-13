import threading
class Runner(threading.Thread):
    def __init__(self,function,args=[],constantRun=False):
        super(Runner,self).__init__()
        self.function=function
        self.args=args
        self.constantRun=constantRun
    def run(self):
        haveArgs=len(self.args)>0
        while True:
            if haveArgs:
                self.Result=self.function(self.args)
            else:
                self.Result=self.function()

            if not self.constantRun:
                return