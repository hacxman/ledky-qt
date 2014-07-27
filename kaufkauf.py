import urllib2
import urllib
import re

# f = urllib2.urlopen("http://openean.kaufkauf.net/?ean = {} & cmd = query & queryid = [userid] 
def lookup(ean):
  c = ean.split(':')[1]
  f = urllib2.urlopen("http://openean.kaufkauf.net/index.php",
    urllib.urlencode({'ean': c, 'cmd': 'ean1', 'SID':''}))
  #return re.match('<a target="blank" href=".*amazon.de.*">$^(.*)$ *</a>', f.read()).groups()[0].strip()
  return re.search(r'<a href=\'.*amazon.de.* TARGET=\'_blank\'>(.*)</a>', f.read()).groups()[0].strip()

