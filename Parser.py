class algorithm():
	def __init__(self, temp):
		self.input = list(temp)
		self.input = [value for value in self.input if value != " "]
		#for x in range(len(self.input)):
		#	if self.input[x] == "-" and self.input[x+1] == ""
		#print self.input

	def check(self):
		if len(self.input) == 1:
			return self.input[0]

		if self.input[1] == "=":
			x = algorithm(self.input[2:])
			return self.equate(self.input[0], x.check())

		elif self.input[1] == "+":
			x = algorithm(self.input[2:])
			return self.add(self.input[0], x.check())

		elif self.input[1] == "-":
			x = algorithm(self.input[2:])
			return self.subtract(self.input[0], x.check())

		elif self.input[1] == "*":
			x = algorithm(self.input[2:])
			return self.multiply(self.input[0], x.check())

		elif self.input[1] == "/":
			x = algorithm(self.input[2:])
			return self.divide(self.input[0], x.check())

		else:
			return self.input[0]

	def equate(self, x, y):
		x = y
		return x

	def add(self, x, y):
		return float(x) + float(y)

	def subtract(self, x, y):
		return float(x) - float(y)

	def multiply(self, x, y):
		return float(x) * float(y)

	def divide(self, x, y):
		return float(x) / float(y)

x = algorithm("y = 9 + 1 + 1")
print x.check()