import random
# import bitcoinpy.keyUtils
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
	
	def add_withdrawer(self, person):
		self.withdrawers.append(person)

	def add_depositer(self, person):
		self.depositers.append(person)