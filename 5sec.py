import time
import random
import tkinter
from tkinter import *
#a multiplayer quiz game
#14/6/2020
def click(btn):    
    btn['bg'] = '#' + str(random.randint(111111,999999))
x1 = 0
x2 = 0
x3 = 0
x4 = 0
run = False
turns = 1
questions = []
play3 = [[540,620],[280,620],[20,620] ,[540,380],[280,380],[20,380],[540,140],[280,140]]
play4 = [[580,620],[320,620],[60,620] ,[600,380],[320,380],[60,380],[580,140],[320,140]]
play1 = [[620,620],[360,620],[100,620],[640,380],[360,380],[100,380],[620,140],[360,140]]
play2 = [[660,620],[400,620],[140,620],[680,380],[400,380],[140,380],[660,140],[400,140]]
def playerscount(player):
    global players
    players = player
    
    if player >= 2:
        b.config(state = 'disabled')
        players = 2
    if player >=3:
        b.config(state = 'disabled')
        b2.config(state = 'disabled')
        players = 3
    if player >=4:
        b.config(state = 'disabled')
        b2.config(state = 'disabled')
        b3.config(state = 'disabled')
        players = 4

myFile = open("Questions.txt", "r")
for line in myFile:
    questions.append(line.strip("\n"))
myFile.close()
root = Tk()
root.title('3 in ten')
def defplayer():
    if (turns % players) == 1:
        play = 2
    elif (turns % players) == 2:
        play = 3
    elif (turns % players) == 3:
        play = 4
    elif (turns % players) == 0:
        play = 1
    else:
        print('error')
    return(play)
def correct():
    global x1,x2,x3,x4,turns
    mover = defplayer()
    turns += 1
    try:
        
        if mover == 1:
            x1 += 1
            b11.place(x =play1[x1][0] , y = play1[x1][1])
            
        elif mover == 2:
            x2 +=1
            b12.place(x =play2[x2][0] , y = play1[x2][1])
            
        elif mover == 3:
            x3 += 1
            b13.place(x =play3[x3][0] , y = play3[x3][1])
            
        elif mover == 4:
            x4 += 1
            b14.place(x =play4[x4][0] , y = play4[x4][1])
        b4.config(state = 'normal')
        b6.config(state = 'disabled')
        b7.config(state = 'disabled')
    except IndexError:
        if (turns % players) == 1:
            col = b12['bg']
            b12.place_forget()
        elif (turns % players) == 2:
            col = b13['bg']
            b13.place_forget()
        elif (turns % players) == 3:
            col = b14['bg']
            b14.place_forget()
        elif (turns % players) == 0:
            col = b11['bg']
            b11.place_forget()
        print(col)
        b.config(state = 'disabled', bg = col)
        b1.config(state = 'disabled', bg = col)
        b2.config(state = 'disabled', bg = col)
        b3.config(state = 'disabled', bg = col)
        b4.config(state = 'disabled', bg = col)
        b6.config(state = 'disabled', bg = col)
        b7.config(state = 'disabled', bg = col)
        b8.config( bg = col,text = 'WINNER')
        b5.config( bg = col, text = defplayer())
        btn1.config(bg = col)
        btn2.config(bg = col)
        btn3.config(bg = col)
        btn4.config(bg = col)
        btn5.config(bg = col)
        btn6.config(bg = col)
        btn7.config(bg = col)
        btn8.config(bg = col)
        btn9.config(bg = col )
        

        
def incorrect():
    global x1,x2,x3,x4,turns
    turns += 1
    mover = defplayer()
    if mover == 1:
        if x1 == 3:
            x1 = 0
            b11.place(x =play1[x1][0] , y = play1[x1][1])
        elif 4 < x1 < 9:
            x1 = 3
            b11.place(x =play1[x1][0] , y = play1[x1][1])
    elif mover == 2:
        if x2 == 3:
            x2 = 0
            b12.place(x =play1[x1][0] , y = play1[x1][1])
        elif x2 < 9 and x2 > 4:
            x2 = 3
            b12.place(x =play1[x1][0] , y = play1[x1][1])
    elif mover == 3:
        if x3 == 3:
            x3 = 0
            b13.place(x =play1[x1][0] , y = play1[x1][1])
        elif x3 < 9 and x3 > 4:
            x3 = 3
            b13.place(x =play1[x1][0] , y = play1[x1][1])
    elif mover == 4:
        if x4 == 3:
            x4 = 0
            b14.place(x =play1[x1][0] , y = play1[x1][1])
        elif 4 < x4 < 9:
            x1 = 3
            b14.place(x =play1[x1][0] , y = play1[x1][1])
    root.update()
    b6.config(state = 'disabled')
    b7.config(state = 'disabled')
    b4.config(state = 'normal')
