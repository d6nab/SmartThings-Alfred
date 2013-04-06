import json
import urllib
import urllib2


url = 'http://graph.api.smartthings.com/api/smartapps/installations'
req = urllib2.Request(url)
authHeader = open("token.txt")
req.add_header('Authorization', authHeader.read())

response = urllib2.urlopen(req)
the_page = response.read()
jsonData = json.loads(the_page)

# store "Alfred Workflow" smartApp id
alfredAppId = open("smartAppId.txt", "w")
for app in jsonData:
    appName = app["smartAppVersion"]["name"]
    if appName == "Alfred Workflow":
        alfredAppId.write(app["id"])
alfredAppId.close()
