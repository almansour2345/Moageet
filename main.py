#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository  import Gtk, Gdk

import re
import json
import sys
import commands
import time
import datetime
import requests
 
from datetime import datetime

 
#### local time 
a = time.ctime()

rg = '%s%s' %(a[11],a[12])
rg2 = '%s%s' %(a[14],a[15])
g=int(rg)
g2=int(rg2)
 
#### requesting riyadh prayer times from the link 

#r = requests.get('http://muslimsalat.com/riyadh.json')
#### uncomment below to get global based on your location
r = requests.get('http://api.aladhan.com/timingsByCity?city=riyadh&country=sa&method=1')
### getting the data from into a varibal 
p= r.text
 
#xx=json.load(p)
 
##print p
 

tt=p.find('timings')
tt2=p.find('}',tt)
tr=p[tt:tt2]

##print tr

tf=tr.find('Fajr')
ttf=tr.find(',',tf)
trf=tr[tf:ttf]
hrf=trf[7:9]
mrf=trf[10:12]
#print hrf
#print mrf
#print trf

td=tr.find('Dhuhr')
ttd=tr.find(',',td)
trd=tr[td:ttd]
hrd=trd[8:10]
mrd=trd[11:13]
#print trd
#print hrd
#print mrd

ts=tr.find('Asr')
tts=tr.find(',',ts)
trs=tr[ts:tts]
had=trs[6:8]
mad=trs[9:11]
#print trs
#print had
#print mad


tm=tr.find('Maghrib')
ttm=tr.find(',',tm)
trm=tr[tm:ttm]
hmd=trm[10:12]
mmd=trm[13:15]
#print trm
#print hmd
#print mmd


ti=tr.find('Isha')
tti=tr.find(',',ti)
tri=tr[ti:tti]
hid=tri[7:9]
mid=tri[10:12]

#print tri
#print hid
#print mid

tn=tr.find('Sunrise')
ttn=tr.find(',',tn)
trn=tr[tn:ttn]
hrn=trn[10:12]
mrn=trn[13:15]
#print trn
#print hrn
#print mrn
te=tr.find('Sunset')
tte=tr.find(',',te)
tre=tr[te:tte]
hren=tre[9:11]
mren=tre[12:14]
#print tre
#print hren
#print mren
 


fajrh=int(hrf)
fajrm=int(mrf)
duhrh=int(hrd)
duhrm=int(mrd)
asrh=int(had)
asrm=int(mad)
maghrebh=int(hmd)
maghrebm=int(mmd)
ishah=int(hid)
isham=int(mid)
sunriseh=int(hrn)
sunrisem=int(mrn)
sunseth=int(hren)
sunsetm=int(mren)
 
 
gh=int(g)	
 
gm=int(g2)
cx=0	

	 
def grp():
	vv=gh
	gm2=g2
	global cx

	#fajr
	if vv >= ishah and vv <= 24 or vv >=0 and vv <= fajrh:  ## if time "vv" more or equal  to 19 8 isha time or less then  12 midnight or more then 0 12 midnight and less or equal fajer 4 am 

		if vv == ishah and gm2 <= isham: ## if its equal 17 or 8 pm and minuets equal less then 47 ! then isha
			cx=5
		elif vv == ishah and gm2 <= isham:
			cx=5
		elif vv == ishah and gm2 > isham:  ## if its equal 17 or 8 pm and minuets  more  then 47 ! then fajer
			cx=1
		elif vv == fajrh and gm2 <= fajrm: ## if vv equal 4 and minuets less then 27 ! then fajer
			cx=1
		else:
			cx=1
	#duhr		
	elif vv > fajrh and vv <= duhrh: ## if more then 4  and less or equal then 11 !
		if vv == duhrh and gm2 <= duhrm: ## if vv equal 11 and minutes are less or equal 45 then duhr
			cx=2
		elif vv < duhrh: ## if its less then 11 ! duhr 
			cx=2
		else:
			cx=3
	
	#asr
	elif vv > duhrh and vv <= asrh: ## if vv more then 11 and less or equal  15
		if vv == asrh and gm2 <=asrm: ## if vv eqaul 15 and minuets equal or less then 11 ! then asr
			cx=3
		elif vv < asrh: ## if vv less then 15
			cx=3
		else:
			cx=4
			
	elif vv > asrh and vv <= maghrebh: ## if vv more then 15 and vv equal or less then 17 
		if vv == maghrebh and gm2 <= maghrebm: ## if vv equal 17 and minuets less or equal 47! then maghreb
			cx = 4
		elif vv < maghrebh: ## if vv less then 17 ! then maghreeb
			cx=4
		else: ## else isha 
			cx=5
			
	elif vv > maghrebh and vv <=ishah: ## if vv more then 17 and vv equal or less  19 
		if vv == ishah and gm2 <= isham: ## if vv equal 19 and minuets less or equal 02 ! then isha
			cx=5
		elif vv < ishah: ## if vv less then 19 ! then isha
			cx=5
		else: ## else fajer = not more 
			cx=1
	return cx


