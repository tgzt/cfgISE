#! /usr/bin/env python2.7
# get Endpoint Groups
import requests
#
usr = "ers"
pwd = "ersM0"
ise = "ise.secure-x.local"
headers = {"Accept" : "application/vnd.com.cisco.ise.identity.internaluser.1.0+xml"}

url= "https://%s:9060/ers/config/internaluser/versioninfo" % ise

r = requests.get(url,verify=False,auth=(usr,pwd),headers=headers)
#
print "CODE:",r.status_code
print "HEADERS:",r.headers
print "CONTENT:",r.content
