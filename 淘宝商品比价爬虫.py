import requests
import re
# 爬虫之前查看robots协议
def getHTMLTEXT(url): # 根据网址获取页面源代码文本
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def parsePage(infoList, html):
    try:
        plt = re.findall(r'"view_price":"[\d.]*"',html) # 通过正则表达式匹配得到价格信息
        tlt = re.findall(r'"raw_title":".*?"',html) # 通过正则表达式匹配得到商品名信息
        for i in range(len(plt)): # 拼接信息
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            infoList.append([price,title]) 
    except:
        return ''

def printGoodsList(infoList): # 设置打印模板
    tplt = '{:4}\t{:8}\t{:16}' # 设置打印模板
    print(tplt.format('序号','价格','商品名称'))
    count = 0 # 序号
    for g in infoList:
        count = count + 1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods = '书包' # 搜索商品关键字
    depth = 2 # 搜索几页
    start_url = 'https://s.taobao.com/search?q=' + goods # 搜索结果的第一页网址
    infoList = [] # 初始商品信息
    for i in range(depth): # 循环翻页
        try:
            url = start_url + '&=' + str(44 * i) # 构造翻页后的网址
            html = getHTMLTEXT(url) # 获取网页源代码的文本
            parsePage(infoList,html) # 解析源代码文本，得到商品信息
        except:
            continue
    printGoodsList(infoList) # 打印商品信息
  
main()

