import os
import Tools.CmdBuilder
class CmdExec:
    def execCmd(self,cmd):
        print(f'os.system:{cmd}')
        return (os.system(cmd))
class CC:
    DisplayRank=0
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    @staticmethod
    def r(info,title='\033[95m'):
        return f'{title}{info}\'\033[0m\''
    """
    控制台输出
    """
    @staticmethod
    def i(info,rank=0):
        if rank>=CC.DisplayRank:print(f'{Tools.CmdBuilder.StandardTime()} {info}')