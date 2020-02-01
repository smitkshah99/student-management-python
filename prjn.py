


from tkinter import *

from tkinter import messagebox

from tkinter import scrolledtext

global entqote

global text

import numpy as np 

import matplotlib.pyplot as plt

global student_list 

global mark_list  

global list1



root = Tk()

root.title("Student Management System")

root.geometry("500x700+450+50")

def f1():

	root.withdraw()

	addst.deiconify()

def f2():

	addst.withdraw()

	root.deiconify()

def f3():

  

	root.withdraw()

	viewst.deiconify()

	global list1

	import cx_Oracle

	con = None

	cursor = None

	try:

		con = cx_Oracle.connect("system/abc123")

		cursor = con.cursor()

		sql = "select * from student"

		cursor.execute(sql)

		list1 = cursor.fetchall()

		stData.delete("1.0",END)

		msg = ""

		for rno,name,marks in list1:

			#msg = msg + "r: " +str(d[0]) +" n: "+ d[1] + "\n"

			name = "Roll_no" + " " + str(rno)+" " + "Name" + " " + name + " " + "Marks" + " " + str(marks) + "\n"

			stData.insert(END,name)

	   

	

		

	except cx_Oracle.DatabaseError as e:

		print("some issue " ,e)

	finally:

		

		if cursor is not None:

			cursor.close()

		if con is not None:

			con.close()

		



def f4():

	viewst.withdraw()

	root.deiconify()

def f5():

	import cx_Oracle

	con = None

	cursor = None



	try:

		con = cx_Oracle.connect("system/abc123")

		try:

			rno = int(entRno.get())

			

			if rno <0:

				msg= "enter positive roll no"

				messagebox.showerror("Error",msg);

				entRno.delete(0,END)

				entRno.focus()

				return;

			if rno ==0:

				msg = "enter correct roll no"

				messagebox.showerror("Error",msg)

				entRno.delete(0,END)

				entRno.focus()

				return;

			if rno == "":

				msg ="Roll no field should be blank"

				messagebox.showerror("Error",msg)

				entRno.delete(0,END)

				entRno.focus()

				return;



		except ValueError as e:

			msg = "enter integer only for rollno"

			messagebox.showerror("Error Window",msg)

			entRno.delete(0,END)

			entRno.focus()

			return

		try:



			name = entName.get()

			if name == "":

				msg = "Enter name(Mandatory)";

				messagebox.showerror('Error window',msg)

				entName.delete(0,END)

				entName.focus()

				return

			if name.isdigit():

				msg = "Name cannot be integer"

				messagebox.showerror("Error window",msg)

				entName.delete(0,END)

				entName.focus()

				return

			if not(name.isalpha()):

				msg = "Enter name(alphabets only)"

				messagebox.showerror("Error window",msg)

				entName.delete(0,END)

				entName.focus()

				return

			if len(name)<2:





				msg = "Name cannot be less than 2 letters"

				messagebox.showerror("Error window",msg)

				entName.delete(0,END)

				entName.focus()

				return

		except ValueError as e:

			msg = "enter proper name"

			messagebox.showerror("Error Window",msg)

			entName.delete(0,END)

			entName.focus()

			return

		try:

			marks = int(entaMarks.get())

			if marks < 0:



				msg = "Marks cannot be negative"

				messagebox.showerror("Error window",msg)

				entaMarks.delete(0,END)

				entaMarks.focus()

				return

			if marks == 0 or marks >100:

				msg = "Enter correct marks"

				messagebox.showerror("Error window",msg)

				entaMarks.delete(0,END)

				entaMarks.focus()

				return

			if marks == "":

				msg  = "enter valid marks(mandatory)";

				messagebox.showerror("Error window",msg)

				entaMarks.delete(0,END)

				entaMarks.focus()

				return

		except ValueError as e:

			msg = "enter integer only for marks"

			messagebox.showerror("Error Window",msg)

			entaMarks.delete(0,END)

			entaMarks.focus()

			return

		cursor = con.cursor()

		sql = "insert into student values('%d','%s','%d')"

		args = (rno,name,marks)

		

		

		

		

		

		

		

		

		



		cursor.execute(sql % args)

		msg = "record added successfully"

		messagebox.showinfo("Message",msg)

		con.commit()

		entRno.delete(0,END)

		entName.delete(0,END)

		entaMarks.delete(0,END)

		entRno.focus()

		msg = str(cursor.rowcount) + "records inserted "

		

	except cx_Oracle.DatabaseError as e:

		messagebox.showerror("Error window" ,e)

		con.rollback()



	finally:

		if cursor is not None:

			cursor.close()

		if con is not None:

			con.close()



