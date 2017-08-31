# encoding=utf-8
import requests

url = "https://cool-cf19a.firebaseio.com/"

request1 = requests.delete(url + '/data1_string.json')
print request1.status_code, request1.content

request2 = requests.delete(url + '/data2_utf_chinese.json')
print request2.status_code, request2.content
