import requests
Keyword = 'python'
try:
    kv = {'wd':Keyword}
    r = requests.get('https://www.baidu.com/s',params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print('爬取失败')