import os
import datetime
from time import sleep
#11/7/21
#an alarm that will open a video file when its a certain time
#the video can vary depending on the day except on weekends where it doesn't
#start to give the user a 2 days off
#needs some mp4 files in the same folder with the names below
alarmw = '18:25'
def clock():
    d = str(datetime.datetime.today()).split()[0]
    w = datetime.date.today()
    we = datetime.date.today()
    wee =int(we.weekday())
    now = datetime.datetime.now()
    t = now.strftime("%H:%M")
    return ([wee ,t,d])
while True:
    n = clock()
    
    if n[1] == alarmw:
        if n[0] == 0:
            os.startfile('mon.mp4')
        elif n[0] == 1:
            os.startfile('tue.mp4')
        elif n[0] == 2:
            os.startfile('wed.mp4')
        elif n[0] == 3:      
            os.startfile('th.mp4')
        elif n[0] == 4:
            os.startfile('fri.mp4')
        elif n[0] == 5:
            pass
        elif n[0] == 6:
            pass
        
    
    sleep(59)
    #its 59 seconds so it should loop once every minute

