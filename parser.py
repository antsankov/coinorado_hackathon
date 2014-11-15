from persons import persons
from bank import bank
from account import account
import transaction
import money

def parser(origination_number,input,bank):
    
    if(not(origination_number in bank.people.keys())):
        caller = persons(origination_number)
        bank.add_person(origination_number)
    else:
        caller = bank.get_person(origination_number)
    
    #split the input 
    mod_input = input.split()
    verb = mod_input[0]
    
    #Amount account
    if (verb == "amount"):
        account = mod_input[1]
        return bank.get_account(account).wallet.get_balance()
   
    #WITHDRAW
    if (verb == "withdraw"):
        accountID = mod_input[1]
        amount = mod_input[2]

        #check if amount is valid
        amount = get_satoshis(amount)
        if(amount < 0):
            return "Invalid quantity specified: amount must be a valid currency valued at greater than 1 satoshi"


        #check if the user has the account that they want to draw from 
        if (accountID in caller.waccounts ):
            
            #get the actual account from the bank 
            account = bank.get_account(accountID)

            if (hasFunds(amount, account)):
                withdraw(account, caller, amount)
                return "SUCCESS " + input

        else:
            return "Invalid/Unknown account"


    #DEPOSIT
    if (verb == "deposit"):
        accountID = mod_input[1]
        amount = mod_input[2]

        #check if amount is valid
        amount = get_satoshis(amount)
        if(amount < 0):
            return "Invalid quantity specified: amount must be a valid currency valued at greater than 1 satoshi"

        if (accountID in caller.daccounts):
            
            account = bank.get_account(accountID)
            deposit(account,caller,amount)
            return "SUCCESS " + input

        else:
            return "Invalid/Unknown account"
    
    #ADD       
    if (verb == "add"):
        phone_number = mod_input[1]
        permission = mod_input[2]
        percent = mod_input[3]

        if (not(phone_number in bank.people.keys())):
            bank.add_person(phone_number)
            bank.accout_to_person()
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