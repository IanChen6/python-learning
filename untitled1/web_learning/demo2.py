import urllib.request

response = urllib.request.urlopen('http://www.jobbole.com/',timeout=10)
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader("server"))
print(response.read())
