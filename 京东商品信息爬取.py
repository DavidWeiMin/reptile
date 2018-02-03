# 利用requests.get()获取网页文本的通用代码框架
####################################################################################
import requests
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[:1000]
    except:
        return '产生异常'

if __name__ == '__main__':
    url = 'https://item.jd.com/5706773.html'
    print(getHTMLText(url))