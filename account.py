import random
from bank import bank
import bitcoinpy.keyUtils
from blockchain.wallet import Wallet
import transaction

class account:

	def __init__(self):
		self.account_id = create_id()
		self.withdrawers = []
		self.depositers = []
		self.wallet = Wallet.__init__('team_moorhead_' + self.account_id, '1234567890asdfghjkl')
		self.address = self.wallet.new_address()
		bank.add_account(self.account_id, self)

	def create_id(self):
		id = ''
		for i in range(0,15):
			id = id + str(random.randint(0,9))
		return id

	def add_withdrawer(self, person):
		self.withdrawers.append(person)

	def add_depositers(self, person):
		self.depositers.append(person)