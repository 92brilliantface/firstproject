import re

ip1 = '192.168.0.114'
ip2 = '192.168.112.'

webs = ['http://www.test.com', 
        'https://www.test1.com', 
        'http://www.test.com', 
        'ftp://www.test.com', 
        'http:://www.test.com',
       'htp://www.test.com',
       'http://www.google.com', 
       'https://www.homepage.com']

ip_correct = re.compile(r'\d+.\d+.\d+.\d+')
print ip_correct.search(ip1).group()
