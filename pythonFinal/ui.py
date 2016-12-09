#!/usr/bin/python

from Tkinter import *
import tkMessageBox
import sys 
import os

path = os.path.split(os.path.realpath(sys.argv[0]))[0]

def analyze():
	radioValue = analysis.get()
	if radioValue == "analysis_1":
		carrier = parameter1.get()
		# tkMessageBox.showinfo('Message', "You chose, %s" % carrier)
		os.system("python " + path + "/analysis_1.py " + carrier)
	elif radioValue == "analysis_2":
		city = parameter1.get()
		# tkMessageBox.showinfo('Message', "You chose, %s" % radioValue % city)
		os.system("python " + path + "/analysis_2.py " + city)
	elif radioValue == "analysis_3":
		month = parameter1.get()
		day = parameter2.get()
		# tkMessageBox.showinfo('Message', "You chose, %s" % radioValue % month % day)
		os.system("python " + path + "/analysis_3.py " + month + " " + day)
	elif radioValue == "analysis_4":
		month = parameter1.get()
		carrier = parameter2.get()
		# tkMessageBox.showinfo('Message', "You chose, %s" % radioValue % month % carrier)
		os.system("python " + path + "/analysis_4.py " + month + " " + carrier)
	elif radioValue == "analysis_5":
		carrier.parameter1.get()
		# tkMessageBox.showinfo('Message', "You chose, %s" % radioValue % carrier)
		os.system("python " + path + "/analysis_5.py " + carrier)

def insert1():
	yourParameter1.delete(0,END)
	yourParameter2.delete(0,END)
	yourParameter1.insert(0, 'AA')

def insert2():
	yourParameter1.delete(0,END)
	yourParameter2.delete(0,END)
	yourParameter1.insert(0, "ATL")

def insert3():
	yourParameter1.delete(0,END)
	yourParameter2.delete(0,END)
	yourParameter1.insert(0, "1")
	yourParameter2.insert(0, "1")

def insert4():
	yourParameter1.delete(0,END)
	yourParameter2.delete(0,END)
	yourParameter1.insert(0, "1")
	yourParameter2.insert(0, "AA")

def insert5():
	yourParameter1.delete(0,END)
	yourParameter2.delete(0,END)
	yourParameter1.insert(0, "AA")

app = Tk()
app.title("Flight Information")
app.geometry('600x600+500+500')
app.configure(background='lightblue')

labelText = StringVar()
labelText.set("Please choose the information to analyze and input the parameter")
label1 = Label(app, textvariable = labelText, height = 4)
label1.configure(background='lightblue')
label1.pack()

analysis = StringVar()
analysis.set(None)
radio1 = Radiobutton(app, text = "Flights by carrier (Please input code for carrier)", value = "analysis_1", variable = analysis, command = insert1)
radio2 = Radiobutton(app, text = "Flights by city (Please inout code for city)", value = "analysis_2", variable = analysis, command = insert2)
radio3 = Radiobutton(app, text = "Flights by month and day of week (Please inout numeric value for month and day of week)", value = "analysis_3", variable = analysis, command = insert3)
radio4 = Radiobutton(app, text = "Delayed flights by month and carrier (Please input numeric value for month and code for carrier)", value = "analysis_4", variable = analysis, command = insert4)
radio5 = Radiobutton(app, text = "Top cities by carrier (Please input code for carrier)", value = "analysis_5", variable = analysis, command = insert5)
radio1.configure(background='lightblue')
radio2.configure(background='lightblue')
radio3.configure(background='lightblue')
radio4.configure(background='lightblue')
radio5.configure(background='lightblue')
radio1.pack()
radio2.pack()
radio3.pack()
radio4.pack()
radio5.pack()

text1 = StringVar()
text1.set("parameter 1: ")
label2 = Label(app, textvariable = text1, height = 4)
label2.configure(background='lightblue')
label2.pack()

parameter1 = StringVar(None)
yourParameter1 = Entry(app, textvariable = parameter1)
yourParameter1.pack()

text2 = StringVar()
text2.set("parameter 2: ")
label3 = Label(app, textvariable = text1, height = 4)
label3.configure(background='lightblue')
label3.pack()

parameter2 = StringVar(None)
yourParameter2 = Entry(app, textvariable = parameter2)
yourParameter2.pack()

button = Button(app, text = "Submit", width = 20, command = analyze)
button.pack(side = 'bottom', padx = 15, pady = 15)

app.mainloop()
