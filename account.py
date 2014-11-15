import random
from blockchain.wallet import Wallet
import blockchain.createwallet


class account:

	def __init__(self):
		self.account_id = self.create_id()
		self.withdrawers = []
		self.depositers = []
		temp = blockchain.createwallet.create_wallet('Boondock2013', 'c62026c6-89e3-4200-93a9-f51250ad1ea5')
		self.wallet = Wallet(temp.identifier, 'Boondock2013')
		self.address = self.wallet.new_address(('team_moorhead_'+self.account_id))
		# bank.add_account(self.account_id, self)

	def create_id(self):
		id = ''
		for i in range(0,15):
			id = id + str(random.randint(0,9))
		return id

	def pay_debts(self):
		for withdrawer in self.withdrawers:
			withdraw(self.account, withdrawer[0], withdrawer[1])

	def collect_debts(self):
		for depositer in self.depositers:
			deposit(self.wallet, depositer[0], depositer[1])
	
	#we make the withdrawer from a list of the person the money is owed to, and the mount actually owed  
	def add_withdrawer(self, person,amount):
		if (has_funds(self.account,amount)):
			self.withdrawers.append([person,amount])
		else:
			return "Not enough money to make deal"

	#we make this list by getting the person and the money they owe us
	def add_depositer(self, person,amount):
		self.depositers.append([person,amount])