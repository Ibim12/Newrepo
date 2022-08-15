import smtplib
import urllib.request
import urllib2

proxy_support = urllib2.ProxyHandler({"http":"http://61.233.25.166:80"})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)

html = urllib2.urlopen("http://www.yahoo.co.uk").read()
print (html)

server=smtplib.SMTP_SSL("smtp.yahoo.co.uk",465)
server.login("ibim.obomanu@yahoo.co.uk", "29036Bdany")
server.sendmail("ibim.obomanu@yahoo.co.uk","ibim.obomanu@gmail.com","Hello, this is your first python pprogramming message")


server.quit()