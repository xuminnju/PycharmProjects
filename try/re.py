import requests

# get
r = requests.get('https://www.python.org')
print(r.status_code)
print(b'Python is a programming language' in r.content)

print("--------------get args-------------")
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)

print("-------------post------------")
payload = dict(key1='value1', key2='value2')
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)