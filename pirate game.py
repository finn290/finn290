import pygame,os,time
from random import randint,choice,shuffle

pygame.init()
pygame.joystick.init()

#constants
X,Y = 1650, 850
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0,128,0)
BLUE = (0,0,255)
SAND = (223,208,68)
VEL = 16
pirh , pirw =50,40
#pirw = 40
XTIL,YTIL = 70,50
pirx,piry = 4,4
coins = 0
#game files
COINPICK= pygame.mixer.Sound('coinpickup.wav')
DEATH1 = pygame.mixer.Sound('death1.wav')
DEATH2 = pygame.mixer.Sound('death2.wav')
GAME_OVER = pygame.mixer.Sound('game over.wav')
DIR = 'R'
GEN1 = pygame.mixer.Sound('gen1.wav')
GEN2 = pygame.mixer.Sound('gen2.wav')
GEN3 = pygame.mixer.Sound('gen3.wav')
jGO  = pygame.mixer.Sound('go.wav')
theme  = pygame.mixer.Sound('riamu.wav')
theme.set_volume(0.3)
KILL = pygame.mixer.Sound('kill.wav')
yes = pygame.mixer.Sound('yes.wav')
START = pygame.mixer.Sound('start.wav')
TREASURE = pygame.mixer.Sound('treasure.wav')

#GAME_WIN  = pygame.mixer.Sound('win.mp3')
sea = pygame.image.load('sea.jpg')
icon = pygame.image.load('rodger.png')
PROTAG =  pygame.image.load('pirate.png')
mapp = pygame.image.load('map.jpg')
chestim = pygame.image.load('chest.png')
chestim = pygame.transform.scale(chestim,(28,14))
coin= pygame.image.load('dubloon.png')
coin = pygame.transform.scale(coin,((164),(100)))
sand = pygame.image.load('sand.jpeg')
sand = pygame.transform.scale(sand, (VEL , VEL))
sea = pygame.transform.scale(sea,((1200),(Y)))
PROTAG = pygame.transform.scale(PROTAG, (pirh, pirw))
protag2 = pygame.image.load('pirate2.png')
protag2 = pygame.transform.scale(protag2, (pirh, pirw))
can = pygame.image.load('cannibal.png')
can = pygame.transform.scale(can, (pirh, pirw))
boat  =  pygame.image.load('ship.png')
boat2  =  pygame.image.load('boat2.png')
boat = pygame.transform.scale(boat, (pirh, pirw))
boat2 = pygame.transform.scale(boat2, (pirh, pirw))
protag1 = [[PROTAG,protag2],[boat,boat2]]
land = 1
sprite = 0
left= False
mapp = pygame.transform.scale(mapp, (500,Y))
deathclock = False
deathtick = 0
#window setup
WIN = pygame.display.set_mode((X,Y))
WIN.fill(WHITE)
pygame.display.set_caption('pirate game')
clock = pygame.time.Clock()
grid = [ ]
#game files
COINPICK= pygame.mixer.Sound('coinpickup.wav')
DEATH1 = pygame.mixer.Sound('death1.wav')
DEATH2 = pygame.mixer.Sound('death2.wav')
GAME_OVER = pygame.mixer.Sound('game over.wav')
DIR = 'R'
GEN1 = pygame.mixer.Sound('gen1.wav')
GEN2 = pygame.mixer.Sound('gen2.wav')
GEN3 = pygame.mixer.Sound('gen3.wav')
jGO  = pygame.mixer.Sound('go.wav')
theme  = pygame.mixer.Sound('theme.wav')
theme.set_volume(0.3)
KILL = pygame.mixer.Sound('kill.wav')
START = pygame.mixer.Sound('start.wav')
TREASURE = pygame.mixer.Sound('treasure.wav')
#GAME_WIN  = pygame.mixer.Sound('win.mp3')
sea = pygame.image.load('sea.jpg')
icon = pygame.image.load('rodger.png')
PROTAG =  pygame.image.load('pirate.png')
mapp = pygame.image.load('map.jpg')
coin= pygame.image.load('dubloon.png')
coin = pygame.transform.scale(coin,((164),(100)))
sand = pygame.image.load('sand.jpeg')
sand = pygame.transform.scale(sand, (pirw ,pirh))
sea = pygame.transform.scale(sea,((1200),(Y)))
PROTAG = pygame.transform.scale(PROTAG, (pirh, pirw))
protag2 = pygame.image.load('pirate2.png')
protag2 = pygame.transform.scale(protag2, (pirh, pirw))
can = pygame.image.load('cannibal.png')
can = pygame.transform.scale(can, (pirh, pirw))
boat  =  pygame.image.load('ship.png')
boat2  =  pygame.image.load('boat2.png')
mine  =  pygame.image.load('mine.png')
boat = pygame.transform.scale(boat, (pirh, pirw))
boat3  =  pygame.image.load('ship.png')
boat3 = pygame.transform.scale(boat3, (pirh, pirw))
mine = pygame.transform.scale(mine, (pirh, pirw))
boat2 = pygame.transform.scale(boat2, (pirh, pirw))
protag1 = [[PROTAG,protag2],[boat,boat2]]
land = 1
sprite = 0
left= False
mapp = pygame.transform.scale(mapp, (500,Y))
deathclock = False
deathtick
#window setup
WIN = pygame.display.set_mode((X,Y))
WIN.fill(WHITE)
pygame.display.set_caption('pirate game')
clock = pygame.time.Clock()
pirates = [ ]
grid = [ ]
vis_haz = [ ]
#hazards
chests_left = 10
cannibals_left= 3
tribes_left = 3
pirates_left = randint(10,20)
seam_monst_left = 2
islands = [ ]
myfont = pygame.font.SysFont('monospace',50)
def lose(killer):
    global deathclock,mapp
    deathclock = True
    mapp = pygame.image.load('9.jpg')
    mapp = pygame.transform.scale(mapp, (500,Y))
