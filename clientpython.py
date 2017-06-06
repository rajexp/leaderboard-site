# For python 2
import urllib
dat = urllib.urlencode({'username':'Test','score':10,'guesses':10,'country':'India'}).encode()
#req =  request.Request('http://leaderboard-flask-rajexp.c9users.io:8080/update',data=dat) # this will make the method "POST"
response = urllib.urlopen('http://0.0.0.0:8080/update',data=dat)
print (response.read())