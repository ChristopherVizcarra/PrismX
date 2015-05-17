class algorithm():
	def __init__(self):
		self.input = ""
		self.variables = {}

	def set_input(self, temp):
		self.input = temp
		self.input = self.input.replace("\t", "")
		#self.input = self.input.replace(" ", "")
		self.input = self.input.split("\n")
		for x in self.input:
			if len(x) == 0:
				self.input.remove(x)

		#print self.input

		self.check()

	def check(self):
		a = 0
		while(1):
			temp = self.input[a]
			#temp = list(x)

			if list(temp.replace(" ", ""))[1] == "=":
				temp = list(temp.replace(" ", ""))
				self.equate(temp[0], temp[2:])

			else:
				temp = "".join(temp)
				while(1):
					try:
						exec(temp)
						break
					except:
						a += 1
						temp = temp.append(self.input[a])

			a += 1

	def equate(self, thisisvariablenumber1, thisisvariablenumber2):
		thisisvariablenumber2 = list(thisisvariablenumber2)
		try:
			self.variables[thisisvariablenumber1] = eval("".join([str(i) for i in thisisvariablenumber2]))

		except:
			for x in range(len(thisisvariablenumber2)):
				if thisisvariablenumber2[x] in self.variables:
					thisisvariablenumber2[x] = self.variables[thisisvariablenumber2[x]]

			self.variables[thisisvariablenumber1] = eval("".join([str(i) for i in thisisvariablenumber2]))

		print self.variables

x = algorithm()
x.set_input("""
	z=7
	y=z
	a = z * y
	for x in range(100): print"Hello world"
	""")