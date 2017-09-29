#! /usr/bin/env python2.7
# get Endpoint Groups

url= "https://%s:%s@ise-secure-x.local:9060/ers/config.endpoint"

r = requests.get(url,auth=(usr,pwd))
r.status_code