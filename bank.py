import account
import persons

class bank:

	def __init__(self):
		self.people = {}
		self.accounts = {}

	def add_person(self, phone, person):
		p = {phone : person}
		self.people.update(p)

	def add_acount(self, account_id, account):
		a = {account_id : account}
		self.accounts.update(a)

	def get_account(self, account_id):
		return self.accounts[account_id]

	def get_person(self, phone):
		return self.people[phone]

