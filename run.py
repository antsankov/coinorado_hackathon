#the default flask for running the server
from flask import Flask, request, redirect

#this is the twiml stuff
import twilio.twiml
from twilio.rest import TwilioRestClient 

#our own classes 
from persons import persons
from bank import bank
from account import account
import transaction

ACCOUNT_SID = "AC2a9e06ea97e4a1a785361f0e8064e870" 
AUTH_TOKEN = "bc96d318cbda7ef495f1418baed042f4" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
app = Flask(__name__)

#this function takes in two strings and cats them together with a space. 
def space(return_string, input):
    return (return_string + " " + input)

def bank_init():
    test_bank = bank()
    # test_person = person('+17208378697')
    # test_bank.addPerson('+17208378697', test_person)
    return test_bank

def parser(origination_number,input,bank):
    if(not(origination_number in bank.people.keys())):
        test_person = persons(origination_number)
        bank.add_person(origination_number)
    else:
        test_person = bank.get_person(origination_number)

    #looks up the person from the bank based on their origination number
    # user = bank.get_person(origination_number)
    
    #split the input 
    mod_input = input.split()
    verb = mod_input[0]
    
    #WITHDRAW
    if (verb == "withdraw"):
        accountID = mod_input[1]
        amount = mod_input[2]

        #check if the user has the account that they want to draw from 
        if (accountID in test_person.waccounts ):
            
            #get the actual account from the bank 
            account = bank.get_account(accountID)

            if (hasFunds(amount, account)):
                withdraw(account, test_person, amount)
                return "SUCCESS " + input

        else:
            return "Invalid/Unknown account"


    #DEPOSIT
    if (verb == "deposit"):
        accountID = mod_input[1]
        amount = mod_input[2]

        if (accountID in test_person.daccounts):
            
            account = bank.get_account(accountID)
            deposit(account,test_person,amount)
            return "SUCCESS " + input

        else:
            return "Invalid/Unknown account"
    
    #ADD       
    if (verb == "add"):
        phone_number = mod_input[1]
        if (not(phone_number in bank.people.keys())):
            bank.add_person(phone_number)
            return "Successfully added person with wallet of: " + bank.get_person(phone_number).address

        elif(phone_number == None):
            return "Must give phone number of new user"
        else:
            return "User has already been created"

    #CREATE
    if(verb == "create"):
        phone_number = mod_input[1]
        bank.add_account(phone_number)

    else:
        return "Unknown if withdrawl or deposit!"

#this actually crafts the message for the person. Currently it grabs all messages and only selects the first inbound one, we should find a way to reduce this
def returner(bank,debug):
    messages = client.messages.list() 
    for m in messages:
        if (m.direction == 'inbound' and debug == False):
            #you need to use m.from_ NOT m.From, this causes 
            return parser(m.from_,m.body,bank)

        if (m.direction == 'inbound' and debug == True):
            #you need to use m.from_ NOT m.From, this causes 
            return m.body
 
#this is the main route with the two possible verbs 
@app.route("/", methods=['GET', 'POST'])

#this is the responder function 
def responder():
    test_bank = bank_init()
    resp = twilio.twiml.Response()
    resp.message(returner(test_bank,False))
    return str(resp)


@app.route("/debug", methods=['GET', 'POST'])
def debugger():
    test_bank = bank_init()
    resp = twilio.twiml.Response()
    resp.message(returner(test_bank,True))
    return str(resp)


#this gets the server running.
if __name__ == "__main__":
    # print (parser("1111111","withdraw 555 48758475"))
    # print (parser("2222222","deposit 555 488923478923"))
    app.run(debug=True)

