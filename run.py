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

    #looks up the person from the bank based on their origination number
    user = bank.get_person(origination_number)
    
    #split the input 
    mod_input = input.split()
    
    verb = mod_input[0]
    accountID = mod_input[1]
    amount = mod_input[2]


    #this checks if we are withdrawing
    if (verb == "withdraw"):

        #check if the user has the account that they want to draw from 
        if (user.waccounts.contains(accountID)):
            
            #get the actual account from the bank 
            account = bank.get_account(accountID)

            if (account.hasFunds(amount)):
                account.get_withdrawl(amount)
                return "SUCCESS " + input

        else:
            return "Invalid/Unknown account"


    #this checks if we have a w or d 
    if (verb == "deposit"):

        if (user.daccounts.contains(accountID)):
            
            account = bank.get_account(accountID)
            account.do_deposit(amount)
            return "SUCCESS " + input

        else:
            return "Invalid/Unknown account"

    else:
        return "Unknown if withdrawl or deposit!"

#this actually crafts the message for the person. Currently it grabs all messages and only selects the first inbound one, we should find a way to reduce this
def returner():
    messages = client.messages.list() 
    for m in messages:
        if (m.direction == 'inbound'):
            #you need to use m.from_ NOT m.From, this causes 
            return parser(m.from_,m.body)
 
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



