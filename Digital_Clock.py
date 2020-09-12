import sys
from tkinter import *
import time
import turtle
import datetime
import calendar

# Time recognizton
alarmHour = int(input("What hour do you want the clock to pop up on screen? "))
alarmMinute = int(input("What minute do you want the clock to pop up on screen? "))
amPm = str(input("Am or Pm: "))

if(amPm == "pm"):
    alarmHour = alarmHour + 12

while(1 == 1):
    if(alarmHour == datetime.datetime.now() .hour and
       alarmMinute == datetime.datetime.now() .minute):
      break

###################

# Clock
def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200,tick)


root = Tk("The time is:")
clock=Label(root, font=("times", 50, "bold"), bg= "blue")
clock.grid(row=0, column=1)
tick()

root.mainloop()
###################
# End of the code 
