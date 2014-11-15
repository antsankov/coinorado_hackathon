from account import account
from persons import persons

#Send from person to account
def deposit(account, person, amount,tip):
	aa = account.address
	person.wallet.send(aa, amount, person.address,tip,"sent with bxb!")

#Send from account to person
def withdraw(account, person, amount):
	pa = person.address
	account.wallet.send(pa, amount, account.address)

#Checks if they have the account 
def has_funds( amount, account):
	if(amount <= acount.wallet.get_balance()):
		return True
	else:
		return False

# def pay_debts(withdrawers):
# 	for withdrawer in withdrawers:
# 		withdraw(self.account, withdrawer[0], withdrawer[1])

# def collect_debts(depositers):
# 	for depositer in depositers:
# 		deposit(self.wallet, depositer[0], depositer[1])

