from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient 

ACCOUNT_SID = "AC2a9e06ea97e4a1a785361f0e8064e870" 
AUTH_TOKEN = "bc96d318cbda7ef495f1418baed042f4" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
  

app = Flask(__name__)

#this function takes in two strings and cats them together with a space. 
def space(return_string, input):
    return (return_string + " " + input)

def parser(input):
    return_string = ""
    mod_input = input.split()

    #this checks if we have a w or d 
    if (mod_input[0] == "w"):
        return_string = space(return_string,mod_input[0])

        if (valid_account(mod_input[1])):
            return_string = space(return_string,mod_input[1])            
            print(return_string)

        else:
            return "Invalid/Unknown account"


    if (mod_input[0] == "d"):
        return_string = space(return_string,mod_input[0])

        if (valid_account(mod_input[1])):
            return_string = space(return_string,mod_input[1])            
            print(return_string)

        else:
            return "Invalid/Unknown account"

    else:
        return "Unknown if withdrawel or deposit!"

 
def valid_account(account):
    return True

#this actually crafts the message for the person. Currently it grabs all messages and only selects the first inbound one, we should find a way to reduce this
def returner():
    messages = client.messages.list() 
    for m in messages:
        if (m.direction == 'inbound'):
            return parser(m.body)
 
#this is the main route with the two possible verbs 
@app.route("/", methods=['GET', 'POST'])

#this is the responder function 
def responder():
    resp = twilio.twiml.Response()
    resp.message(returner())
    return str(resp)


#this gets the server running.
if __name__ == "__main__":
    print parser("w 555")
    app.run(debug=True)



