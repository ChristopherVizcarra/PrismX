import lex

class syntax():
	def __init__(self):
		self.text = ""
		self.lex = lex.lexical_analysis()
		self.input = []
		self.parse = [0]
		self.table = []

	def set_input(self, temp):
		temp = temp.rstrip().split("\n")
		self.text = temp

	def algorithm(self):
		for x in self.text:
			self.lex.set_text(list(x))
			self.input = self.lex.main()

		self.setup()

		print self.input
		#temp = 0
		#while 1:
		#	temp = self.input.pop(0)
		#	temp1 = self.parse[-1:]

			#if temp == 
			
	def setup(self):
		temp = [5, None, None, 4, None, None, 1, 2, 3]
		self.table.append(temp)

		temp = [None, 6, None, None, "accept", None, None, None]
		self.table.append(temp)

		temp = [None, -2, 7, None, -2, -2, None, None, None]
		self.table.append(temp)

		temp = [None, -4, -4, None, -4, -4, None, None, None]
		self.table.append(temp)

		temp = [5, None, None, 4, None, None, 8, 2, 3]
		self.table.append(temp)

		temp = [None, -6, -6, None, -6, -6, None, None, None]
		self.table.append(temp)

		temp = [5, None, None, 4, None, None, None, 9, 3]
		self.table.append(temp)

		temp = [5, None, None, 4, None, None, None, None, 10]
		self.table.append(temp)

		temp = [None, 6, None, None, 11, None, None, None, None]
		self.table.append(temp)

		temp = [None, -1, 7, -1, -1, None, None, None]
		self.table.append(temp)

		temp = [None, -3, -3, None, -3, -3, None, None, None]
		self.table.append(temp)

		temp = [None, -5, -5, None, -5, -5, None, None, None]
		self.table.append(temp)