def start():
    global players,b11,b12,b13,b14,run

    b4.config(state = 'disabled' )
    b2.config(state = 'disabled')
    b.config(state = 'disabled')
    b3.config(state = 'disabled')
    if not run:
        if players > 2:
            b13 = Button(frm , height = 3 , width = 3, font = ('Ariel' , 8 , 'bold'), bg = '#' + str(random.randint(111111,999999)),command = lambda :click(b13))
            b13.place(x = 540 , y = 620)
        if players > 3:
            b14 = Button(frm , height = 3 , width = 3, font = ('Ariel' , 8 , 'bold'), bg = '#' + str(random.randint(111111,999999)),command = lambda :click(b14))
            b14.place(x = 580 , y = 620)
        b11 = Button(frm , height = 3 , width = 3, font = ('Ariel' , 8 , 'bold'), bg = '#' + str(random.randint(111111,999999)),command = lambda :click(b11))
        b12 = Button(frm , height = 3 , width = 3, font = ('Ariel' , 8 , 'bold'), bg = '#' + str(random.randint(111111,999999)),command = lambda :click(b12))
        b12.place(x = 660 , y = 620)
        b11.place(x = 620 , y = 620)
        run = True
    random.shuffle(questions)
    y = questions[0]
    questions.remove(y)
    b5.config(text = y)
    b8.config(text = 'go')
    root.update()
    time.sleep(1)
    b8.config(text = '5')
    root.update()
    time.sleep(1)
    b8.config(text = '4')
    root.update()
    time.sleep(1)
    b8.config(text = '3')
    root.update()
    time.sleep(1)
    b8.config(text = '2')
    root.update()
    time.sleep(1)
    b8.config(text = '1')
    root.update()
    time.sleep(1)
    b8.config(text = 'times up')
    b4.config(state = 'disabled')
    b6.config(state = 'normal')
    b7.config(state = 'normal')
    
frame1 = Frame(root)
frame1.pack()

frm = Frame(frame1)
frm.pack()
btn1 = Label(frm , height = 7 , width = 14, font = ('Ariel' , 20 , 'bold'),text = 'start',  bg = 'light grey')
btn2 =Label(frm , height = 7 , width = 14, font = ('Ariel' , 20 , 'bold'),text = '1',bg  = 'light grey')
btn3 =Label(frm , height = 7 , width = 14, font = ('Ariel' , 20 , 'bold'),text = '2', bg = 'light grey')
btn4 =Label(frm , height = 7 , width = 14, font = ('Ariel' , 20 , 'bold'),text = '3',  bg = 'orange')
btn5 =Label(frm , height = 7 , width = 14, font = ('Ariel' , 20 , 'bold'),text = '4',  bg = 'light grey')
btn6 =Label(frm , height = 7 , width = 14, font = ('Ariel' , 20 , 'bold'),text = '5', bg = 'red')
btn7 =Label(frm , height = 7 , width = 14, font = ('Ariel' , 20 , 'bold'),text = '6',  bg = 'red')
btn8 =Label(frm , height = 7 , width = 14, font = ('Ariel' , 20 , 'bold'),text = '7', bg = 'red')
btn9 =Label(frm , height = 7 , width = 14, font = ('Ariel' , 20 , 'bold'), borderwidth=1, relief=GROOVE, bg = 'light grey')
b = Button(frm , height = 2 , width = 2, font = ('Ariel' , 8 , 'bold'), bg = 'grey', text = '2', command = lambda:  playerscount(2))
b1 =Label(height = 2, width = 5,font = ('Ariel' , 10 , 'bold'), bg = 'light grey', text = 'Players')
b2 = Button(frm , height = 2 , width = 2, font = ('Ariel' , 8 , 'bold'), bg = 'grey', text = '3', command = lambda: playerscount(3))
b3 = Button(frm , height = 2 , width = 2, font = ('Ariel' , 8 , 'bold'), bg = 'grey', text = '4' , command = lambda: playerscount(4))
b4 = Button(frm , height = 3 , width = 5, font = ('Ariel' , 8 , 'bold'), bg = 'grey', text = 'Start' , command = lambda: start())
b5 =  Label(frm , height = 3 , width = 30, font = ('Ariel' , 8 , 'bold'), bg = 'grey', text = ' ')
b6 = Button(frm , height = 2 , width = 2, font = ('Ariel' , 8 , 'bold'), bg = 'grey', text = '✓' , command = lambda: correct())
b7 = Button(frm , height = 2 , width = 2, font = ('Ariel' , 8 , 'bold'), bg = 'grey', text = 'X' , command = lambda: incorrect())
b8 = Label(frm , height = 3 , width = 12, font = ('Ariel' , 8 , 'bold'), text = 'waiting to start', bg = 'grey')


btn9.grid(row = 0, column = 0)
btn8.grid(row = 0, column = 1)
btn7.grid(row = 0, column = 2)
btn6.grid(row = 1, column = 0)
btn5.grid(row = 1, column = 1)
btn4.grid(row = 1, column = 2)
btn3.grid(row = 2, column = 0)
btn2.grid(row = 2, column = 1)
btn1.grid(row = 2, column = 2)
b.place(x = 10 , y = 60)
b2.place(x = 35 , y = 60)
b1.place(x = 30 , y = 20)
b3.place(x = 60 , y = 60)
b4.place(x = 170 ,y = 20)
b5.place (x = 20 ,y = 180)
b6.place(x = 110 , y = 60)
b7.place( x = 140 , y = 60)
b8.place(x = 70 , y = 118)

b6.config(state = 'disabled')
b7.config(state = 'disabled')

root.mainloop

