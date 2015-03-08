class Sloth (object): 

	content = [] 
	def __init__(self, name, stuffie):
		self.name = name
		self.stuffie = stuffie

	def hug(self): 
		return 'i lub u, {0}' .format(self.name)  

	def change_stuffie(self, new_stuffie): 
		if new_stuffie is None:
			raise ValueError('Give that sloth a stuffie!')

		self.stuffie = new_stuffie 

	def show(self): 
		return self.content

s = Sloth('Punkin', 'Giraffe')
print s.stuffie
s.stuffie = 'Manatee'
print s.stuffie
print s.hug()
s.change_stuffie('me')
print s.stuffie 
s.show()