def f6():

	

		root.withdraw()

		updatest.deiconify()

def f7():

	import cx_Oracle

	cursor = None

	con = None

	try:

		con = cx_Oracle.connect("system/abc123")

		try:

			rno = int(entrollno.get())

			if rno <0:

				msg= "enter positive roll no"

				messagebox.showerror("Error",msg);

				entrollno.delete(0,END)

				return

			if rno ==0:

				msg = "enter correct roll no"

				messagebox.showerror("Error",msg)

				entrollno.delete(0,END)

				return

			if rno == "":

				msg ="Roll no field should be blank"

				messagebox.showerror("Error",msg)

				entrollno.delete(0,END)

				return

				

		except ValueError as e:

				msg = "Enter integer only for rollno"

				messagebox.showerror("Error window",msg)

				entrollno.delete(0,END)

				entrollno.focus()

				return

		try:



			name = entname.get()

			if name.isdigit():

				msg = "Name cannot be integer"

				messagebox.showerror("Error window",msg)

				entname.delete(0,END)

				entname.focus()

				return

			if len(name) == 0:

				msg = "enter name"

				messagebox.showerror("Error Window",msg)

				entname.delete(0,END)

					

				entname.focus()

				return

			if not(name.isalpha()):

				msg = "Enter name(alphabets only)"

				messagebox.showerror("Error window",msg)

				entname.delete(0,END)

				entname.focus()

				return

			if len(name)<2:

				msg = "Name cannot be less than 2 letters"

				messagebox.showerror("Error window",msg)

				entname.delete(0,END)

				entname.focus()

				return

		except ValueError as e:

				msg = "Enter name correctly"

				messagebox.showerror("Error Window",msg)

				entname.delete(0,END)

				entname.focus()

				return

		try:

			marks = int(entmarks.get())

			if marks < 0:

				msg = "Marks cannot be negative"

				messagebox.showerror("Error window",msg)

				entmarks.delete(0,END)

				entmarks.focus()

				return

			if marks == 0 or marks >100:

				msg = "Enter correct marks"

				messagebox.showerror("Error window",msg)

				entmarks.delete(0,END)

				entmarks.focus()

				return

		except ValueError as e:

				msg  = "Enter integer only for marks"

				messagebox.showerror("Error window",msg)

				entmarks.delete(0,END)

				entmarks.focus()

				return

		cursor = con.cursor()

		sql = "update student set name = '%s',marks = '%d' where rno ='%d'"

		args = (name,marks,rno)

		cursor.execute(sql % args)

		c = cursor.rowcount

		if c==0:

			msg = "record does not exists"

			messagebox.showerror("Error Window",msg)

			entrollno.delete(0,END)

			entname.delete(0,END)

			entmarks.delete(0,END)

			entrollno.focus()

			return

		else:

			msg = "record updated successfully"

			messagebox.showinfo("Message",msg)

			con.commit()

			#msg = str(cursor.rowcount) + "records inserted "

			entrollno.delete(0,END)

			entname.delete(0,END)

			entmarks.delete(0,END)

			entrollno.focus()

			

	except cx_Oracle.DatabaseError as e:

		messagebox.showerror("Error window" ,e)

		con.rollback()

	finally:

		if cursor is not None:

			cursor.close()

		if con is not None:

			con.close()

