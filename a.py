from tkinter import *
import random as rd

r = Tk()
r.geometry('600x650')
r.config(background='black')
l1 = Label(r,text='POINTS = 0 0 0 0          LIFE = 0 3',font=('OCR A Extended',20),background='black',fg='#f2ff26')

c = Canvas(r,height='600',width='600',background='#090807')
l1.pack()
c.pack()

did_shoot = 0

coordinates = []
barriers = []
ship = []       #coordinates
shp = []        #canvas function
sht_me = []     #bullet location
for i in range(0,600,10):
    for j in range(0,600,10):
        coordinates.append([i,j])
for i in range(120):
    s = rd.choice(coordinates)
    c.create_rectangle(s[0],s[1],s[0]+2,s[1]+2,fill='white')

def barrier_create():
    #barriers from 320 to 400
    global barriers
    x = [i for i in range(80,151,5)]
    x.extend([i for i in range(200,271,5)])
    x.extend([i for i in range(330,401,5)])
    x.extend([i for i in range(450,521,5)])
    y = [i for i in range(320,421,5)]
    x0 = [80,200,330,450,85,205,335,455,150,270,265,400,395,520,515,145]
    for i in x:
        for j in y:
            if (i not in x0) or (j not in [320,325]):
                if (i not in x0) or (j not in [400,395,390,385,380]):
                    barriers.append([i,j,c.create_rectangle(i,j,i+5,j+5,fill='red')])

def blt_move():
    global sht_me,did_shoot,barriers
    start = sht_me[0]
    proceed = 1
    for i in barriers:
        if (start[0] == i[0]) and (start[1] == i[1]):
            c.delete(i[2])
            barriers.remove(i)
            proceed = 0
            break
    if start[1] == 10:
        proceed = 0
    if proceed == 0:
        c.delete(sht_me[1])
        sht_me = []
        did_shoot = 0
    else:
        c.delete(sht_me[1])
        sht_me = []
        sht_me.extend([[start[0],start[1]-5],c.create_rectangle(start[0],start[1]-5,start[0]+2,start[1]+15,fill='#0cff0c')])
        r.after(30,blt_move)

def ship_create():
    global ship,shp
    #ind = 5 is shooting
    ship = [[280,550],[280,560],[285,560],[290,550],[290,560],
            [295,530],[295,540],[295,550],[295,560],
            [300,550],[300,560],[305,560],[310,550],[310,560]]
    for i in ship:
        shp.append([i,c.create_rectangle(i[0],i[1],i[0]+5,i[1]+10,fill='#00fcfc')])

def lft_mov(event):
    global ship,shp
    if ship[0][0]>=10:
        for i in shp:
            c.delete(i[1])
        shp = []
        for i in ship:
            i[0]-=5
            shp.append([i,c.create_rectangle(i[0],i[1],i[0]+5,i[1]+10,fill='#00fcfc')])

def rgt_mov(event):
    global ship,shp
    if ship[len(ship)-1][0]<=585:
        for i in shp:
            c.delete(i[1])
        shp = []
        for i in ship:
            i[0]+=5
            shp.append([i,c.create_rectangle(i[0],i[1],i[0]+5,i[1]+10,fill='#00fcfc')])

def shoot(event):
    global sht_me,ship,did_shoot
    if did_shoot == 1:
        pass
    else:
        start = [ship[5][0],ship[5][1]-20]
        sht_me.extend([start,c.create_rectangle(start[0],start[1],start[0]+2,start[1]+20,fill='#0cff0c')])
        did_shoot = 1
        blt_move()

barrier_create()
ship_create()

r.bind('<Left>',lft_mov)
r.bind('<Right>',rgt_mov)
r.bind('<space>',shoot)

r.mainloop()