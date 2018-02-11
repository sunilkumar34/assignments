class Bank(object):

	def __init__(self,account,balance):
		self.account=account
		self.balance=balance

	def withdraw(self,draw):
		self.balance-=draw
		print(self.balance)

	def deposit(self,dep):
		self.balance+=dep
		print(self.balance)

	def checkbal(self):
		print(self.balance)