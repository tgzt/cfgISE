# Add NAD
import requests
import json
#
usr = "ers"
pwd = "ersM0"
ise = "ise.secure-x.local"
headers = {"accept" : "application/vnd.com.cisco.ise.networkdevice.1.0+xml" ,
	}

payload = { }
	
	
url= "https://%s:9060/ers/config/networkdevice" % ise

r = requests.post(url,payload=payload,verify=False,auth=(usr,pwd),headers=headers)
#
print "CODE:",r.status_code
print "HEADERS:",r.headers
print "CONTENT:",r.content
print r.content.result.json()
