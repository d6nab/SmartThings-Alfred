import json
import urllib
import urllib2
import string

def execute_command(query = ""):
    
    args = string.split(query, ".")
    appId = args[0]
    deviceId = args[1]
    command = args[2]
    
    url = "http://graph.api.smartthings.com/api/smartapps/installations/{app_Id}/switches/{device_Id}".format(app_Id=appId, device_Id=deviceId)
    request = ""
    if command == "on":
        request = urllib2.Request(url, data='{"command":"on"}')
    else:
        request = urllib2.Request(url, data='{"command":"off"}')

    authHeaderFile = open("token.txt")
    authHeader = authHeaderFile.read()
    authHeaderFile.close()
    request.add_header('Authorization', authHeader)
    request.add_header('Content-Type', 'application/json')
    request.get_method = lambda: 'PUT'

    opener = urllib2.build_opener(urllib2.HTTPHandler)
    opener.open(request)

    return

