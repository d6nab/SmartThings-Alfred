import json
import urllib
import urllib2
import string
from Feedback import Feedback

def login_command(query = ""):
    try:
        with open('email.txt'): pass
    except IOError:
        tmp = open("email.txt", "w")
        tmp.close()
    
    feedback = Feedback()
    # feedback.add_item('works')

    output = open("output.txt", "w")
    output.write(query)

    eFile = open("email.txt")
    e = eFile.read()
    eFile.close

    output.write("email : ")
    output.write(e)
    output.write("\nlength: ")
    output.write(str(e.__len__()))

    output.close()

    if e.__len__() == 0:
        arg = "email:{email}".format(email=query)
        feedback.add_item('Email', 'Enter your email address', arg)
        return feedback
    else:
        arg = "password:{password}".format(password=query)
        feedback.add_item('Password', 'Your password will not be stored', arg)
        # feedback.add_item('like a charm')
        return feedback
