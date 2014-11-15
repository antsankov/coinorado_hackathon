import transaction
from persons import persons
from account import account

class bank:

	def __init__(self):
		self.people = {}
		self.accounts = []

	#person to percent is dict between person object and and that it can withdraw
	def account_to_person(self, account, person, permission,amount):
		relation = [person,amount]
		if permission == 'w':
			account.add_withdrawer(relation)
		elif permission == 'd':
			account.add_depositer(person)

	def add_person(self, phone):
		p = {phone : persons(phone)}
		self.people.update(p)

	def add_account(self, account):
		self.accounts.append(account)
		
	def get_account(self, account_id):
		return self.accounts[account_id]

	def get_person(self, phone):
		return self.people[phone]



