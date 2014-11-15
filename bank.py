import transaction

class bank:

	def __init__(self):
		self.people = {}
		self.accounts = {}
		self.atop = {}

	#person to percent is dict between person object and and that it can withdraw
	def acount_to_person(self, account, person_to_percent):
		self.atop.update({acount : person_to_percent})

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



