import json
import urllib2


url = 'https://graph.api.smartthings.com/api/smartapps/endpoints'
req = urllib2.Request(url)
token = open("token.txt")
req.add_header('Authorization', "Bearer %s" % token.read())
token.close()

response = urllib2.urlopen(req)
the_page = response.read()
jsonData = json.loads(the_page)

# store "Alfred Workflow" endpoint url
endpointFile = open("endpoints.txt", "w")
for endpoint in jsonData:
    endpointFile.write(endpoint["url"] + "\n")
endpointFile.close()
