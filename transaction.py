from account import account
from persons import persons

#Send from person to account
def deposit(account, person, amount):
	aa = account.address
	person.wallet.send(aa, amount, person.address)

#Send from account to person
def withdraw(account, person, amount):
	pa = person.address
	account.wallet.send(pa, amount, account.address)

def has_funds( amount, account):
	if(amount <= acount.wallet.get_balance()):
		return True
	else:
		False

