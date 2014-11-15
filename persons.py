import random
from account import account
import bitcoinpy.keyUtils

class persons:

	def __init__(self, phone):
		self.phone = phone
		# self.password = create_password()
		self.wallet = Wallet.__init__('team_moorhead_' + self.account_id, '1234567890asdfghjkl')
		self.address = self.wallet.new_address()
		self.waccounts = []
		self.daccounts = []
		# bank.add_person(phone, self)
	
	def add_withdraw(self, account):
		self.waccounts.append(account)

	def add_deposit(self, account):
		self.daccounts,append(account)

	# def add_withdrawer(self, account_number, phone):
	# 	a = account.get_account(account_number)
	# 	p = self.get_person(phone)
	# 	a.add_withdrawer(p)
