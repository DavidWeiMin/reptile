import re
# re库的函数式用法
print('-'*20 + '\t\t\tre库的函数式用法\t\t\t' + '-'*20)
match = re.search(r'[1-9]\d{5}','HNU 410082') # 从HNU 410082匹配邮政编码，返回match对象
if match:
    print(match.group(0))
match = re.match(r'[1-9]\d{5}','410082 HNU') # 从410082 HNU开头开始匹配，返回match对象
if match:
    print(match.group(0))
ls = re.findall(r'[1-9]\d{5}','HNU 410082 CSU 410000') # 返回匹配到的对象列表
print(ls)
split = re.split(r'[1-9]\d{5}','HNU410082CSU410000THU100000') # 按正则表达式分割
print(split)
split = re.split(r'[1-9]\d{5}','HNU410082CSU410000THU100000',maxsplit=2)
print(split)
for m in re.finditer(r'[1-9]\d{5}','HNU410082CSU410000THU100000'):
    if m:
        print(m.group(0))
print(re.sub(r'[1-9]\d{5}',' ZIPCODE ','HNU410082CSU410000THU100000'))
# re库的面向对象用法
print('-'*20 + '\t\t\tre库的面向对象用法\t\t\t' + '-'*20)
regex = re.compile(r'[1-9]\d{5}')
match = regex.search('HNU 410082')
if match:
    print(match.group(0))
match = regex.match('410082 HNU') # 
if match:
    print(match.group(0))
ls = regex.findall('HNU 410082 CSU 410000')
print(ls)
split = regex.split('HNU410082CSU410000THU100000')
print(split)
split = regex.split('HNU410082CSU410000THU100000',maxsplit=2)
print(split)
for m in regex.finditer('HNU410082CSU410000THU100000'):
    if m:
        print(m.group(0))
print(regex.sub(' ZIPCODE ','HNU410082CSU410000THU100000'))
# match对象的属性和方法
print('-'*20 + '\t\t\tmatch对象的属性和方法\t\t\t' + '-'*20)
print(match.string) # 返回原字符串
print(match.re) # 返回待匹配的正则表达式
print(match.pos) # 返回原字符串的开始位置
print(match.endpos) # 返回原字符串的结束位置
print(match.group(0)) # 返回匹配到的字符串
print(match.start()) # 返回匹配到的字符串的开始位置
print(match.end()) # 返回匹配到的字符串的结束位置
print(match.span()) # 返回（start，end）