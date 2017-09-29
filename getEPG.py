#! /usr/bin/env python2.7
# get Endpoint Groups
import requests
#
usr = "admin"
pwd = "Ci5coAdmin"
ise = "ise.secure-x.local"

url= "https://%s:9060/ers/config.endpoint" % ise

r = requests.get(url,verify=False,auth=(usr,pwd))
#
print "CODE:",r.status_code
print "HEADERS:",r.headers
print "CONTENT:",r.content
