#! /usr/bin/env python2.7
# get Endpoint Groups
#
usr = "admin"
pwd = "Ci5coAdmin"
ise = "ise.secure-x.local"

url= "https://%s:%s@ise-secure-x.local:9060/ers/config.endpoint" % (usr,pwd,ise)

r = requests.get(url,auth=(usr,pwd))
#
print r.status_code
print r.headers
print r.content