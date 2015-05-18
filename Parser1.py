class algorithm():
	def __init__(self):
		self.input = ""
		self.variables = {}
		self.condition = 0	#Determines how deep the code is at

	def set_input(self, temp):
		self.input = temp
		self.input = self.input.split("\n")
		for x in self.input:
			if len(x) == 0:
				self.input.remove(x)

		self.check()

	def check(self):
		a = 0
		while(1):
			try:
				temp = self.input[a]
				temp = temp[:-1]
				temp1 = list(temp.replace(" ", "").replace("\t", ""))
				if temp.count("\t") < self.condition:
					while temp.count("\t") < self.condition:
						self.condition -= 1
			except:
				break


			if temp1 == []:	#if line is empty, do nothing
				pass

			elif temp1[1] == "=" and temp.count("\t") == self.condition:	#if line is assignment, assign
				self.equate(temp1[0], temp1[2:])

			elif temp1[0] == "i" and temp1[1] == "f" and temp1[2] == "(" and temp.count("\t") == self.condition:	#if line is if
				temp2 = temp1[3:]
				temp2 = "".join(temp2)
				self.conditional(temp2)

			elif temp1[0] == "b" and temp1[1] == "r" and temp1[2] == "e" and temp1[3] == "a" and temp1[4] == "k" and len(temp1) == 5:
				self.condition -= 1			
			#elif

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

	def conditional(self, thisisvariablenumber1):
		try:
			eval("".join([str(i) for i in thisisvariablenumber1]))

		except:
			thisisvariablenumber1 = list(thisisvariablenumber1)
			for x in range(len(thisisvariablenumber1[1:])):
				if thisisvariablenumber1[x] in self.variables:
					thisisvariablenumber1[x] = self.variables[thisisvariablenumber1[x]]


		if eval("".join([str(i) for i in thisisvariablenumber1])) == True:
			self.condition += 1
		else:
			self.condition = 0

x = algorithm()
x.set_input("""
z=7;
y=z;
a = z * y;
if (z == 7)
	w = 8;
	break;
	w = 100;
""")