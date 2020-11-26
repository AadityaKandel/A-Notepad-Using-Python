from tkinter import *
import tkinter.messagebox as tmsg
import time
ak_root = Tk()

ak_root.geometry("500x500")
tmsg.showinfo('Start','Notepad By Aaditya Kandel')
ak_root.title(f"Untitled 1.txt")
def about():
    tmsg.showinfo('About','Notepad By Aaditya Kandel')
def contact():
	tmsg.showinfo('Contact','Contact:\n\nE-mail: kandelaaditya11@gmail.com')
def save():
	ak_root.title(f"{(nameen.get())}{(ex.get())}")
	with open(f"{(nameen.get())}{(ex.get())}","w") as f:
		f.write(f"{(text1.get(1.0, END))}")
		print(text1)
	tmsg.showinfo('Save',f'File {(nameen.get())}{(ex.get())} is saved Successfully..')
def exit():
	a = tmsg.askquestion('Exit','Do You Really Want To Exit ?')
	if(a == "yes"):
		sys.exit()
	else:
		a = tmsg.showinfo('Exit','Okay')


mainmenu = Menu(ak_root)
m1 = Menu(mainmenu,tearoff = 0)
m1.add_command(label = "Save",command = save)
m1.add_command(label = "Exit",command = exit)

m2 = Menu(mainmenu,tearoff = 0)
m2.add_command(label = "About",command = about)
m2.add_command(label = "Contact",command = contact)

ak_root.config(menu = mainmenu)
mainmenu.add_cascade(label = "File",menu = m1)
mainmenu.add_cascade(label = "Help",menu = m2)
s = Scrollbar(ak_root)
s.pack(fill = "y", side = "right")

f1 = Frame(bg = "black")
Label(f1,text = "Name of File: ").pack(side = LEFT)


nameen = StringVar()
nameen.set("Untitled 1")
Entry(f1,textvariable = nameen).pack(side = LEFT)
f1.pack()



ex = StringVar()
ex.set('.txt')
Entry(f1,textvariable = ex).pack(side = RIGHT)
Label(f1,text = "           Extension: ").pack(side = RIGHT)
f1.pack()

textvar = StringVar()
text1 = Text(ak_root,yscrollcommand =s.set,font = "comicsansms 20 italic")
text1.pack(fill = BOTH)
s.config(command = text1.yview)

ak_root.mainloop()
