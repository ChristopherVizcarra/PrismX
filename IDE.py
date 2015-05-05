from Tkinter import *
import tkFileDialog

class GUI():
	def __init__(self):
		self.root = Tk()
		self.root.geometry("800x600")

		self.createWidgets()

		self.root.mainloop()

	def createWidgets(self):
		menubar = Menu(self.root)

		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="Open", command=self.open)
		filemenu.add_command(label="Save", command=self.save)
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=self.exit)
		menubar.add_cascade(label="File", menu=filemenu)

		self.root.config(menu = menubar)

		self.text = Text(self.root)
		self.text.pack(side=LEFT, fill=BOTH, expand=YES)

		scroll = Scrollbar(self.root, orient=VERTICAL, command=self.text.yview)
		scroll.pack(side=RIGHT, fill=Y)

		self.text["yscrollcommand"] = scroll.set

	def exit(self):
		self.root.quit()

	def open(self):
		try:
			name = tkFileDialog.askopenfilename()

			f = open(name, "r")
			temp = f.read()
			f.close()

			self.text.delete(1.0, END)
			self.text.insert(INSERT, temp)

			self.root.title(name)
		except:
			pass

	def save(self):
		try:
			name = tkFileDialog.asksaveasfilename()

			f = open(name, "w")
			f.write(self.text.get(1.0, END))
			f.close()

			self.root.title(name)
		except:
			pass

GUI()