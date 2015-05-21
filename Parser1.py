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

			elif len(temp1) > 1 and "|" in temp1[0] and "|" in temp1[-1]:	#if line is assignment, assign
				temp1 = self.remove_pipe(temp1)
				temp1 = self.split_equals(temp1)
				temp1 = self.remove_greater(temp1)
	
				self.equate(temp1[0], temp1[2:])

			elif (temp1[0] == "if" or (temp1[0] == "elif" and self.trial[self.condition] == -1)) and "(" in temp1[1]:	#if line is if
				self.conditional(temp1[1:])

			elif temp1[0] == "els" and len(temp1) == 1 and self.trial[self.condition] == -1:
				self.conditional([1])

			elif temp1[0] == "break" and len(temp1) == 1:	#break
				self.condition -= 1		

			elif temp1[0] == "for" and "(" in temp1[1]:	#for loop
				temp1[1] = list(temp1[1])
				temp1[1].remove("(")
				temp1[1] = "".join([str(i) for i in temp1[1]])

				temp1 = " ".join([str(i) for i in temp1[1:]])
				temp1 = temp1.split(";")
				self.forer(temp1, a)

			elif temp1[0] == "do" and len(temp1) == 1:
				self.do_whiler(a)

			a += 1

	def remove_pipe(self, thisisvariablenumber1):	#input is list
		if len(thisisvariablenumber1[0]) == 1:
			thisisvariablenumber1.pop(0)
		else:
			thisisvariablenumber1[0] = thisisvariablenumber1[0].split("|")
			thisisvariablenumber1[0] = "".join([str(i) for i in thisisvariablenumber1[0][1:]])

		if len(thisisvariablenumber1[-1]) == 1:
			thisisvariablenumber1.pop(-1)
		else:
			thisisvariablenumber1[-1] = thisisvariablenumber1[-1].split("|")
			thisisvariablenumber1[-1] = "".join([str(i) for i in thisisvariablenumber1[-1][:-1]])

		return thisisvariablenumber1

	def split_equals(self, thisisvariablenumber1):
		for x in range(len(thisisvariablenumber1)):
			if "=" in thisisvariablenumber1[x] and len(thisisvariablenumber1[x]) != 1:
				thisisvariablenumber1[x] = thisisvariablenumber1[x].split("=")
				temp1 = thisisvariablenumber1[x]

				if temp1[0] in ["+", "-", "*", "%", "/"]:
					thisisvariablenumber1.insert(x, "=")
					thisisvariablenumber1.insert(x+1, thisisvariablenumber1[0])
					thisisvariablenumber1.insert(x+2, temp1[0])
					thisisvariablenumber1.pop(x+3)
					break

				thisisvariablenumber1.insert(x, temp1[0])
				thisisvariablenumber1.insert(x+1, "=")
				thisisvariablenumber1.insert(x+2, temp1[1])
				thisisvariablenumber1.pop(x+3)
				break
		
		return thisisvariablenumber1


	def remove_greater(self, thisisvariablenumber1):
		if len(thisisvariablenumber1[-1]) == 1 and ">" in thisisvariablenumber1[-1]:
			thisisvariablenumber1.pop(-1)
		elif ">" in thisisvariablenumber1[-1]:
			thisisvariablenumber1[-1] = thisisvariablenumber1[-1].split(">")
			thisisvariablenumber1[-1] = "".join([str(i) for i in thisisvariablenumber1[-1][:-1]])

		if len(thisisvariablenumber1[2:][0]) == 1 and "<" in thisisvariablenumber1[2:][0]:
			thisisvariablenumber1.remove("<")
		elif "<" in thisisvariablenumber1[2:][0]:
			thisisvariablenumber1[2] = thisisvariablenumber1[2].split("<")
			thisisvariablenumber1[2] = "".join([str(i) for i in thisisvariablenumber1[2]])

		return thisisvariablenumber1


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
		try:
			temp = eval(" ".join([str(i) for i in thisisvariablenumber1]))
		except:
			temp = eval("".join([str(i) for i in thisisvariablenumber1]))

		if temp == True and thisisvariablenumber2 == 0:
			self.trial[self.condition] = self.condition
			self.condition += 1
		elif temp == True and thisisvariablenumber2 == 1:
			return self.condition
		elif temp == True and thisisvariablenumber2 == 2:
			return True
		else:
			self.trial[self.condition] = -1

	def forer(self, thisisvariablenumber1, linenumber):
		temp1 = self.remove_pipe(list(thisisvariablenumber1[0].replace(" ", "")))
		temp1 = self.split_equals(temp1)
		temp1 = self.remove_greater(temp1)
		self.equate(temp1[0], temp1[2:])

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
			self.check(temp)
			self.iterate(thisisvariablenumber1[2])

		self.condition -= 1

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
		temp1 = []
		test = ""
		for x in temp:
			if x.count("\t") == self.condition+1 and len(x) != 1:
				temp1.append(x)
			else:
				test = x
				break

		temp = temp1
		self.condition += 1
		self.trial[self.condition] = self.condition
		self.check(temp)
		test = test.split(" ")
		test[-1] = list(test[-1])[:-1]
		test[-1] = "".join([str(i) for i in test[-1]])
		test = test[1:]
		test = " ".join([str(i) for i in test])

		while(self.conditional(test, 2) == True):
			self.check(temp)

		self.condition -= 1


x = algorithm()
x.set_input("""

|z = 9|;
|y = 9|;
|a = <z * y * 0>|;
if ( (z == 7) and (y == 7) )
	|w = 8|;
elif ( z == 8 )
	if (y == 8)
		|w = 50|;
	else
		if (a == 0)
			|x = 7|;
		|w = 100|;
else
	|w = 5000|;
	|b = <w / 500 * 10>|;


| c=<0 + 100> |;

for (|x = 0|; (x < 10); x ++)
	|c += 1|;

do:
	|c -= 1|;
while (c > 100);

""")