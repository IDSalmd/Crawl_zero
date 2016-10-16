import demo

url = 'http://www.zhihu.com'
#print  demo.download('https://www.baidu.com',{},None,3)
print demo.get_robots(url).read()
