#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: 02_grequests_test.py
@time: 2023/6/9  16:10
# @describe: GRequests
    允许您将 Requests 与 Gevent 一起使用，以轻松发出异步 HTTP 请求。
"""
import grequests


urls = [
    'https://www.baidu.com/',
    'https://fanyi.baidu.com/translate',
    'https://note.youdao.com/web',
    'https://www.yuque.com/',
    'https://www.cnblogs.com/aggsite/allsitecategories',

]

# 创建一组未发送的请求
res = (grequests.get(u) for u in urls)
# 同时发送它们
response = grequests.map(res)
print(response)


# 2. 使用回调函数
def print_response(response, *args, **kwargs):
    # print(response.content)
    print(response.url)
    print(response.text)


urls = ['http://httpbin.org/delay/1']*3
requests = [grequests.get(url, callback=print_response) for url in urls]
responses = grequests.map(requests)


# 3.使用会话-会话可以在多个请求之间共享状态，例如cookie或身份验证信息
session = grequests.Session()
urls = ['http://httpbin.org/get', 'http://httpbin.org/post']
requests = [grequests.get(url, session=session) for url in urls]
responses = grequests.map(requests)


# 4. 使用 自定义请求的URL、请求头和请求参数
urls = ['https://www.cnblogs.com/aggsite/allsitecategories', 'https://www.cnblogs.com/hejiale010426/ajax/blogStats']
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
# params = {'usernme': 'xx', 'password': ''}

session = grequests.Session()
# 创建请求列表
requests = (grequests.get(u, headers=headers, params='') for u in urls)

# 发送请求并获取响应
responses = grequests.map(requests)

# 处理响应
for response in responses:
    if response is not None:
        # print(response.url)
        # print(response.text)
        print(response)
    else:
        print('Request failed')

