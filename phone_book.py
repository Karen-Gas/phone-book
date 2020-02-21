from tkinter import *
import time
import pyttsx3
#import tkinter
root = Tk() # ვქმნით ჩარჩოს
root.config(bg="#E5E8E8") # ჩარჩოს ფერი
root.geometry('300x350')# ზომა
root.title('phone book')# სათაური 

menu = Menu(root) # ვქმნით მენიუ widgets
root.config(menu=menu) 

Tel = Menu(root) 
menu.add_cascade(label='Tel', menu= Tel) 
Tel.add_command(label = 'Add')
#Tel.add_command(label = 'Поиск')

helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label = 'Help')
helpmenu.add_command(label='About') 
#------------------------------------------------

frame = Frame(root,  bg= 'black') # ვქმნით  ფრამმე ვიჯეტს, ''ჩარჩოს გაშავებული ნაწილი''
frame.grid(row=0, sticky = N, column=0, padx=30, pady = 95)


list_box = Listbox(frame, width=35) # ლისტ ბოქსი სადაც დავინახავთ პასუხებს, 
list_box.grid(row=0, column=0, pady = 8, padx = 8)


def voice(words):     # ფუნქცია იღებს ერთ არგუმენტს და ახმოვანებს.
	y =pyttsx3.init()
	y.getProperty('voices')
	
	y.say(words)
	y.runAndWait()
		


def dzebna_func():                            # ტეკსტურ ფაილში ვეძებთ სახელ და გვარს
	my_list = []
	list_box.delete(0,'end') # ყოველ გამოძახებისას ვშლით ლისტბოქსის  მონაცემებს.
	word = ent1.get()
	f = open('C:\\Users\\karen\\Desktop\\r.txt', 'r') # 
	line = f.readline() # ვკითხულობთ სროკებს
	while line:
		line = f.readline() 
		new_word = line.split()
		
		if word in new_word:
			data = list(new_word)# მინაცემებს ვამატებთ ლისტში, იგივე მონაცემები, რომ არ განმეორდეს
			if data in my_list:
				continue
			else:
					
				my_list.append(data)
	for i in range(1, len(my_list)):
				
		list_box.insert(i, my_list[i])
		#line = f.readline()	

	
	if val_C1.get() ==1: # აქ ვამოწმებთ თუ ხმა ჩართულია მაშინ ახმოვანოს,
		for x in range(1, len(my_list)):
			wordss = ' '.join(my_list[x][2])
			voice(wordss)

ent1 = Entry(root,  width=20)  # დასაწერი ადგილი
ent1.grid(row=0, column = 0, sticky = N, pady = 45)

but = Button(root, text = 'dzebna',  command = dzebna_func) # ეს არის ბუთონი რმელიც გამოიძახება ძებნა ფუნქციას
but.grid(row=0, column = 0, sticky = N, pady = 12)

#rbvar = StringVar( )
val_C1 = IntVar() 
C1 = Checkbutton(root, text = 'xma', variable = val_C1, onvalue = 1, offvalue = 0 ) # აქ  val_c1  ვანიჩებთ ან1 ან 0, 1 შემთხვევააში ჩარულია ხმა
#r = Radiobutton(window,width = 19,  value=1, variable=rbvar, indicatoron=0)
C1.grid(row=0, column = 0, sticky = N, pady = 70)



root.mainloop()# უსასრულო ციკი იმისთვის რომ ჩვენი ჩარჩო იყოს ჩართული.