import urllib2
import string
from settings import PROTOCOL, HOSTNAME


def execute_command(query=""):
    args = string.split(query, ".")
    url = args[0]
    command = args[1]

    url = "{protocol}://{hostname}{url}".format(protocol=PROTOCOL, hostname=HOSTNAME, url=url)
    
    requestBody = '{"command":"' + "{command}".format(command=command) + '"}'
    request = urllib2.Request(url, data=requestBody)

    tokenFile = open("token.txt")
    token = tokenFile.read()
    tokenFile.close()
    request.add_header('Authorization', "Bearer %s" % token)
    request.add_header('Content-Type', 'application/json')
    request.get_method = lambda: 'PUT'

    opener = urllib2.build_opener(urllib2.HTTPHandler)
    opener.open(request)

    return
