import os
class CmdExec:
    def execCmd(self,cmd):
        print(f'os.system:{cmd}')
        return (os.system(cmd))
class CC:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    @staticmethod
    def r(info,title=CC.HEADER):
        return f'{title}{info}{CC.ENDC}'