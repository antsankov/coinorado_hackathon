from bank import bank
from parser import parser


def bank_init():
    test_bank = bank()
    # test_person = person('+17208378697')
    # test_bank.addPerson('+17208378697', test_person)
    return test_bank

def tester():
    test_bank = bank_init()
    #our m.from: +17208378697 m.body: what we want, bank
    
    #adds a user 
    print(parser("+17208378697","add +17208378675",test_bank))
    #gives their info
    print(parser("+17208378697","info",test_bank))
    #gives the balance
    print(parser("+17208378697","balance",test_bank))
    #add a dupilicate tester 
    print(parser("+17208378697","add +17208378675",test_bank))
    #creates an accoutn and prints an account number 
    print(parser("+17208378697","create +17208378675",test_bank))
    #creates an accoutn and prints an account number 
    print(parser("+17208378697","create +17208378675",test_bank))
    print(parser("+17208378697","add +57208378675",test_bank))
    print(parser("+17208378697","info +17208378675",test_bank))
    #print("Bank customers: " + str(test_bank.people))
    #print("Bank accounts" + str(test_bank.accounts))


if __name__ == "__main__":
    tester()
