import json
import urllib2
import string
from Feedback import Feedback


def device_collector(query=""):
    feedback = Feedback()

    args = string.split(query, " ")

    command = args[-1]
    executable = 'no'
    if command == 'on' or command == 'off':
        executable = 'yes'
    # feedback.add_item(command) # for testing

    tokenFile = open("token.txt")
    token = tokenFile.read()
    tokenFile.close()

    with open("endpoints.txt", 'r') as fh:
        for endpoint in fh.readlines():
            if endpoint.__len__() > 1:
                ### collect devices for each endpoint
                endpoint = endpoint.strip()
                url = "https://graph.api.smartthings.com%s/switches" % endpoint

                req = urllib2.Request(url)
                req.add_header('Authorization', "Bearer %s" % token)
                response = urllib2.urlopen(req)
                the_page = response.read()
                jsonData = json.loads(the_page)

                for device in jsonData:
                    labelElseName = device['name'] if len(device['label']) == 0 else device['label']
                    arg = "{endpoint}/switches/{device_id}.{command}".format(endpoint=endpoint, device_id=device['id'], command=command)
                    title = "Turn {command} {device}".format(command=command, device=device['label']) if command.__len__() > 1 else device['label']
                    feedback.add_item(title, device['name'], arg, executable, labelElseName)

    return feedback
