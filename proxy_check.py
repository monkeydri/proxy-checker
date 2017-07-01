import urllib2, socket, sys

socket.setdefaulttimeout(180)

# 0. Read the list of proxy provided as arguments
# remove the name of the script in the arguments array
sys.argv.pop(0)
proxyList = sys.argv

def is_bad_proxy(pip):
	try:
		proxy_handler = urllib2.ProxyHandler({'http': pip})
		opener = urllib2.build_opener(proxy_handler)
		opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		urllib2.install_opener(opener)
		req=urllib2.Request('http://www.google.com')  # change the url address here
		sock=urllib2.urlopen(req)
	except urllib2.HTTPError, e:
		print 'Error code: ', e.code
		return e.code
	except Exception, detail:
		print "ERROR:", detail
		return 1
		return 0

for item in proxyList:
	if is_bad_proxy(item):
		print "Bad Proxy", item
	else:
		print item, "is working"