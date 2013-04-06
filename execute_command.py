import json
import urllib
import urllib2
import string

def execute_command(query = ""):
    if query == "":
        query = "8ac8e3de3cb12d11013cb1fac5360046.on"
    args = string.split(query, ".")
    deviceId = args[0]
    command = args[1]
    appIdFile = open("smartAppId.txt")
    appId = appIdFile.read()
    authHeader = open("token.txt")
    url = "http://graph.api.smartthings.com/api/smartapps/installations/{app_Id}/switches/{device_Id}".format(app_Id=appId, device_Id=deviceId)

    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request = ""
    if command == "on":
        request = urllib2.Request(url, data='{"command":"on"}')
    else:
        request = urllib2.Request(url, data='{"command":"off"}')
    request.add_header('Content-Type', 'application/json')
    request.add_header('Authorization', authHeader.read())
    request.get_method = lambda: 'PUT'
    opener.open(request)

    return

