import random
from account import account
# import bitcoinpy.keyUtils
from blockchain.wallet import Wallet
import blockchain.createwallet

class persons:

	def __init__(self, phone):
		self.phone = phone
		# self.password = create_password()
		temp = blockchain.createwallet.create_wallet('Boondock2013', 'c62026c6-89e3-4200-93a9-f51250ad1ea5')
		self.wallet = Wallet(temp.identifier, 'Boondock2013')
		self.address = self.wallet.new_address(('team_moorhead_' + phone))

	
	def add_withdraw(self, account):
		self.waccounts.append(account)

	def add_deposit(self, account):
		self.daccounts.append(account)

	def add_account(self,acount):
		self.accounts.append(account)

	# def add_withdrawer(self, account_number, phone):
	# 	a = account.get_account(account_number)
	# 	p = self.get_person(phone)
	# 	a.add_withdrawer(p)
