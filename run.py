#the default flask for running the server
from flask import Flask, request, redirect

#this is the twiml stuff
import twilio.twiml
from twilio.rest import TwilioRestClient 

#our own classes 
from persons import persons
from bank import bank
from account import account

ACCOUNT_SID = "AC2a9e06ea97e4a1a785361f0e8064e870" 
AUTH_TOKEN = "bc96d318cbda7ef495f1418baed042f4" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

app = Flask(__name__)

#this function takes in two strings and cats them together with a space. 
def space(return_string, input):
    return (return_string + " " + input)

def parser(origination_number,input):
    #we are going to be using the origination number to lookup our account
    return_string = origination_number + " "
    mod_input = input.split()

    #this checks if we have a w or d 
    if (mod_input[0] == "withdraw"):
        return_string = space(return_string,mod_input[0])

        if (valid_account(mod_input[1])):
            return_string = space(return_string,mod_input[1])            

            account = account_lookup(mod_input[1])

            if (hasFunds(account,mod_input[2])):
                return_string = space(return_string,mod_input[2])
                return "SUCCESS " + return_string

        else:
            return "Invalid/Unknown account"


    #this checks if we have a w or d 
    if (mod_input[0] == "deposit"):
        return_string = space(return_string,mod_input[0])

        if (valid_account(mod_input[1])):
            return_string = space(return_string,mod_input[1])            

            account = account_lookup(mod_input[1])

            if (addFunds(account,mod_input[2])):
                return_string = space(return_string,mod_input[2])
                return "SUCCESS " + return_string

        else:
            return "Invalid/Unknown account"

    else:
        return "Unknown if withdrawl or deposit!"

def addFunds(account, number):
    return True

def accountLookup(number):
    return number

def hasFunds(account,amount):
    return True

#talk directly to the bank
def account_lookup(account):
    return 555
 
def valid_account(account):
    return True

#this actually crafts the message for the person. Currently it grabs all messages and only selects the first inbound one, we should find a way to reduce this
def returner():
    messages = client.messages.list() 
    for m in messages:
        if (m.direction == 'inbound'):
            return parser(m.From, m.Body)
 
#this is the main route with the two possible verbs 
@app.route("/", methods=['GET', 'POST'])

#this is the responder function 
def responder():
    resp = twilio.twiml.Response()
    resp.message(returner())
    return str(resp)


#this gets the server running.
if __name__ == "__main__":
    print (parser("1111111","withdraw 555 48758475"))
    print (parser("2222222","deposit 555 488923478923"))
    app.run(debug=True)



