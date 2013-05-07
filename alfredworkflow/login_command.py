from alfred import Feedback
import os.path
from http_server import stop


def login_command(query=""):
    stop()

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