def f8():

	updatest.withdraw()

	root.deiconify()

def f9():

	import cx_Oracle

	cursor = None

	con = None

	try:

		con = cx_Oracle.connect("system/abc123")

		cursor = con.cursor()

		try:

			rno = int(entdrno.get())

			if rno <0:

				msg= "enter positive roll no"

				messagebox.showerror("Error",msg);

				entdrno.delete(0,END)

				entdrno.focus()

				return

			if rno ==0:

				msg = "enter correct roll no"

				messagebox.showerror("Error",msg)

				entdrno.delete(0,END)

				entdrno.focus()

				return

			if rno == "":

				msg ="Roll no field should not be blank"

				messagebox.showerror("Error",msg)

				entdrno.delete(0,END)

				entdrno.focus()

				return

		except ValueError as e:

			msg = "Enter integer only"

			messagebox.showerror("Error Window",msg)

			entdrno.delete(0,END)

			entdrno.focus()

			return

		sql = "delete from student where rno = '%d'"

		args = (rno)

		cursor.execute(sql % args)

		c = cursor.rowcount

		#print(c)

		

		if  c==0:

			msg = "Record does not exists"

			messagebox.showerror("Error Window",msg)

			entdrno.delete(0,END)

			entdrno.focus()

			return

		else:

			

			msg = "record deleted successfully"

			messagebox.showinfo("Message",msg)

			con.commit()

			entdrno.delete(0,END)

			entdrno.focus()



	except cx_Oracle.DatabaseError as e:

		messagebox.showerror("Error window", e)

		con.rollback()  

	finally:

		if cursor is not None:

			cursor.close()

		if con is not None:

			con.close()

		

def f10():

		root.withdraw()

		deletest.deiconify()

def f11():

	deletest.withdraw()

	root.deiconify()

def f12():

#function to display graph window

		root.withdraw()

		graphst.deiconify()

def f13():

#function to exit from graph window

	graphst.withdraw()

	root.deiconify()

def f14():

	

#function to display graph 

	import cx_Oracle

	student_list = []

	mark_list = []

	con = None

	cursor = None

	try:

		con = cx_Oracle.connect("system/abc123")

		cursor = con.cursor()

		sql = "select * from student where rownum<6"

		cursor.execute(sql)

		list1 = cursor.fetchall()

		for rno,name,marks in list1:

			student_list.append(name)

			mark_list.append(marks)

				

		x = np.arange(len(student_list))

		plt.title("Students performance graph",fontsize=30)

		plt.bar(x,mark_list,width = 0.25,label = 'mark_list',color='r',alpha = 0.5)

		plt.xticks(x,student_list,fontsize=10,rotation = 30)

		   

		plt.xlabel('Students',fontsize=20)

		plt.ylabel('Marks',fontsize=20)

		#plt.legend()

		plt.grid()

		plt.show()



	except cx_Oracle.DatabaseError as e:

		print("Some issues" ,e)

	finally:

		if cursor is not None:

			cursor.close()

		if con is not None:

			con.close()



def hack():

	import cx_Oracle

	student_list = []

	mark_list = []

	con = None

	cursor = None

	try:

		con = cx_Oracle.connect("system/abc123")

		cursor = con.cursor()

		sql = "select * from student where rownum<6"

		cursor.execute(sql)

		list1 = cursor.fetchall()

		for rno,name,marks in list1:

			student_list.append(name)

			mark_list.append(marks)

				

		x = np.arange(len(student_list))

		plt.title("Students performance graph")

		plt.bar(x,mark_list,width = 0.25,label = 'mark_list',color='r',alpha = 0.5)

		plt.xticks(x,student_list,fontsize=10,rotation = 30)

		   

		plt.xlabel('Students',fontsize=10)

		plt.ylabel('Marks',fontsize=30)

		#plt.legend()

		plt.grid()

		#plt.show()

		plt.savefig('Student_Performance.pdf')

		#plt.savefig('Student_Performance.jpg')

		msg = "Graph saved successfully"

		messagebox.showinfo("Info Window",msg)

	except cx_Oracle.DatabaseError as e:

		print("Some issues" ,e)

	finally:

		if cursor is not None:

			cursor.close()

		if con is not None:

			con.close()



