class algorithm():
	def __init__(self):
		self.input = ""
		self.variables = {}
		self.condition = 0	#Determines how deep the code is at
		self.trial = {}

	def set_input(self, temp):
		self.input = temp
		self.input = self.input.split("\n")
		self.check()

	def check(self, b = None):
		a = 0
		while(1):
			try:
				if b == None:
					temp = self.input[a]
				else:
					temp = b[a]
				temp = temp[:-1]
				temp1 = temp.lstrip()
				temp1 = temp1.split(" ")

			except:
				break

			if temp.count("\t") < self.condition:
				while temp.count("\t") < self.condition:
					self.condition -= 1

			if self.condition != temp.count("\t") or temp1 == [""]:
				pass

			elif len(temp1) > 1 and "=" in temp1[1]:	#if line is assignment, assign
				if len(temp1[1]) > 1:
					temp1[1] = temp1[1].split("=")
					temp1[1].remove("")
					temp1[2:] = list(temp1[0]) + temp1[1] + temp1[2:]

				if temp1[2][0] == "<":
					z = list(temp1[2])
					z.remove("<")
					temp1[2] = "".join([str(i) for i in z])
					z = list(temp1[-1])
					z.remove(">")
					temp1[-1] = "".join([str(i) for i in z])

				temp1[0] = list(temp1[0])
				temp1[0].remove("|")
				temp1[0] = "".join([str(i) for i in temp1[0]])
				temp1[-1] = temp1[-1].split("|")[0]
	
				self.equate(temp1[0], temp1[2:])

			elif (temp1[0] == "if" or (temp1[0] == "elif" and self.trial[self.condition] == -1)) and "(" in temp1[1]:	#if line is if
				#temp2 = temp1[1].split("(")
				#temp2.remove("")
				#temp2 += temp1[2:]

				temp1[-1] += ")"
				print temp1[1:]

				self.conditional(temp1[1:])

			elif temp1[0] == "els" and len(temp1) == 1 and self.trial[self.condition] == -1:
				self.conditional([1])

			elif temp1[0] == "break" and len(temp1) == 1:	#break
				self.condition -= 1		

			elif temp1[0] == "for" and "(" in temp1[1]:	#for loop
				temp2 = " ".join([str(i) for i in temp1])
				temp2 = temp2.split("(")
				temp2[1] = temp2[1].split(";")
				self.forer(temp2[1], a)

			elif temp1[0] == "do" and len(temp1) == 1:
				self.do_whiler(a)

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

	def conditional(self, thisisvariablenumber1, thisisvariablenumber2=0):
		thisisvariablenumber1 = list(thisisvariablenumber1)

		for x in range(len(thisisvariablenumber1)):
			try:
				thisisvariablenumber1[x] = list(thisisvariablenumber1[x])
				thisisvariablenumber1[x] = [value for value in thisisvariablenumber1[x] if value != "(" and value != ")"]
				thisisvariablenumber1[x] = "".join([str(i) for i in thisisvariablenumber1[x]])

				if thisisvariablenumber1[x]  in self.variables:
					thisisvariablenumber1[x] = self.variables[thisisvariablenumber1[x]]
			except:
				pass

		if eval(" ".join([str(i) for i in thisisvariablenumber1])) == True and thisisvariablenumber2 == 0:
			self.trial[self.condition] = self.condition
			self.condition += 1
		elif eval(" ".join([str(i) for i in thisisvariablenumber1])) == True and thisisvariablenumber2 == 1:
			return self.condition
		elif eval(" ".join([str(i) for i in thisisvariablenumber1])) == True and thisisvariablenumber2 == 2:
			return True
		else:
			self.trial[self.condition] = -1

	def forer(self, thisisvariablenumber1, linenumber):
		print thisisvariablenumber1
		temp = thisisvariablenumber1[0].split(" ")[0]
		temp = list(temp)
		temp = "".join([str(i) for i in temp[1:]])

		temp1 = thisisvariablenumber1[0].split(" ")[2:]
		temp2 = list(temp1[-1])
		temp2.pop()
		temp2 = "".join([str(i) for i in temp2])
		temp1[-1] = temp2
		self.equate(temp, temp1)

		temp = self.input[linenumber+1:]
		temp1 = []
		for x in temp:
			if x.count("\t") == self.condition+1 and len(x) != 1:
				temp1.append(x)
			else:
				break
		temp = temp1

		self.condition += 1
		self.trial[self.condition] = self.condition

		while (self.conditional(thisisvariablenumber1[1].lstrip().split(" "), 2) == True):
			self.iterate(thisisvariablenumber1[2])
			self.check(temp)	

	def iterate(self, thisisvariablenumber1):
		temp1 = thisisvariablenumber1.lstrip()
		temp1 = temp1.split(" ")

		temp2 = temp1[-1:]
		temp1 = temp1[:-1]
		temp1 = " ".join([str(i) for i in temp1])

		if temp2 == ["++"]:
			self.variables[temp1] += 1

		elif temp2 == ["--"]:
			self.variables[temp1] -= 1

	def do_whiler(self, linenumber):
		temp = self.input[linenumber+1:]

		print linenumber


x = algorithm()
x.set_input("""
|z = 9|;
|y = 9|;
|a = <z * y * 0>|;
if ((z == 7) and (y == 7))
	|w = 8|;
elif (z == 8)
	if (y == 8)
		|w = 50|;
	else
		if (a == 0)
			|x = 7|;
		|w = 100|;
else
	|w = 5000|;
	|b = <w / 500 * 10>;

|c = 0|;

for (|x = 0|; (x < 10); x ++)
	|c += 1|;
""")