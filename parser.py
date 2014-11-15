from persons import persons
from bank import bank
from account import account
import transaction

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
            return ("Successfully added person with wallet of: " + str(bank.get_person(phone_number).address))
        
        else:
            return "User has already been created"

    #CREATE
    if(verb == "create"):
        phone_number = mod_input[1]
        id = bank.add_account(phone_number)
        return id 
    else:
        return "Unknown if withdrawl or deposit!"