def f15():

#function to save graph

	

	try:

		hack()

		

	except OSError as e:

		pass	

def f16():

#function to display quote

	

	import bs4

	import requests



	res = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")

	#print(res)

	



	soup = bs4.BeautifulSoup(res.text,'lxml')

	quote = soup.find('img',{"class":"p-qotd"})



	#print(quote)



	text = quote['alt']

	#entqote.set(text)	

	#print(text)

	entqote.insert(END,text)

	

	pic = "https://www.brainyquote.com" + quote['data-img-url']

	res = requests.get(pic)

	#print(res)

	import datetime

	date = datetime.datetime.now().date()

	fn = str(date)+ ".jpg"

	with open(fn,"wb")as f:

		f.write(res.content)


		f.close()

def f17():

#function to show temperature of mumbai

	import socket

	import requests



	try:

		

		

		

		c = 'mumbai'

		socket.create_connection(("www.google.com",80))

		a1 = "https://api.openweathermap.org/data/2.5/weather?units=metric"

		a2 = "&q=" + c

		a3 = "&appid=c6e315d09197cec231495138183954bd"

		api_address = a1+a2+a3

		res1 = requests.get(api_address)

		#print(res1)

		data = res1.json()

		#print(data)

		main = data['main']

				#print(main)

		temp = main['temp']

		enttemp.insert(END,temp)

		#print("city = ",c,"temp = ",temp)

			

	except OSError:

		

		print("not connected")

def f18():

	#function to close application

	sys.exit()

btnAdd = Button(root,text = "Add",font=("arial",18,"bold"),width = 10,command= f1)

btnView = Button(root,text="View",font = ("arial",18,"bold"),width =10,command = f3)

btnUpdate = Button(root,text="Update",font = ("arial",18,"bold"),width = 10,command = f6)

btnDelete = Button(root,text = "Delete",font= ("arial",18,"bold"),width =10,command = f10)

btnGraph= Button(root,text = "Graph",font = ("arial",18,"bold"),width = 10,command = f12)

#quote of the day

lblqotd = Label(root,text = "Quote",font = ("arial",18,"bold"),width=10)

'''label for quote'''

#lblqoted = Label(root,font =("arial",18,"bold"),width =30)

#entry for qotd



entqote = Text(root,bd=5,font = ("arial",12),height = 5,width = 30)

f16()

entqote.config(state=DISABLED)

'''label for temperature 

lbltempd = Label(root,text = "",font = ("arial",18,"bold"),width = 30)'''

#temperature of mumbai

lbltemp = Label(root,text ="Temperature",font = ("arial",18,"bold"),width=10)

enttemp = Entry(root,bd = 5,font =("arial",18,"bold"),justify = 'center')

f17()

enttemp.config(state=DISABLED)



btnClose = Button(root,text = "Close",font = ("arial",18,"bold"),command = f18,width =10)

btnAdd.pack(pady=10)

btnView.pack(pady=10)

btnUpdate.pack(pady=10)

btnDelete.pack(pady=10)

btnGraph.pack(pady=10)

lblqotd.pack(pady=10)

#lblqoted.pack(pady=10)

entqote.pack(pady=10)

lbltemp.pack(pady=10)

#lbltempd.pack(pady = 10)

enttemp.pack(padx=10)

btnClose.pack(pady =10)

addst = Toplevel(root)

addst.title("Add stduent")

