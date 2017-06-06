# For python 2
import urllib
dat = urllib.urlencode({'username':'Test','score':10,'guesses':10,'country':'India'}).encode()
response = urllib.urlopen('http://0.0.0.0:8080/update',data=dat)
print (response.read())
