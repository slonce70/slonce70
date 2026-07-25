import json,time,urllib.error,urllib.request
TOK='eca379f9-c439-478b-8ff6-2b2fe6315205'
url=f'https://webhook.site/token/{TOK}/requests?sorting=newest'
for i in range(10):
    try:
        q=urllib.request.Request(url,headers={'Accept':'application/json','User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(q,timeout=20) as r:
            b=r.read().decode('utf-8','replace');print('REQUESTS',r.status,b[:50000]);break
    except Exception as e:
        print('ERR',repr(e));time.sleep(2)
