# 导入模块
import requests # 网络请求模块
import re # 提取数据
import time # time.sleep用于暂停

# 爬取数据要求
page = 2 # 爬取数据的总页码

for n in range(1,page):
    # 电影天堂网址
    a_url = 'http://www.dytt8.net/html/gndy/dyzz/list_23_%s.html' % str(n) # 观察页码网址规律，拼接出每页的网址
    html_1 = requests.get(a_url) # 访问网页，请求方法从网页开发者工具查看
    # 指定网页编码格式
    html_1.encoding = 'gb2312' # 网页编码方式用网页开发者工具从elments的head查看charset
    # print(html_1.status_code) # 等于200表示正常
    # print(html_1.text) # 查看网页源代码
    detail_list = re.findall('<a href="(.*?)" class="ulink',html_1.text) # 利用正则表达式在网页源代码中匹配需要进入的链接
    # print(detail_list)
    for m in detail_list:
        b_url = 'http://www.dytt8.net/' + m # 拼接形成点击进入之后的链接
        # print(b_url)
        html_2 = requests.get(b_url) # 访问网页，请求方法从网页开发者工具查看
        # 指定网页编码格式   
        html_2.encoding = 'gb2312'
        ftp = re.findall('<a href="(.*?)">.*?</a></td>',html_2.text) # 利用正则表达式在网页源代码中的链接
        # 将获取的下载链接写入文件
        with open('d:\\Documents\\GitHub\\reptile\\下载的资源.txt','a',encoding='utf-8') as f: 
            f.write(ftp[0] + '\n')
        time.sleep(2) # 暂停2秒以模拟人的访问速度（访问过快会被以为是机器）

