datatypes = ["boolean", "char", "int", "long", "float", "double"]

class algorithm():
	def __init__(self):
		self.input = ""
		self.variables = {}
		self.condition = 0	#Determines how deep the code is at
		self.trial = {}
		self.functions = {}

	def set_input(self, temp):
		self.input = temp
		self.input = self.input.split("\n")
		self.check()

	def check(self, b=None, c=None):
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

			elif "|" in temp1[0] and "|" in temp1[-1]:	#if line is assignment, assign
				temp1 = self.remove_pipe(temp1)
				temp1 = self.split_equals(temp1)
				temp1 = self.remove_greater(temp1)
	
				if c == None:
					self.equate(temp1[0], temp1[2:])
				else:
					self.equate(temp1[0], temp1[2:], c)

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
				if b != None:
					self.forer(temp1, a, b)
				else:
					self.forer(temp1, a, self.input)

			elif temp1[0] == "do" and len(temp1) == 1:
				if b != None:
					self.do_whiler(a, b)
				else:
					self.do_whiler(a, self.input)

			elif temp1[0] in datatypes:
				self.function_declare(temp1, a)

			elif temp1[0] in self.functions:
				temp1.remove("(")
				temp1.pop()
				temp2 = temp1[1:]
				temp2 = "".join([str(i) for i in temp2])
				temp2 = temp2.split(",")
				self.run_function(temp1[0], temp2)

			a += 1

	def remove_pipe(self, thisisvariablenumber1):	#input is list
		if thisisvariablenumber1[0] == "|":
			thisisvariablenumber1.pop(0)
		else:
			thisisvariablenumber1[0] = thisisvariablenumber1[0].split("|")
			thisisvariablenumber1[0] = "".join([str(i) for i in thisisvariablenumber1[0][1:]])

		if thisisvariablenumber1[-1] == "|":
			thisisvariablenumber1.pop(-1)
		else:
			
			thisisvariablenumber1[-1] = thisisvariablenumber1[-1].split("|")
			if len(thisisvariablenumber1) != 1:
				thisisvariablenumber1[-1] = "".join([str(i) for i in thisisvariablenumber1[-1][:-1]])
			else:
				return thisisvariablenumber1[0]

		return thisisvariablenumber1

	def split_equals(self, thisisvariablenumber1):
		for x in range(len(thisisvariablenumber1)):
			if "=" in thisisvariablenumber1[x] and len(thisisvariablenumber1[x]) != 1:
				thisisvariablenumber1[x] = thisisvariablenumber1[x].split("=")
				temp1 = thisisvariablenumber1[x]

				if "+" in temp1[0] or "-" in temp1[0] or "*" in temp1[0] or "/" in temp1[0] or "%" in temp1[0]:
					if len(list(temp1[0])) == 1:
						thisisvariablenumber1.insert(x, "=")
						thisisvariablenumber1.insert(x+1, thisisvariablenumber1[0])
						thisisvariablenumber1.insert(x+2, temp1[0])
						thisisvariablenumber1.insert(x+3, temp1[1])
						thisisvariablenumber1.pop(x+4)
					else:
						
						temp2 = list(temp1[0])
						temp3 = temp2[-1]
						temp2 = "".join([str(i) for i in temp2[:-1]])
						temp4 = []
						temp4.append(temp2)
						temp4.append("=")
						temp4.append(temp2)
						temp4.append(temp3)
						temp5 = thisisvariablenumber1[1:]
						temp5.insert(0,list(temp1)[1])
						for x in temp5:
							temp4.append(x)

						thisisvariablenumber1 = temp4
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
		else:
			thisisvariablenumber1[2:] = "".join([str(i) for i in thisisvariablenumber1[2:]])
			try:
				thisisvariablenumber1.remove("<")
				thisisvariablenumber1[2:] = "".join([str(i) for i in thisisvariablenumber1[2:]])
			except:
				pass

		return thisisvariablenumber1

	def equate(self, thisisvariablenumber1, thisisvariablenumber2, extra=None):
		thisisvariablenumber2 = list(thisisvariablenumber2)
		try:
			self.variables[thisisvariablenumber1] = eval("".join([str(i) for i in thisisvariablenumber2]))

		except:
			for x in range(len(thisisvariablenumber2)):
				if extra != None and thisisvariablenumber2[x] in extra:
					thisisvariablenumber2[x] = extra[thisisvariablenumber2[x]] 
				elif thisisvariablenumber2[x] in self.variables:
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

	def forer(self, thisisvariablenumber1, linenumber, lines):
		temp1 = self.remove_pipe(list(thisisvariablenumber1[0].replace(" ", "")))
		temp1 = self.split_equals(temp1)
		temp1 = self.remove_greater(temp1)
		self.equate(temp1[0], temp1[2:])

		temp = lines[linenumber+1:]
		temp1 = []
		for x in temp:
			if x.count("\t") >= self.condition+1 and len(x) != 1:
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

	def do_whiler(self, linenumber, lines):
		temp = lines[linenumber+1:]
		temp1 = []
		test = ""
		for x in temp:
			if x.count("\t") >= self.condition+1 and len(x) != 1:
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

	def function_declare(self, thisisvariablenumber1, linenumber):
		typer = thisisvariablenumber1[0]
		name = thisisvariablenumber1[1]
		thisisvariablenumber1.pop(2)
		thisisvariablenumber1.pop(-1)
		arguments = " ".join([str(i) for i in thisisvariablenumber1[2:]])
		arguments = arguments.split(",")

		temp = self.input[linenumber+1:]
		temp1 = []
		for x in temp:
			if x.count("\t") == self.condition+1 and len(x) != 1:
				temp1.append(x)
			else:
				break
		temp = temp1
		
		self.functions[name] = [typer, arguments, temp]

	def run_function(self, name, arguments=None):
		temp = self.functions[name]
		if len(temp[1]) != len(arguments):
			print "ERROR. Invalid arguments."
			exit(1)
		else:
			temp1 = {}
			a = 0
			for x in temp[1]:
				temp2 = x.split(" ")
				temp2[1] = " ".join([str(i) for i in temp2[1:]])
				temp3 = temp2[0]
				temp2 = temp2[1]
				temp1[temp2] = arguments[a]
				
				if temp3 == "int":
					temp1[temp2] = int(temp1[temp2])
				elif temp3 == "float":
					temp1[temp2] = float(temp1[temp2])
				elif temp3 == "long":
					temp1[temp2] = long(temp1[temp2])
				elif temp3 == "double":
					#temp1[temp2] = double(temp1[temp2])
					pass
				a += 1

		self.condition += 1

		self.check(temp[2], temp1)

x = algorithm()
x.set_input("""

int adder ( int d ):
	|d+=<100-10>|;

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
	if (z == 9)
		do:
			|c += 1|;
		while (c < 1000);
do:
	|c -= 1|;
while (c > 100);

adder ( 5 );

""")