from  tkinter import *
import datetime
import time
from pygame import mixer
import threading
from tkinter import messagebox



root=Tk()
root.title("Alarm Clock")
root.geometry("600x550")
root.configure(bg='cyan')

alarmtime1=StringVar()
msg2=StringVar()

head= Label(root,text="Alarm Clock",font=('Ariel',30,),justify='center',background='cyan')
head.grid(row=0,columnspan=3,pady=10)

mixer.init()

def alarm():
    a=alarmtime1.get()

    Alarmtime=a
    currenttime=time.strftime("%H:%M")

    while Alarmtime!=currenttime:
        currenttime=time.strftime("%H:%M")
        root.update()

    if Alarmtime==currenttime:
        mixer.music.load('song.mp3')
        mixer.music.play()
        msg1=messagebox.showinfo('Info',f'{msg2.get()}')
        if msg1=='ok':
            mixer.music.stop()

Clockimg= PhotoImage(file="Clock.png")

img= Label(root,image=Clockimg,background='cyan')
img.grid(rowspan=3,column=1,pady=20)

inputtime= Label(root,text="Input Time",font=('Ariel',20),background='cyan')
inputtime.grid(row=5,column=0)

alarmtime=Entry(root,textvariable=alarmtime1,font=('Ariel',20),width=7,background='white')
alarmtime.grid(row=5,column=1)

msg=Label(root,text="Message",font=('Ariel',20),background='cyan')
msg.grid(row=6,column=0)

msginput=Entry(root,textvariable=msg2,font=('Ariel',20),background='white')
msginput.grid(row=6,column=1,pady=20)

submit= Button(root,text="Set Alarm",font=('Ariel',20),background='gold',command=alarm)
submit.grid(row=8,column=1)
root.mainloop()