tt = grp()
#print tt 
if tt ==1:
	pn="Fajr"
	
elif tt==2:
	pn="Duhr"
elif tt==3:
	pn="Asur"
elif tt==4:
	pn="Magreeb"
elif tt==5:
	pn="Esha"


had=int(had)-12
hmd=int(hmd)-12
hid=int(hid)-12
hren=int(hren)-12


def tooa():
	arr = time.ctime()

	rgrr = '%s%s' %(arr[11],arr[12])
	rg2rr = '%s%s' %(arr[14],arr[15])
	
	#rgrr="19"
	#rg2rr="11"
	xr=arr[11]

	if tt>2 :
		rgrr=int(rgrr)-12

	#print rgrr
	
	g=str(rgrr) + ":" + rg2rr + ":" + "00"
	gfT=hrf + ":" + mrf + ":"	+ "00"
	gdT=hrd + ":" + mrd + ":"	+ "00"
	gaT=str(had) + ":" + mad + ":"	+ "00"
	gmT=str(hmd) + ":" + mmd + ":"	+ "00"
	giT=str(hid) + ":" + mid + ":"	+ "00"
	
	fmt = '%H:%M:%S'
		
	if tt==1:
		pn="Fajr"
		d1 = datetime.strptime(g, fmt)
		d2 = datetime.strptime(gfT, fmt)
		diff = d2-d1
		qq=str(diff)
		 
		css="Prayer Fajr in: %s " % qq
		 


	elif tt==2:
		pn="Duhr"
		d1 = datetime.strptime(g, fmt)
		d2 = datetime.strptime(gdT, fmt)
		diff = d2-d1
		qq=str(diff)
		 
		css="Prayer Duhr in: %s " % qq
		 

	elif tt==3:
		pn="Asr"
		d1 = datetime.strptime(g, fmt)
		d2 = datetime.strptime(gaT, fmt)
		diff = d2-d1
		qq=str(diff)
		 
		css="Prayer Asr in: %s " % qq
		 

	elif tt==4:
		pn="Maghreeb"
		d1 = datetime.strptime(g, fmt)
		d2 = datetime.strptime(gmT, fmt)
		diff = d2-d1
		qq=str(diff)
		 
		css="Prayer Maghreeb in: %s " % qq
		 

	elif tt==5:
		pn="Isha"
		
		d1 = datetime.strptime(g, fmt)
		d2 = datetime.strptime(giT, fmt)
		diff = d2-d1
		qq=str(diff)
		 
		css="Prayer Isha in: %s " % qq
 

	return css
			
cssd=tooa()
faj=str(hrf)+":" + str(mrf)
duh=str(hrd)+":" + str(mrd)
asrr=str(had)+":" + str(mad)
mage=str(hmd)+":" + str(mmd)
ish=str(hid)+":" + str(mid)
ris=str(hrn)+":" + str(mrn)
seet=str(hren)+":" + str(mren)
grgr=int(rg)
if grgr>12:
	rg=grgr-12
	
