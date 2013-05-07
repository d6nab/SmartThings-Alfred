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
    executable = False
    if command == 'on' or command == 'off':
        executable = True

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
                    arg = "{endpoint}/switches/{device_id}.{command}".format(endpoint=endpoint, device_id=device['id'], command=command)
                    title = "Turn {command} {device}".format(command=command, device=device['label']) if command.__len__() > 1 else device['label']
                    feedback.addItem(title=title, subtitle=device['name'], arg=arg, valid=executable, autocomplete=labelElseName)

    return feedback
