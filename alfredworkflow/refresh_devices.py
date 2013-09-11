import json
import urllib2
import string
from settings import PROTOCOL, HOSTNAME
from http_server import stop


def refresh_devices():
    stop()

    tokenFile = open("token.txt")
    token = tokenFile.read()
    tokenFile.close()
    
    devicesFile = open("devices.txt", "w")

    with open("endpoints.txt", 'r') as fh:
        for endpoint in fh.readlines():
            if endpoint.__len__() > 1:
                ### collect devices for each endpoint
                
                for deviceType in ("switches", "locks"):
                    endpoint = endpoint.strip()
                    url = "{protocol}://{hostname}{endpoint}/{deviceType}".format(protocol=PROTOCOL, hostname=HOSTNAME, endpoint=endpoint, deviceType=deviceType)

                    req = urllib2.Request(url)
                    req.add_header('Authorization', "Bearer %s" % token)
                    response = urllib2.urlopen(req)
                    the_page = response.read()
                    jsonData = json.loads(the_page)
                    
                    for device in jsonData:
                        deviceKey = "{endpoint}/{deviceType}/{deviceId}".format(endpoint=endpoint, deviceType=deviceType, deviceId=device['id'])                        
                        deviceValue = device['name'] if len(device['label']) == 0 else device['label']
                        deviceCache = "{key}:{value}\n".format(key=deviceKey, value=deviceValue)
                        devicesFile.write(deviceCache)
                        
    devicesFile.close()
    
    return "Your SmartThings device cache has been updated"

    