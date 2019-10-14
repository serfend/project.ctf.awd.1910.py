import random
import requests
def upload(self,rawFile):
        url=f'http://47.74.224.5:37002/ws_utc/resources/setting/keystore?timestamp={int(time.time()*1000)}'
        
        file = {'id': (None, 'WU_FILE_0'), 
            'name':  (None, f'{random.randint(1000,9999)}sf.MP4'), 
            'type': (None, 'plan/text'),
            'lastModifiedDate': (None, 'Sat Oct 21 2019 13:20:12 GMT+0800 (中国标准时间)'),
            'size': (None,'1555'), 
            'file': (f'{random.randint(1000,9999)}sf.MP4', rawFile, 'plan/text')} # 
        headers={'Cookies':'wordpress_test_cookie=WP+Cookie+check; JSESSIONID=Mcq-T51fXGCkf7_F-mAFL-5kExiIVxL4PoLR53sXTpDjn-8xoErF!779300569'}
        r=requests.post(url=url,files=file,headers=headers)
        print(r.text)