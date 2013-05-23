import json
import urllib2
import string
from alfred import Feedback
from settings import PROTOCOL, HOSTNAME
from http_server import stop


def device_collector(query=""):
    stop()

    feedback = Feedback()

    args = string.split(query, " ")

    command = args[-1]
    if len(command) < 1:
        command = args[-2]

    executable = False
    if command == 'on' or command == 'off':
        executable = True
    else:
        command = ''
    
    deviceFilter = ''
    for currentArg in args:
        if currentArg != command:
            deviceFilter += ' {ca}'.format(ca=currentArg)

    deviceFilter = deviceFilter.strip()

    tokenFile = open("token.txt")
    token = tokenFile.read()
    tokenFile.close()

    with open("endpoints.txt", 'r') as fh:
        for endpoint in fh.readlines():
            if endpoint.__len__() > 1:
                ### collect devices for each endpoint
                endpoint = endpoint.strip()
                url = "{protocol}://{hostname}{endpoint}/switches".format(protocol=PROTOCOL, hostname=HOSTNAME, endpoint=endpoint)

                req = urllib2.Request(url)
                req.add_header('Authorization', "Bearer %s" % token)
                response = urllib2.urlopen(req)
                the_page = response.read()
                jsonData = json.loads(the_page)
                
                for device in jsonData:                        
                    labelElseName = device['name'] if len(device['label']) == 0 else device['label']
                    if len(deviceFilter) > 0:
                        if not deviceFilter in labelElseName:
                            continue

                    arg = "{endpoint}/switches/{device_id}.{command}".format(endpoint=endpoint, device_id=device['id'], command=command)
                    title = "Turn {command} {device}".format(command=command, device=device['label']) if command.__len__() > 1 else labelElseName
                    feedback.addItem(title=title, subtitle=device['name'], arg=arg, valid=executable, autocomplete=' {l}'.format(l=labelElseName))

    return feedback
