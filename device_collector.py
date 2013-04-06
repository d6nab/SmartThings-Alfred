import json
import urllib
import urllib2
import string
from Feedback import Feedback

def device_collector(query = ""):
    feedback = Feedback()    
    
    args = string.split(query, " ")

    command = args[-1]
    executable = 'no'
    if command == 'on' or command == 'off':
        executable = 'yes'
    # feedback.add_item(command) # for testing
    
    appIdsFile = open("smartAppIds.txt")
    appIdsString = appIdsFile.read()
    appIds = appIdsString.split()
    appIdsFile.close()
    

    authHeaderFile = open("token.txt")
    authHeader = authHeaderFile.read()
    for appId in appIds:
        ### collect devices for each appId
        url = "http://graph.api.smartthings.com/api/smartapps/installations/%s/switches" % appId
        
        req = urllib2.Request(url)
        req.add_header('Authorization', authHeader)
        response = urllib2.urlopen(req)
        the_page = response.read()
        jsonData = json.loads(the_page)
            
        for device in jsonData:
            labelElseName = device['name'] if len(device['label']) == 0 else device['label']
            arg = "{deviceId}.{command}".format(deviceId=device['id'], command=command)
            feedback.add_item(device['label'], device['name'], arg, executable, labelElseName)
    
    
        
    return feedback

