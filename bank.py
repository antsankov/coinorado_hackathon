import transaction
from persons import persons
from account import account

class bank:

	def __init__(self):
		self.people = {}
		self.accounts = {}
		self.atop = {}

	#person to percent is dict between person object and and that it can withdraw
	def account_to_person(self, account, person, permission, person_to_percent = 1.0):
		self.atop.update({account : person_to_percent})
		if permission == 'w':
			account.add_withdrawer(person)
		elif permission == 'd':
			account.add_depositer(person)

	def add_person(self, phone):
		p = {phone : persons(phone)}
		self.people.update(p)
		

	def add_account(self, phone_number):
		temp_a = account()
		self.atop.update({temp_a : self.get_person(phone_number)})
		a = {temp_a.account_id : temp_a}
		self.accounts.update(a)

	def get_account(self, account_id):
		return self.accounts[account_id]

	def get_person(self, phone):
		return self.people[phone]



