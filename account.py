import random
import bitcoinpy.keyUtils
from blockchain.wallet import Wallet
import blockchain


class account:

	def __init__(self):
		self.account_id = create_id()
		self.withdrawers = []
		self.depositers = []
		temp = create_wallet('Boondock2013', 'bitcoin')
		self.wallet = Wallet(temp.identifier, 'Boondock2013')
		self.address = self.wallet.new_address()
		# bank.add_account(self.account_id, self)

	def create_id(self):
		id = ''
		for i in range(0,15):
			id = id + str(random.randint(0,9))
		return id

	def add_withdrawer(self, person):
		self.withdrawers.append(person)

	def add_depositer(self, person):
		self.depositers.append(person)