def chest():
    global coins
    coins += randint(250,750)
    COINPICK.play()
def cannibal():
    global can
    DEATH2.play()
    lose('c')
    can = pygame.image.load('cannibal.png')
    can = pygame.transform.scale(can, (pirh, pirw))
def seamon():
    DEATH2.play()
    lose('m')


    
class island:

    def __init__(self, hazard):
        self.xloc = int(xloc)
        self.yloc = int(yloc)
        self.hazard = hazard



         
def gen_hazards(islands):
    hazards = [ ]
    shuffle(islands)
    #chests
    for h in range(10):
        hazards.append([islands[h],'t'])
    #cannibals
    for h in range(10,13):
        hazards.append([islands[h],'c'])
    for h in range(13,16):
        hazards.append([islands[h],'l'])
def dev_mode():
    for j in hazards:
        isx = int((j[0].split(':')[0]))
        isy = int(((j[0].split(':'))[1]))
        if j[1] == 't':
            WIN.blit(chestim,((isx + 5,isy)))
        elif j[1] == 'c':
            WIN.blit(can,(isx,isy))
        elif j[1] == 'l':
            WIN.blit(mine,(isx,isy))
            
          
 
f=open('loc1.txt','r')
for lines in f:
    grid.append(lines)


def window(WIN,DIR,land):
    global protag1,sprite,left,coins,deathtick,vis_haz
    if deathclock:
        deathtick += 5
    if deathtick > 600:
        play = False
    WIN.fill(WHITE)
    pygame.display.set_icon(icon)
    dubs = str(coins)
    dubs = (dubs +' dubloons')
    label = myfont.render((dubs),80,GREEN)
    
    WIN.blit(sea,(0,0))
    WIN.blit(mapp,(1180,0))
    WIN.blit(coin,(1180,86))
    WIN.blit(label,(1299,106))
#    for j in hazards:
 #       isx = int((j[0].split(':')[0]))
 #       isy = int(((j[0].split(':'))[1]))
 #       if j[1] == 't':
 #           WIN.blit(chestim,((isx + 5,isy)))
  #      elif j[1] == 'c':
  #          WIN.blit(sea,(0,0))
    #    elif j[1] == 'l':
    #        WIN.blit(sea,(0,0))
    #    WIN.blit(chestim,((isx + 5,isy)))
    
    
            
    for lox in islands:
        place_island(lox) 

    if DIR == 'L' and not left:
        sprite = 1
        left = True
    elif (DIR == 'R') and left:    
        sprite = 0
        left = False
    WIN.blit(protag1[land][sprite],(pirx - 4,piry - 4))
    if active_haz == 't':
        WIN.blit(chestim,(pirx,piry))
    dev_mode()
    
    pygame.display.update()
