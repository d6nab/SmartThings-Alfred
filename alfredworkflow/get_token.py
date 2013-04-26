import json
import urllib
import urllib2
import string

def get_token(query = ""):
    tmp = query

    if(tmp.startswith('email:')):
        email = open("email.txt", "w")
        args = string.split(tmp, ":")
        email.write(args[1])
        email.close()
        return ''
    else:
        emailFile = open("email.txt")
        email = emailFile.read()
        emailFile.close()
        args = string.split(tmp, ":")

        url = "http://graph.api.smartthings.com/oauth/token"
        values = {'grant_type' : 'password',
          'client_id' : 'ios',
          'client_secret' : '5d0a80ae-955e-11e2-83cf-dafe6709f8c0',
          'username': email,
          'password': args[1] }
        data = urllib.urlencode(values)

        req = urllib2.Request("{u}?{p}".format(u=url, p=data), data)
        req.add_header('Content-type', 'application/json')
        req.add_header('Accept', 'application/json')

        response = urllib2.urlopen(req)
        the_page = response.read()
        jsonData = json.loads(the_page)

        token = jsonData["access_token"]
        authHeader = open("token.txt", "w")
        authHeader.write("Bearer ")
        authHeader.write(token)
        authHeader.close()

        get_smart_app_ids()

        return "Logged in to the Alfred SmartApp" # this tells the next step that we're finished

    return


def get_smart_app_ids():
    output = open("output.txt", "w")
    output.write("CALLED METHOD!!!")


    url = 'http://graph.api.smartthings.com/api/smartapps/installations'
    req = urllib2.Request(url)
    authHeader = open("token.txt")
    req.add_header('Authorization', "Bearer %s" % authHeader.read())

    response = urllib2.urlopen(req)
    the_page = response.read()
    jsonData = json.loads(the_page)

    # store "Alfred Workflow" smartApp id
    alfredAppId = open("smartAppIds.txt", "w")
    for app in jsonData:
        appName = app["smartAppVersion"]["name"]
        if appName == "Alfred Workflow":
            alfredAppId.write(app["id"])
            alfredAppId.write(" ")
    alfredAppId.close()


    output.close()
    return
