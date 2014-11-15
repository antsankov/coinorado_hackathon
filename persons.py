import random
from bank import bank
from account import account


class persons:

	def __init__(self, phone, permissions):
		self.phone = phone
		self.permissions = permissions
		self.id = create_id()
		self.password = create_password()
		self.wallet = create_wallet()
		self.accounts = []
		bank.add_person(phone, self)

	def create_id(self):
		id = ''
		for i in range(0,8):
			id = id + str(random.randint(0,9))
		return id

	def create_wallet(self):
		#FIXME
		return 0

	def withdraw(self, account_number):
		#FIXME
		return 0

	def deposit(self, account_number):
		#FIXME
		return 0

	def see_balance(self, account_number):
		#FIXME
		return 0

	def add_withdrawer(self, account_number, phone):
		a = account.get_account(account_number)
		p = self.get_person(phone)
		a.add_withdrawer(p)

	def get_person(self, phone):
		return bank.get_person(phone)

