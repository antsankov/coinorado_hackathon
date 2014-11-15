from persons import persons
from bank import bank
from account import account
import transaction
import money
import math

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
        #account = mod_input[1]
        return "balance {0}".format(caller.wallet.get_balance())
   
    #combine     
    if (verb == "combine"):
        identifier = mod_input[1]
        #password = mod_input[2]
        wallet = Wallet(identifier, 'Boondock2013')
        #failsafe: only import 10 satoshi max
        previous_balance = math.max(wallet.get_balance(), 10)
        ra = caller.address
        rw = caller.wallet
        wallet.send(r, s, wallet.get_address)
        current_balance = rw.get_balance()
        return "Successfully moved {0} satoshi from {1} to {2}: ".format(r, identifier, ra)

    #INFO
    if (verb == "info"):
        #account = mod_input[1]
        return "Blockchain Wallet: {0}\n Address: {1}".format(caller.wallet.identifier, caller.address.address)

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
    


    #ADD, this adds money to an account, gives a person the ability to access the account, what percent of the money they have access to     
    if (verb == "add"):
        #def account_to_person(self, account, person, permission, person_to_percent = 1.0):

        #this is the account you are sending the coins from
        account = mod_input[1]

        #this is the phone number you are sending the coins to. 
        desitnation_phone = mod_input[2]

        #this is the permission that you want to give the person 
        permission = mod_input[3]

        #this is the amount of coins you are sending 
        amount = mod_input[4]

        #this is the percent they can withdraw ONLY if they are actually withdrawers 
        percent = mod_input[5]

        #this checks if the persons phone number is in the bank keys 
        if (not(desitnation_phone in bank.people.keys())):
            return "Person doesn't exist"

        actual_amount = (amount * percent)

        if (not(hasFunds(account,amount))):
            return "Not enough coins to make transfer"

        #transfers from an account to a person: 
            # 1. take the account we are transferring from!
            # 2. the desitnation_phone we are sending it to. 
            # 3. permission whether they can take or depsoit
            # 4. the amount we are actually transferring
            # 5. the percent to transfer

        account_to_person(account,desitnation_phone,permission,actual_amount)


    #CREATE
    if(verb == "create"):
        phone_number = mod_input[1]
        id = bank.add_account(phone_number)
        return id 
    else:
        return "Unknown if withdrawl or deposit!"