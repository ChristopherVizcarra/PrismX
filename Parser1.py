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
				temp1 = list(temp.replace(" ", ""))
				if temp1.count("\t") < self.condition:
					while temp1.count("\t") < self.condition:
						self.condition -= 1
			except:
				break


			if temp1 == []:	#if line is empty, do nothing
				pass

			elif list(temp.replace(" ", "").replace("\t", ""))[1] == "=" and temp1.count("\t") == self.condition:	#if line is assignment, assign
				temp2 = list(temp.replace(" ", "").replace("\t", ""))
				self.equate(temp2[0], temp2[2:])

			elif list(temp.replace(" ", "").replace("\t", ""))[0] == "i" and list(temp.replace(" ", "").replace("\t", ""))[1] == "f" and list(temp.replace(" ", "").replace("\t", ""))[2] == "(" and temp1.count("\t") == self.condition:	#if line is if
				temp2 = list(temp.replace(" ", "").replace("\t", ""))
				temp2 = temp2[3:]
				temp2 = "".join(temp2)
				self.conditional(temp2)
			
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
""")