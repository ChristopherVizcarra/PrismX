class algorithm():
	def __init__(self):
		self.input = ""
		self.variables = {}
		self.condition = 0	#Determines how deep the code is at

	def set_input(self, temp):
		self.input = temp
		self.input = self.input.split("\n")
		self.check()

	def check(self):
		a = 0
		while(1):
			try:
				temp = self.input[a]
				temp = temp[:-1]
				temp1 = temp.lstrip()
				temp1 = temp1.split(" ")

			except:
				break

			if temp.count("\t") < self.condition:
				while temp.count("\t") < self.condition:
					self.condition -= 1

			if temp1 == [""]:	#if line is empty, do nothing
				pass

			elif len(temp1) > 1 and temp1[1] == "=" and self.condition == temp.count("\t"):	#if line is assignment, assign
				self.equate(temp1[0], temp1[2:])

			elif temp1[0] == "if" and "(" in temp1[1] and self.condition == temp.count("\t"):	#if line is if
				temp2 = temp1[1].split("(")
				temp2.remove("")
				temp2 += temp1[2:]
				self.conditional(temp2)

			elif temp1[0] == "break" and len(temp1) == 1 and self.condition == temp.count("\t"):	#break
				self.condition -= 1		

			elif temp1[0] == "for" and "(" in temp1[1] and self.condition == temp.count("\t"):	#for loop
				pass

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
			eval(" ".join([str(i) for i in thisisvariablenumber1]))

		except:
			thisisvariablenumber1 = list(thisisvariablenumber1)
			for x in range(len(thisisvariablenumber1[1:])):
				if thisisvariablenumber1[x] in self.variables:
					thisisvariablenumber1[x] = self.variables[thisisvariablenumber1[x]]

		if eval(" ".join([str(i) for i in thisisvariablenumber1])) == True:
			self.condition += 1
		else:
			self.condition = 0

x = algorithm()
x.set_input("""
z = 7;
y = z;
a = z * y;
if (z == 7 and y == 7)
	w = 8;
	break;
	w = 100;
""")