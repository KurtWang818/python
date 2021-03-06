#!/usr/bin/python

from Tkinter import *
import tkMessageBox
import sys 
import os
import pandas as pd
import csv
from collections import defaultdict
# from PIL import ImageTk, Image

path = os.path.split(os.path.realpath(sys.argv[0]))[0]

def analyze():
	radioValue = analysis.get()
	if radioValue == "analysis_1":
		carrier = parameter1.get()
		# tkMessageBox.showinfo('Message', "You chose, %s" % carrier)
		os.system("python " + path + "/analysis_1.py " + carrier)
		window = Toplevel(app)
		window.title("Result for analysis_1, total number of flights for carriers")
		window.config(height = '600', width = '600')
		carrier = pd.read_csv(path + '/results/analysis1.csv', sep=",", usecols = ["Carrier", "Count"])
		noti = Label(window, text = carrier)
		noti.grid(row = 0, column = 0, sticky="nsew", padx=1, pady=1)
		# img1 = PhotoImage(file = (path + "/pythonFinalscreen/image1.gif"))
		# img1 = img1.zoom(5)
		# panel1 = Label(window, image = img1)
		# panel1.image = img1
		# panel1.pack()
		# img2 = ImageTk.PhotoImage(Image.open(path + "/pythonFinalscreen/image2.png"))
		# panel2 = Label(window, image = img2)
		# panel2.pack()
	elif radioValue == "analysis_2":
		city = parameter1.get()
		# tkMessageBox.showinfo('Message', "You chose, %s" % radioValue % city)
		os.system("python " + path + "/analysis_2.py " + city)
		window = Toplevel(app)
		window.title("Result for analysis_2, top origin city, destination city, and route")
		window.config(height = '600', width = '600', bg = "lightblue")
		city = pd.read_csv(path + '/results/analysis2.csv', sep=",", usecols = ["Origin", "Count"])
		noti = Label(window, text = city)
		noti.grid(row = 0, column = 0, sticky="nsew", padx=1, pady=1)
	elif radioValue == "analysis_3":
		month = parameter1.get()
		day = parameter2.get()
		# tkMessageBox.showinfo('Message', "You chose, %s" % radioValue % month % day)
		os.system("python " + path + "/analysis_3.py " + month + " " + day)
		window = Toplevel(app)
		window.title("Result for analysis_3, total flights by month and day")
		window.config(height = '600', width = '600', bg = "lightblue")
		time = pd.read_csv(path + '/results/analysis3.csv', sep=",", usecols = ["Month", "Count"])
		noti = Label(window, text = time)
		noti.grid(row = 0, column = 0, sticky="nsew", padx=1, pady=1)
	elif radioValue == "analysis_4":
		month = parameter1.get()
		carrier = parameter2.get()
		# tkMessageBox.showinfo('Message', "You chose, %s" % radioValue % month % carrier)
		os.system("python " + path + "/analysis_4.py " + month + " " + carrier)
		window = Toplevel(app)
		window.title("Result for analysis_4, departure, arrival, and carrier delay percentage")
		window.config(height = '600', width = '600', bg = "lightblue")
		info = pd.read_csv(path + '/results/analysis4.csv', sep=",", usecols = ["Month", "Count"])
		noti = Label(window, text = info)
		noti.grid(row = 0, column = 0, sticky="nsew", padx=1, pady=1)
	elif radioValue == "analysis_5":
		carrier = parameter1.get()
		# tkMessageBox.showinfo('Message', "You chose, %s" % radioValue % carrier)
		os.system("python " + path + "/analysis_5.py " + carrier)
		window = Toplevel(app)
		window.title("Result for analysis_5, top cities for carrier")
		window.config(height = '600', width = '600', bg = "lightblue")
		time = pd.read_csv(path + '/results/analysis5.csv', sep=",", usecols = ["City", "Count"])
		noti = Label(window, text = time)
		noti.grid(row = 0, column = 0, sticky="nsew", padx=1, pady=1)

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

def record1():
	os.system("python " + path + "/speak.py ")
	file = open(path + "/results/recordResult.txt", 'r')
	yourParameter1.delete(0,END)
	yourParameter1.insert(0, file.read())

def record2():
	os.system("python " + path + "/speak.py ")
	file = open(path + "/results/recordResult.txt", 'r')
	yourParameter2.delete(0,END)
	yourParameter2.insert(0, file.read())

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

button1 = Button(app, text = "Start recording", width = 20, command = record1)
button1.pack(padx = 5, pady = 5)

parameter1 = StringVar(None)
yourParameter1 = Entry(app, textvariable = parameter1)
yourParameter1.pack()

text2 = StringVar()
text2.set("parameter 2: ")
label3 = Label(app, textvariable = text1, height = 4)
label3.configure(background='lightblue')
label3.pack()

button2 = Button(app, text = "Start recording", width = 20, command = record2)
button2.pack(padx = 5, pady = 5)

parameter2 = StringVar(None)
yourParameter2 = Entry(app, textvariable = parameter2)
yourParameter2.pack()

button3 = Button(app, text = "Submit", width = 20, command = analyze)
button3.pack(side = 'bottom', padx = 5, pady = 5)

app.mainloop()
