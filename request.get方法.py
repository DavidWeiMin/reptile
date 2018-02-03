# # 利用requests.get()获取网页文本的通用代码框架
# ####################################################################################
# import requests
# def getHTMLText(url):
#     try:
#         r = requests.get(url,timeout=30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         return '产生异常'

# if __name__ == '__main__':
#     url = 'https://www.baidu.com/'
#     print(getHTMLText(url))


# requests.get()详解
####################################################################################
r = requests.get('https://www.baidu.com/') # r = requests.get(url,params = None,**kwargs)，得到Response对象
# 检测网络请求的状态码，200表示正常，404表示网络出错
print(r.status_code)
# 返回网络页面源代码的字符串形式
print(r.text)
# 返回从网页源代码header中的charset得到的网络编码格式，没有charset字段时返回'ISO-8859-1'
print(r.encoding)
# 返回从网页相应内容推测的网页实际编码
print(r.apparent_encoding)
# 实际编码替换猜测编码
r.encoding = r.apparent_encoding
print(r.text)


# 网络出错异常处理（六种常用异常）
####################################################################################
print(requests.ConnectionError) # 网络连接错误
print(requests.HTTPError) # HTTP错误异常
print(requests.URLRequired) # URL缺失异常
print(requests.TooManyRedirects) # 超过最大重定向次数
print(requests.ConnectTimeout) # 连接远程服务器超时异常
print(requests.Timeout) # 请求URL超时