def place_island(coor):
    
    isx = (coor.split(':'))[0]
    isx = int(isx) 
    
    isy = int((coor.split(':'))[1])
    try:
        y = int(isy) 
        WIN.blit(sand,(isx,isy))
    except:
        pass

hazards = [ ]       
def island_gen(size):
    global islands
    starting_loc= randint(1,3500)
    shape = randint(70,72)
    for forx in range(size):
        
        for fory in range(size):
            
            try:
            
                islands.append(grid[((starting_loc + fory)+ forx *shape )])
            except IndexError:
                pass
            
        
for gen in range(2):    
    island_gen(10)
    island_gen(8)
    island_gen(4)
island_gen(6)
seas = [ ]
for lands in grid:
    for isles in islands:
        if lands == isles:
            pass
        else:
            seas.append(lands)
            
def pirate_move():
    locpir = [ ]
    
    for boats in pirates:
        enpirx= (boats.split(':'))[0]
        enpiry = (boats.split(':'))[1]
        dirp = choice(['L','R','U','D'])
        enpiry = int(enpiry)
        enpirx = int(enpirx)
        if dirp == 'L':
            if enpirx - 16 > 0:
                enpirx -= 16
        if dirp == 'R':
            if enpirx + 16 > 1136:
                enpirx += 16
        if dirp == 'U':
            if enpiry - 16 < 3:
                enpiry -= 16
        if dirp == 'D':
            if enpiry + 16 > 800:
                enpiry+= 16
        p = str(str(enpirx) + ':' + str(enpiry))
        locpir.append(p)
def turnend():
    pirate_move()
        
def gen_hazards(islands):
    global pirates
    shuffle(islands)
    #chests
    for h in range(10):
        hazards.append([islands[h],'t'])
    #cannibals
    for h in range(10,13):
        hazards.append([islands[h],'l'])
    #tribe
    for h in range(13,15):
        hazards.append([islands[h],'c'])
    #sea monsters
    shuffle(seas)
    for h in range(2):
        hazards.append([seas[h],'m'])
    for h in range(2,22):
        pirates.append(seas[h])
        
    turnend()
def check_hazards(coor,seas):
    qck_haz = [ ]
    for locs in hazards:
        if coor == locs[0]:
            qck_haz.append(locs[1])
            hazards.remove(locs)
    for haz in qck_haz:
        if haz == 't':
            chest()
            return 't'
        if haz == 'c':
            cannibal()
            return 'c'
        if haz == 'm':
            seamon()
            return 'm'

gen_hazards(islands)
active_haz = ''
def main():
    global pirx,piry,PROTAG,sprite,land,deathclock,active_haz,mapp,sea

    theme.play()
    DIR = ''
    pygame.display.update()
    play = True
    while play:
        pygame.display.update()
        clock.tick(FPS)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                pygame.quit()
            if (event.type == pygame.KEYDOWN):
            
                if (event.key == pygame.K_ESCAPE):
                     play = False

            if not deathclock:
                if (event.type == pygame.KEYDOWN):
                    pygame.display.update()
                    if (event.key == pygame.K_RIGHT):
                        DIR = 'R'
                        if ((pirx +VEL) < 1136):
                                pirx += VEL
                                pygame.display.update()
                    elif (event.key == pygame.K_LEFT):
                        DIR = 'L'
                        if pirx - VEL > 0:
                            pirx -= VEL
                            pygame.display.update()
                                
                    elif (event.key == pygame.K_DOWN):
                        DIR = 'D'
                        if piry + VEL < (Y - 50):
                            piry += VEL
                            pygame.display.update()
                    elif (event.key == pygame.K_UP):
                        DIR = 'U'
                        if piry - VEL > 0:
                            piry -= VEL
                            pygame.display.update()                    
                    else:
                        DIR = ''
                    tup = str(pirx),str(piry)
                    coor1 = ':'.join(tup)
                    tup = (coor1,'\n')
                    coor1 = ''.join(tup)
                    found = False
                    land = 1
                    for lands in islands:
                        if lands == coor1:
                            found = True
                            land = 0
                    active_haz = check_hazards(coor1,seas)
                        


        window(WIN,DIR,land)
    pygame.quit()


chest()        
if __name__ == '__main__':
    main()
