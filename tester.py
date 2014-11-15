from bank import bank
from parser import parser


def tester():
    test_bank = bank()

    #adds a user
    #alex
    print(parser("+17208378697","create 2666f08a-bfbb-42fb-80f8-e1ef974d5343 1Edw3z8dkgjqch5UFvkgBuUeaP2mAU2LvT 1234567890", test_bank))
    #sam create 2666f08a-bfbb-42fb-80f8-e1ef974d5343 1Edw3z8dkgjqch5UFvkgBuUeaP2mAU2LvT 1234567890
    print(parser("+17209991335","create 4620ffe2-86d6-4b63-ac16-4b8decfaa6f5 1KoQFBAEASCykCmnvK4kz7FRV4a1bqQu1Q Boondock2013", test_bank))
    #C1rissalazar       
    print(parser("+15122842178","create c972c797-2595-4fb6-91e4-0547ef268c80 1G4kUxVk8wEfKCwNehmP9Fot4pAnAJMAaY C1rissalazar", test_bank))

    #gives their acount_info alex
    print(parser("+17208378697","acount_info",test_bank))
    #gives the balance
    print(parser("+17208378697","balance",test_bank))

        #gives their acount_info sam
    print(parser("+17209991335","acount_info",test_bank))
    #gives the balance
    print(parser("+17209991335","balance",test_bank))

        #gives their acount_info cris
    print(parser("+15122842178","acount_info",test_bank))
    #gives the balance
    print(parser("+15122842178","balance",test_bank))

    #account_to_person(account,desitnation_phone,permission,actual_amount)
    #print (parser("+17208378697","a"))

    #add a dupilicate tester 
    #print(parser("+17208378697","combine 4620ffe2-86d6-4b63-ac16-4b8decfaa6f5 1KoQFBAEASCykCmnvK4kz7FRV4a1bqQu1Q" ,test_bank))
    #gives the balance
    #print(parser("+17208378697","balance",test_bank))
    # print(parser("+17208378697","add +17208378675",test_bank))
    # #creates an accoutn and prints an account number 
    # print(parser("+17208378697","create +17208378675",test_bank))
    # #creates an accoutn and prints an account number 
    # print(parser("+17208378697","create +17208378675",test_bank))
    # # print(parser("+17208378697","add +57208378675",test_bank))
    # # print(parser("+17208378697","acount_info +17208378675",test_bank))
    # #print("Bank customers: " + str(test_bank.people))
    # #print("Bank accounts" + str(test_bank.accounts))


if __name__ == "__main__":
    tester()