d22=str(rg)+":"+str(rg2)
class LabelWindow(Gtk.Window):
	

	def __init__(self):
		Gtk.Window.__init__(self, title="Prayer Times in Riyadh")
		self.set_border_width(11)
		hbox = Gtk.Box(spacing=12)
		hbox.set_homogeneous(True)
		self.add(hbox)

 

		vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=11)
		vbox_left.set_homogeneous(False)
		vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=11)
		vbox_right.set_homogeneous(False)
		vbox_top = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
		vbox_top.set_homogeneous(False)
		vbox_buttom = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		vbox_buttom.set_homogeneous(False)
		hbox.pack_start(vbox_left, True, True, 0)
		hbox.pack_start(vbox_right, True, True, 0)

		
		label = Gtk.Label("time now:") 
		label.set_justify(Gtk.Justification.LEFT)
		vbox_left.pack_start(label, True, True, 1)


		label = Gtk.Label("Fajer") 
		label.set_name('L1')
		label.set_justify(Gtk.Justification.LEFT)
		vbox_left.pack_start(label, True, True, 0)
		
		label = Gtk.Label("Duhr")
		label.set_justify(Gtk.Justification.RIGHT)
		vbox_left.pack_start(label, True, True, 0)
		
		label = Gtk.Label("Asur")
		label.set_justify(Gtk.Justification.RIGHT)
		vbox_left.pack_start(label, True, True, 0)
		
		label = Gtk.Label("Maghrib")
		label.set_line_wrap(True)
		vbox_left.pack_start(label, True, True, 0)
		
		label = Gtk.Label("Isha")
		label.set_line_wrap(True)
		label.set_justify(Gtk.Justification.FILL)
		vbox_left.pack_start(label, True, True, 0)
		


		label = Gtk.Label("UpComing Prayer")
		label.set_line_wrap(True)
		label.set_justify(Gtk.Justification.FILL)
		vbox_left.pack_start(label, True, True, 0)


		label = Gtk.Label("sunrise")
		label.set_line_wrap(True)
		label.set_justify(Gtk.Justification.FILL)
		vbox_left.pack_start(label, True, True, 0)

		label = Gtk.Label("sunset")
		label.set_line_wrap(True)
		label.set_justify(Gtk.Justification.FILL)
		vbox_left.pack_start(label, True, True, 0)
		
############## start the lef vbox

		label = Gtk.Label(a) 
		label.set_justify(Gtk.Justification.LEFT)
		vbox_right.pack_start(label, True, True, 0)


		label = Gtk.Label(faj)
		label.set_line_wrap(True)
		label.set_justify(Gtk.Justification.FILL)
		vbox_right.pack_start(label, True, True, 0)


		label = Gtk.Label(duh)
		label.set_line_wrap(True)
		label.set_justify(Gtk.Justification.FILL)
		vbox_right.pack_start(label, True, True, 0)



		label = Gtk.Label(asrr)
		label.set_line_wrap(True)
		label.set_justify(Gtk.Justification.FILL)
		vbox_right.pack_start(label, True, True, 0)




		label = Gtk.Label(mage)
		label.set_line_wrap(True)
		label.set_justify(Gtk.Justification.FILL)
		vbox_right.pack_start(label, True, True, 0)



		label = Gtk.Label(ish)
		label.set_line_wrap(True)
		label.set_justify(Gtk.Justification.FILL)
		vbox_right.pack_start(label, True, True, 0)



		label = Gtk.Label(cssd)
		label.set_line_wrap(True)
		label.set_justify(Gtk.Justification.FILL)
		vbox_right.pack_start(label, True, True, 0)



		label = Gtk.Label(ris)
		label.set_line_wrap(True)
		label.set_justify(Gtk.Justification.FILL)
		vbox_right.pack_start(label, True, True, 0)





		label = Gtk.Label(seet)
		label.set_line_wrap(True)
		label.set_justify(Gtk.Justification.FILL)
		vbox_right.pack_start(label, True, True, 0)



		button = Gtk.Button("Close")
		button.connect("clicked", self.onButtonPressed)
		hbox.pack_end(button, True, True, 0)
		 

	def onButtonPressed(self, button):
		Gtk.main_quit()


def main(argv):

    def gtk_style():
        css = b"""

GtkWindow {

}
 
 


L1 {
    color: blue;
    background-color: #BC0909;
    border-style: outset;
    border-color: #333;
    padding: 8px 4px;
	border-radius: 13px;
	font-size:21px;	
	transition: 0.3s; 
	border-right: none;
}
 
.label {
	box-shadow: 3px 5px 5px #888888;
    color: white;
    background-color: #525252;
    border-style: outset;
    border-color: #333;
    padding: 18px 18px;
	border-radius: 13px;
	font-size:14px;	
	transition: 0.3s; 
	border-right: none;
}
.button button {
    color: green;
    background-color: shade (@bg_color, 1.44);
    border-style: inset;
    border-width: 2px 0 2px 2px;
    border-color: #333;
    padding: 12px 4px;
	border-radius: 32px;
}
.button:first-child {
    border-radius: 13px 0 0 5px;
}
.button:last-child {
    border-radius: 10px 5px 5px 0;
    border-width: 2px;
}
.button:hover {
    padding: 12px 48px;
    background-color: shade (@bg_color, 1.06);
}
.button *:hover {
    color: white;
}
.button:hover:active,
.button:active {
      background-color: shade (@bg_color, 0.85);
}
        """
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css)

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    gtk_style()
    win = LabelWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
	main(sys.argv)


