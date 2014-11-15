import transaction
from persons import persons
from account import account

class bank:

	def __init__(self):
		#self.people = {}
		self.accounts = {}

	#person to percent is dict between person object and and that it can withdraw
	def account_to_person(self, account, person, permission,amount):
		relation = [person,amount]
		if permission == 'w':
			account.add_withdrawer(relation)
		elif permission == 'd':
			account.add_depositer(person)

	# def add_person(self, phone):
	# 	p = {phone : persons(phone)}
	# 	self.people.update(p)

	def add_account(self, phone, it, ad, pw):
		act = account(phone, it, ad, pw)
		#print "phone = {0}".format(phone)
		p = {phone : act}
		self.accounts.update(p)
		
	def get_account(self, phone):
		#print "phone = {0}".format(phone)
		return self.accounts[phone]

	# def get_person(self, phone):
	# 	return self.people[phone]



