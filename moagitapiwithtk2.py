#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter
from Tkconstants import *

import sys
import commands
import time
import datetime
import requests

# start the tkinter 

tk = Tkinter.Tk()

#### local time 

a = time.ctime()
g = '%s:%s:%s' %(a[3],a[4],a[5])

#### requesting riyadh prayer times from the link 

r = requests.get('http://muslimsalat.com/riyadh.json')
#### uncomment below to get global based on your location


#r = requests.get('http://muslimsalat.com/daily.json')



### getting the data from into a varibal 

p= r.text
 
##### extracting the data 

tfajr=p.find('fajr')
fp0=p.find('am',tfajr)

tl0=p[tfajr:fp0]
# print tl0

tduher=p.find('dhuhr')
fp1=p.find('am',tduher)

tl1=p[tduher:fp1]
# print tl1

tasr=p.find('asr')
fp2=p.find('pm',tasr)

tl2=p[tasr:fp2]
# print tl2

tmaghrib=p.find('maghrib')
fp3=p.find('pm',tmaghrib)

tl3=p[tmaghrib:fp3]
# print tl3


tisha=p.find('isha')
fp4=p.find('pm',tisha)

tl4=p[tisha:fp4]


 
#### starting the GUI "user interface" and inserting the times 
 

tk.title("Moaget Al-Salat")
tk.geometry("800x600")			
frame = Tkinter.Frame(tk, relief=RIDGE, borderwidth=5,width=600, height=1000, bg="black")
frame.config(bg="orange")
frame.pack(fill=BOTH,expand=3)
frame.pack_propagate(3)
label = Tkinter.Label(frame, text="time now", font=("Helvetica", 21))
label.pack(side=TOP,fill=X, expand=3,padx=5, pady=5)
label7= Tkinter.Label(frame, text=a , font=("Helvetica", 18))
label7.pack(side=TOP,fill=X, expand=5,padx=5, pady=5)
label1 = Tkinter.Label(frame, text="time of prayers", font=("Helvetica", 21))
label1.pack(side=TOP,fill=X, expand=3,padx=5, pady=5)
label2= Tkinter.Label(frame, text=tl0, font=("Helvetica", 18))
label2.pack(side=TOP,fill=X, expand=5,padx=5, pady=5)
label3= Tkinter.Label(frame, text=tl1, font=("Helvetica", 18))
label3.pack(side=TOP,fill=X, expand=5,padx=5, pady=5)
label4= Tkinter.Label(frame, text=tl2, font=("Helvetica", 18))
label4.pack(side=TOP,fill=X, expand=5,padx=5, pady=5)
label5= Tkinter.Label(frame, text=tl3, font=("Helvetica", 18))
label5.pack(side=TOP,fill=X, expand=5,padx=5, pady=5)
label6= Tkinter.Label(frame, text=tl4, font=("Helvetica", 18))
label6.pack(side=TOP,fill=X, expand=5,padx=5, pady=5)
button = Tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=RIGHT)
tk.mainloop()


