import requests
import xml.etree.ElementTree as ET
import json

usr = "ers"
pwd = "ersM0"
ise = "ise.secure-x.local"

#Import XML file for NADs and make it useable
xml = open('nad.xml', 'r')
xml2 = xml.read()
xml3 = ET.fromstring(xml2)
payload =  ET.tostring(xml3, encoding='utf-8', method='xml')

#Start Bulk Push Creation
url = "https://%s:9060/ers/config/networkdevice/bulk/submit"  % ise

headers = {
    'content-type': "application/vnd.com.cisco.ise.network.networkdevicebulkrequest.1.1+xml",
    'cache-control': "no-cache"
}
response = requests.request("PUT", url, data=payload, headers=headers, auth=(usr,pwd), verify=False)
print response
print response.json()
#Response manipulation
responselocation = response.headers['location']
bulkstatusid = responselocation.split("submit/",1)[1]

#Print BulkID
print ("Bulk ID:" + str(bulkstatusid))

#Start Bulk Status GET
url = "https://%s:9060/ers/config/networkdevice/bulk/submit"  % ise  + str(bulkstatusid)

headers = {
    'content-type': "application/vnd.com.cisco.ise.network.networkdevicebulkstatus.1.1+xml",
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, auth=(usr,pwd), verify=False)

#Show ugly XML reponse for status
print(response.text)