addst.geometry("400x500+450+50")

addst.withdraw()



lblRno = Label(addst,text = "enter rno",font = ("arial",18,"bold"))

entRno = Entry(addst,bd =5,font =("arial",18,"bold"))

lblName = Label(addst,text = "enter name",font=("arial",18,"bold"))

entName = Entry(addst,bd=5,font=("arial",18,"bold"))

lblaMarks = Label(addst,text = "Enter marks",font = ("arial",18,"bold"))

entaMarks = Entry(addst,bd = 5,font =("arial",18,"bold"))



btnAddSave= Button(addst,text = "Save",font = ("arial",18,"bold"),command = f5)

btnAddBack = Button(addst,text = "Back",font = ("arial",18,"bold"),command = f2)

lblRno.pack(pady = 5)

entRno.pack(pady=5)

lblName.pack(pady=5)

entName.pack(pady=5)

lblaMarks.pack(pady=5)

entaMarks.pack(pady=5)

btnAddSave.pack(pady=5)

btnAddBack.pack(pady=5)



viewst = Toplevel(root)

viewst.title("View S")

viewst.geometry("400x500+450+50")

viewst.withdraw()



stData= scrolledtext.ScrolledText(viewst,width=40,height=10)



btnViewBack = Button(viewst,text = "Back",font = ("arial",18,"bold"),command = f4)



stData.pack()

btnViewBack.pack()





#update window

updatest = Toplevel(root)

updatest.title("Update Student")

updatest.geometry("400x500+450+50")

updatest.withdraw()

lblrollno = Label(updatest,text="Enter Roll no",font=("arial",18,"bold"))

entrollno = Entry(updatest,bd = 5,font = ("arial",18,"bold"))

lblname = Label(updatest,text="Enter name",font =("arial",18,"bold"))

entname = Entry(updatest,bd = 5,font = ("arial",18,"bold"))

lblmarks = Label(updatest,text = "Enter marks",font = ("arial",18,"bold"))

entmarks = Entry(updatest,bd=5,font = ("arial",18,"bold"))

btnUpdateInfo = Button(updatest,text = "Update record",font =("arial",18,"bold"),command = f7)

btnUpdateBack = Button(updatest,text = "Back",font = ("arial",18,"bold"),command = f8)

lblrollno.pack(pady=5)

entrollno.pack(pady=5)

lblname.pack(pady=5)

entname.pack(pady=5)

lblmarks.pack(pady=5)

entmarks.pack(pady=5)

btnUpdateInfo.pack(pady=5)

btnUpdateBack.pack(pady=5)



#delete window

deletest = Toplevel(root)

deletest.title("Delete student")

deletest.geometry("400x500+450+50")

deletest.withdraw()

lbldrno = Label(deletest,text = "Enter roll no",font = ("arial",18,"bold"))

entdrno = Entry(deletest,bd = 5,font = ("arial",18,"bold"))

btnDeleteInfo = Button(deletest,text ="Delete record",font = ("arial",18,"bold"),command = f9)

btnDeleteBack = Button(deletest,text = "Back",font=("arial",18,"bold"),command = f11)

lbldrno.pack(pady=5)

entdrno.pack(pady=5)

btnDeleteInfo.pack(pady=5)

btnDeleteBack.pack(pady=5)



#graph window

graphst = Toplevel(root)

graphst.title("Graph:Students")

graphst.geometry("500x500+450+50")

graphst.withdraw()

btnGraphShow = Button(graphst,text = "View Graph",font = ("arial",18,"bold"),command = f14)

btnGraphSave = Button(graphst,text = "Save Graph",font = ("arial",18,"bold"),command = f15)

btnGraphBack = Button(graphst,text = "Back",font = ("arial",18,"bold"),command = f13)





btnGraphShow.pack(pady = 5)

btnGraphSave.pack(pady = 5)

btnGraphBack.pack(pady=5)



root.mainloop()
