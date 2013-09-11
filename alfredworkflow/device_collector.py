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

    switchCommandsFile = open("commands.switches.txt")
    switchCommands = switchCommandsFile.read()
    switchCommandsFile.close()
    
    lockCommandsFile = open("commands.locks.txt")
    lockCommands = lockCommandsFile.read()
    lockCommandsFile.close()
    
    executable = False    
    if command in switchCommands or command in lockCommands:
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
        try:
            deviceFile = open("devices.txt")
            for deviceDataString in deviceFile.readlines():
                deviceData = string.split(deviceDataString, ":")
                deviceEndpoint = deviceData[0].strip()
                deviceLabel = deviceData[1].strip()
    
                if len(deviceFilter) > 0:
                    if not deviceFilter.lower() in deviceLabel.lower():
                        continue
    
                arg = "{deviceEndpoint}.{command}".format(deviceEndpoint=deviceEndpoint, command=command)
                
                title = deviceLabel
                if command.__len__() > 1:
                    if command in switchCommands:
                        title = "Turn {command} {device}".format(command=command, device=deviceLabel)
                    else:
                        title = "{command} {device}".format(command=command.capitalize(), device=deviceLabel)
    
                feedback.addItem(title=title, subtitle=deviceLabel, arg=arg, valid=executable, autocomplete=' {l}'.format(l=deviceLabel))
            
            deviceFile.close()
        except IOError:
            print "Uh oh"
    
    return feedback
