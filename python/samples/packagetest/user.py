from pkg import foo, bar
import urllib3

foo.func()
http = urllib3.PoolManager()
r = http.request('GET', 'http://google.com/robots.txt')
print(r.data)
bar.func()

