#! /usr/bin/env python2.7
# get Endpoint Groups
import requests
#
usr = "ers"
pwd = "ersM0"
ise = "ise.secure-x.local"

url= "https://%s:9060/ers/config/internaluser/versioninfo" % ise

r = requests.get(url,verify=False,auth=(usr,pwd))
#
print "CODE:",r.status_code
print "HEADERS:",r.headers
print "CONTENT:",r.content
