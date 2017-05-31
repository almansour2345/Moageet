#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter
from Tkconstants import *
import re

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

#r = requests.get('http://muslimsalat.com/riyadh.json')
#### uncomment below to get global based on your location


r = requests.get('http://muslimsalat.com/daily.json')



### getting the data from into a varibal 

p= r.text
 
##### extracting the data 

tfajr=p.find('fajr')
fp0=p.find('am',tfajr)
jl0=p[tfajr:fp0]
tj0=jl0[0:4]
tj1=jl0[7:11]
tl0=tj0 + '\t-_' + tj1+'_-'
 
#tl0=p[tfajr:fp0]
# print tl0

tduher=p.find('dhuhr')
fp1=p.find('pm',tduher)

tl1=p[tduher:fp1]
td0=tl1[0:5]
td1=tl1[7:14]
tl1=td0 + '\t-_' + td1+'_-'


# print tl1



tasr=p.find('asr')
fp2=p.find('pm',tasr)

tl2=p[tasr:fp2]
tr0=tl2[0:4]
tr1=tl2[6:11]
tl2=tr0 + '\t-_' + tr1+'_-'


# print tl2



tmaghrib=p.find('maghrib')
fp3=p.find('pm',tmaghrib)

tl3=p[tmaghrib:fp3]
# print tl3


tisha=p.find('isha')
fp4=p.find('pm',tisha)

tl4=p[tisha:fp4]


 
 
 
 
ms = re.search('(\b)?(\d+):(\d+)',tl0)
ms1 = re.search('(\b)?(\d+):(\d+)',tl1)
ms2 = re.search('(\b)?(\d+):(\d+)',tl2)
ms3 = re.search('(\b)?(\d+):(\d+)',tl3)
ms4 = re.search('(\b)?(\d+):(\d+)',tl4)

dr = ms.group()
dr1 = ms1.group()
dr2 = ms2.group()
dr3 = ms3.group()
dr4 = ms4.group()

fdr="Fajer Prayer (" + dr + ")"
dudr="Duhur Prayer (" + dr1 + ")"
asrdr="Asur Prayer (" + dr2 + ")"
mgdr="Magrib Prayer (" + dr3 + ")"
esdr="Esha Prayer (" + dr4 + ")"
#### starting the GUI "user interface" and inserting the times 
### a def to capture keyboard events 


def key(event):
	frame.focus_set()
	tk.destroy() , repr(event.char)
 
tk.title("Moaget Al-Salat")
tk.geometry("450x500")		

## here execute the key event and exit the app
	
tk.bind("<Key>", key)


frame = Tkinter.Frame(tk, relief=RIDGE, borderwidth=5,width=600, height=1000)#, bg="gray12"



frame.config(bg="gray9")

#frame.bind("<Button-1>", callback)
frame.pack(fill=BOTH,expand=3)

frame.pack_propagate(3)



label = Tkinter.Label(frame, text="Time Now", font=("Helvetica", 24),bg="gray38")
label.pack(side=TOP,fill=X, expand=3,padx=5, pady=5)
label7= Tkinter.Label(frame, text=a , font=("Helvetica", 21),bg="gray35")
label7.pack(side=TOP,fill=X, expand=5,padx=5, pady=5)
label1 = Tkinter.Label(frame, text="Prayer\'s Times ", font=("Helvetica", 21),bg="gray78")
label1.pack(side=TOP,fill=X, expand=3,padx=5, pady=5)
label2= Tkinter.Label(frame, text=fdr, font=("Helvetica", 21),bg="gray59")
label2.pack(side=TOP,fill=X, expand=5,padx=5, pady=5)
label3= Tkinter.Label(frame, text=dudr, font=("Helvetica", 21),bg="gray45")
label3.pack(side=TOP,fill=X, expand=5,padx=5, pady=5)
label4= Tkinter.Label(frame, text=asrdr, font=("Helvetica", 21),bg="gray43")
label4.pack(side=TOP,fill=X, expand=5,padx=5, pady=5)
label5= Tkinter.Label(frame, text=mgdr, font=("Helvetica", 21),bg="gray39")
label5.pack(side=TOP,fill=X, expand=5,padx=5, pady=5)
label6= Tkinter.Label(frame, text=esdr, font=("Helvetica", 21),bg="gray35")
label6.pack(side=TOP,fill=X, expand=5,padx=5, pady=5)
button = Tkinter.Button(frame,text="Exit",command=tk.destroy)
#button.bind("<Key>", key)

button.pack(side=RIGHT)

tk.mainloop()
