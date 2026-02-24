import tkinter 
from tkinter import *
import datetime
import time
import winsound
import os
alarm = Tk()

alarm.title("Pixel Alarm")
alarm.geometry("400x400")

title = Label(alarm,text="Set hour for alarm:")
title.pack()
hour = Entry(alarm,width="85")
hour.pack()
title1 = Label(alarm,text="Set minutes for alarm:")
title1.pack()
minute = Entry(alarm,width="85")
minute.pack()
title2 = Label(alarm,text="AM/PM:")
title2.pack()
ampm = Entry(alarm,width="85")
ampm.pack()

def stopbtn():
   stopbutton.destroy()
def alarmset():
   hourtime = hour.get()
   minutetime = minute.get()
   ampmtime = ampm.get()
   currenttime = datetime.datetime.now()
   if ampmtime == "AM" and hourtime == 12:
         hourtime -= 12
   if ampmtime == "PM":
         hourtime += 12
   print("Alarm time:",str(hourtime) + ":" + str(minutetime),str(ampmtime))
   currenttime1 = currenttime.hour
   currenttime2 = currenttime.minute
   currenttime3 = currenttime.strftime("%p")
   print("Current time:",str(currenttime1) + ":" + str(currenttime2),str(currenttime3))

   while True:
    if datetime.datetime.now().hour == int(hourtime) and datetime.datetime.now().minute == int(minutetime):
         print("Wake up...")
         os.system("C:\\Users\\MrsZulu\\Documents\\Programming\\Assistance\\ChocolateCookieJam.mp3")
         global stopbutton
         stopbutton =  Button(alarm,text="Stop Alarm",width="25",height="2",command=stopbtn)
         stopbutton.pack()
         break
settime = Button(alarm,text="Set Alarm",width="25",height="2",command=alarmset)
settime.pack()


alarm.mainloop()