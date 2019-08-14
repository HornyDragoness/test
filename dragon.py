class Dragon:
	def __init__(self, color, alignment, name):
		self.color = color
		self. alignment = alignment
		self.name = name

	def fire_breath(self):
		print(self.name + " uses breath weapon.")

	def get_description(self):
		print(self.name + " is a " + self.color + " " + self.alignment + " dragon.")

	def roar(self):
		print(self.name + " roars into the sky.")


shanar = Dragon("black", "C-N", "Shanar")
shanar.get_description()
print('')
shanar.fire_breath()
shanar.roar()
