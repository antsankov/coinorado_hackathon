import random
import bank
import persons

class account:

	def __init__(self, creator_id):
		self.creator_id = creator_id
		self.account_id = create_id()
		self.account_wallet = create_wallet()
		self.balance = 0
		self.withdrawers = []
		bank.add_account(self.account_id, self)

	def create_id(self):
		id = ''
		for i in range(0,15):
			id = id + str(random.randint(0,9))
		return id

	def create_wallet(self):
		#FIXEME
		return 0

	def get_withdrawal(self, amount):
		#FIXEME
		return 0

	def do_deposit(self, amount):
		#FIXME
		return 0

	def add_withdrawer(self, person):
		self.withdrawers.append(person)

	def get_account(self, account_id):
		return banks.get_account

