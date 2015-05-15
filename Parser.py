class algorithm():
	def __init__(self, temp):
		self.input = list(temp)
		self.input = [value for value in self.input if value != " "]

		for x in range(len(self.input)):
			if self.input[x] == "-":
				self.input[x+1] = int(self.input[x+1]) * -1
				self.input[x] = "+"
		x = 0
		while len(self.input) > 1 and self.check_float(self.input[x]) == True and self.input[x+1] not in ["-", "+", "/", "*", "(", ")"]:
			self.input[x] = str(self.input[x]) + str(self.input[x+1])
			self.input.pop(x+1)
		print self.input

	def check_float(self, temp):
		try:
			float(temp)
			return True
		except:
			return False

	def check(self):
		if "(" in self.input:
			a = 0
			for x in self.input:
				if x == ")" and "(" not in self.input[a:]:
					break
				a += 1
			x = algorithm(self.input[self.input.index("(")+1:a])
			y = x.check()
			self.input = self.input[a+1:]
			self.input.insert(0, y)

		if len(self.input) == 1:
			return self.input[0]
		
		if self.input[1] == "*":
			x = algorithm(self.input[2:])
			return self.multiply(self.input[0], x.check())

		elif self.input[1] == "/":
			x = algorithm(self.input[2:])
			return self.divide(self.input[0], x.check())

		elif self.input[1] == "+":
			x = algorithm(self.input[2:])
			return self.add(self.input[0], x.check())

		#return self.input[0]

	def equate(self, x, y):
		x = y
		return x

	def add(self, x, y):
		return float(x) + float(y)

	def multiply(self, x, y):
		return float(x) * float(y)

	def divide(self, x, y):
		return float(x) / float(y)

x = algorithm("y = ((100.1 / 10) + 10) / 2")
print x.check()