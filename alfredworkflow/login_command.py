from alfred import Feedback
import os.path
import httplib


def login_command(query=""):
    try:
        conn = httplib.HTTPConnection("localhost", 2222)
        conn.request("GET", "/success")
        response = conn.getresponse()
        response.read()
        conn.close()
    except Exception, err:
        pass

    feedback = Feedback()

    if os.path.isfile("token.txt"):
        tokenFile = open("token.txt")
        token = tokenFile.read()
        tokenFile.close()
        if token.__len__() > 0:
            feedback.addItem(title="You are already authenticated with SmartThings")
            return feedback
    else:
        feedback.addItem(title="Authenticate with SmartThings",
                         subtitle="You will be forwarded to https://www.smartthings.com")
        return feedback
