class Pointer(object):

	def __init__(self,x,y):
		self.x=x
		self.y=y

	def moveup(self):
		self.y=self.y+1

	def movedown(self):
		self.y-=1

	def moveleft(self):
		self.x-=1

	def moveright(self):
		self.x+=1	

	def checkpos(self):
		print(self.x)
		print(self.y)
		print("Hello")
