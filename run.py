#the default flask for running the server
from flask import Flask, request, redirect

#this is the twiml stuff
import twilio.twiml
from twilio.rest import TwilioRestClient 

#our own classes 
from bank import bank
from parser import parser

ACCOUNT_SID = "AC2a9e06ea97e4a1a785361f0e8064e870" 
AUTH_TOKEN = "bc96d318cbda7ef495f1418baed042f4" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
app = Flask(__name__)

test_bank = bank()


#this function takes in two strings and cats them together with a space. 
def space(return_string, input):
    return (return_string + " " + input)

def bank_init():
    test_bank = bank()
    return test_bank

#this actually crafts the message for the person. Currently it grabs all messages and only selects the first inbound one, we should find a way to reduce this
def returner(bank,debug):
    messages = client.messages.list() 
    for m in messages:
        if (m.direction == 'inbound' and debug == False):
            #you need to use m.from_ NOT m.From, this causes 
            return parser(m.from_,m.body,bank)

        if (m.direction == 'inbound' and debug == True):
            #you need to use m.from_ NOT m.From, this causes keyword error  
            return m.body
 
#this is the main route with the two possible verbs, any methods after this runs automatically
@app.route("/", methods=['GET', 'POST'])
#this is the responder function 
def responder():
    resp = twilio.twiml.Response()
    resp.message(returner(test_bank,False))
    return str(resp)



@app.route("/debug", methods=['GET', 'POST'])

def debugger():
    resp = twilio.twiml.Response()
    resp.message(returner(test_bank,True))
    return str(resp)


#this gets the server running.
if __name__ == "__main__":
    app.run(debug=True)
