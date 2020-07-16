import pygame
import random
import math
import time
from pygame import mixer
import webbrowser
import os
from tkinter import*

def l():
    webbrowser.open('https://mohfw.gov.in/')








tick = [0,0,0,0,0,0,0,0,0,0,0,0]

score = 0






icon = pygame.image.load("virus.png")
 
bg = pygame.image.load("background.jpg")

ex = pygame.image.load("explosion.png") 

bullet = pygame.image.load("bullet.png")


hero = pygame.image.load("spaceship.png")



class player():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.life = 20 
    def draw(self,diffx,diffy):
        self.x += diffx
        self.y += diffy
        if self.x < 0:
            self.x = 0
        if self.x > 740:
            self.x = 740
        if self.y > 540:
            self.y = 540
        win.blit(hero,(self.x,self.y))
    
class Bullet():
    def __init__(self,ship):
        self.x = ship.x+16
        self.y = ship.y+16
        self.state = "ready"
        self.speed = 2
        self.life = 10
    def draw(self,ship):
        if self.state is "fire":
            win.blit(bullet,(self.x,self.y))
            self.y -= self.speed
        if self.y < -30 or self.state is "ready":
            self.state = "ready"
            self.y = ship.y + 16
            self.x = ship.x + 16

class enemy1():
    def __init__(self):
        self.img = pygame.image.load("virus.png")
        self.x = random.randrange(0,800)
        self.y = random.randrange(-600,-200)
        self.speed = 1.4

    def draw(self):
        self.y  += self.speed
        if self.y > 600:
                self.x = random.randrange(0,800)
                self.y = -200
        win.blit(self.img,(self.x,self.y))






class enemy2():
    def __init__(self):
        self.img = pygame.image.load("covid.png")
        self.x = random.randrange(0,800)
        self.y = random.randrange(-600,-200)
        self.speed = 1.2
        self.life = 2
    def draw(self):
        self.y  += self.speed
        if self.y > 600:
                self.x = random.randrange(0,800)
                self.y = -200
        win.blit(self.img,(self.x,self.y))




class sanitizer():
    def __init__(self):
        self.img = pygame.image.load("hand-sanitizer.png")
        self.x = random.randrange(0,800)
        self.y = random.randrange(-600,-200)
        self.speed = 1.2
    def draw(self):
        self.y  += self.speed
        if self.y > 600:
                self.x = random.randrange(0,800)
                self.y = -200
        win.blit(self.img,(self.x,self.y))



class mask():
    def __init__(self):
        self.img = pygame.image.load("face-mask.png")
        self.x = random.randrange(0,800)
        self.y = random.randrange(-600,-200)
        self.speed = 1.2
    def draw(self):
        self.y  += self.speed
        if self.y > 600:
                self.x = random.randrange(0,800)
                self.y = -200
        win.blit(self.img,(self.x,self.y))






def destroy(bt,enm,i):
    global  score
    if bt.y < enm[i].y+60:
        if enm[i].x <= bt.x < enm[i].x+64 or enm[i].x <= bt.x + 32 < enm[i].x + 64 :
            explosion = mixer.Sound('explosion.wav')
            explosion.play()
            bt.state = "ready"
            score += 1
            return True
        return False
    return False




def crash(ship,enm1,enm2,nume):
    for i in range(nume):
        if enm1[i].y+60 > ship.y > enm1[i].y or enm1[i].y+60 > ship.y+60 > enm1[i].y:
            if enm1[i].x <= ship.x < enm1[i].x+60 or enm1[i].x <= ship.x+ 60 < enm1[i].x + 60 :
                ship.life -= 1
                enm1[i].x = random.randrange(0,800)
                enm1[i].y = -200
    for i in range(nume):
        if enm2[i].y+60 > ship.y > enm2[i].y or enm2[i].y+60 > ship.y+60 > enm2[i].y:
            if enm2[i].x <= ship.x < enm2[i].x+60 or enm2[i].x <= ship.x + 60 < enm2[i].x + 60 :
                ship.life -= 2
                enm2[i].x = random.randrange(0,800)
                enm2[i].y = -200
    pygame.draw.rect(win,(255,0,0),(680,10,100,10))
    pygame.draw.rect(win,(0,255,0),(680,10,5*ship.life,10))




def text_objects(text, font):
    textsurface = font.render(text, True, (0,0,0))
    return textsurface, textsurface.get_rect()



def game_over(ship):
    global score
    sc = score
    if ship.life < 0:
        tex = pygame.font.Font('freesansbold.ttf',50)
        text1 ,text_rect1 = text_objects('Game Over',tex)
        text_rect1.center = (400,300)
        text2 ,text_rect2 = text_objects('You Scored:'+str(sc),tex)
        text_rect2.center = (400,350)
        win.blit(text1,text_rect1)
        win.blit(text2,text_rect2)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        quit()
        
       
def get_mask(ship,msk,numh):
    for i in range(numh):
        if ship.y < msk[i].y < ship.y+60 or ship.y < msk[i].y+30 < ship.y+60:
            if ship.x <= msk[i].x < ship.x+60 or ship.x <= msk[i].x+30 < ship.x+ 60 :
                ship.life += 1
                msk[i].x = random.randrange(0,800)
                msk[i].y = -200       



def get_sanitizer(ship,bt,snt,numh):
    for i in range(numh):
      if ship.y < snt[i].y < ship.y+60 or ship.y < snt[i].y+30 < ship.y+60:
            if ship.x <= snt[i].x < ship.x+60 or ship.x <= snt[i].x+30 < ship.x + 60 : 
                bt.life += 2 
                snt[i].x = random.randrange(0,800)
                snt[i].y = -200
    tex = pygame.font.Font('freesansbold.ttf',20)
    text ,text_rect = text_objects('Bullets :'+str(bt.life),tex)
    text_rect.center = (50,40)
    win.blit(text,text_rect)



def show_score():
    global score
    tex = pygame.font.Font('freesansbold.ttf',20)
    text ,text_rect = text_objects('Score :'+str(score),tex)
    text_rect.center = (50,20)
    win.blit(text,text_rect)







########################################################################
#########################################################################
win = pygame.display.set_mode((800,600))
def game():
    pygame.init()
    pygame.display.set_caption("Defeat Covid")
    mixer.music.load('bg1.wav')
    mixer.music.play(-1)
    pygame.display.set_icon(icon)
    ship = player(368,530)
    bt = Bullet(ship)
    nume = 6
    numh = 3
    enm1 = []
    enm2 = []
    msk = []
    snt = []
    for i in range(nume):
        enm1.append(enemy1())
        enm2.append(enemy2())
    for i in range(numh):
        msk.append(mask())
        snt.append(sanitizer())


    running = True
    diffX,diffY = 0,0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

          
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    diffX = -0.8
                if event.key == pygame.K_d:
                    diffX = 0.8
                if event.key == pygame.K_w:
                    diffY = -0.8
                if event.key == pygame.K_s:
                    diffY = 0.8
                if event.key == pygame.K_UP:
                    if bt.life > 0:
                        bullet_sound = mixer.Sound('gun_shot.wav')
                        bullet_sound.play()
                        bt.state = "fire"
                        bt.life -= 1 
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                    diffX,diffY = 0,0
       

        

        

        


       

        
        

        


        win.fill((29,211,189))

       

   #######################################################
        for i in range(nume):
            dt = destroy(bt,enm1,i)
            if dt:
                x = enm1[i].x
                y = enm1[i].y
                enm1[i].x = random.randrange(0,800)
                enm1[i].y = -200
                tick[i] = time.time()
            if(time.time()-tick[i] < 0.5):
                    win.blit(ex,(x + 32, y + 32))
        
        for i in range(nume):
            dt = destroy(bt,enm2,i)
            if dt:
                enm2[i].life -= 1
            if dt and enm2[i].life <= 0:
                enm2[i].life = 2
                x = enm2[i].x
                y = enm2[i].y
                enm2[i].x = random.randrange(0,800)
                enm2[i].y = -200
                tick[nume+i] = time.time()
            if(time.time()-tick[nume+i] < 0.5):
                    win.blit(ex,(x + 32, y + 32))
  #######################################################################      



        show_score()

        crash(ship,enm1,enm2,nume)

        get_mask(ship,msk,numh)

        get_sanitizer(ship,bt,snt,numh)

        for i in range(numh):
            msk[i].draw()
            snt[i].draw()


        for i in range(nume):
            enm1[i].draw()
            enm2[i].draw()


        ship.draw(diffX,diffY)


        bt.draw(ship)


        game_over(ship)


        pygame.display.update()



###########################################################################
############################################################################
w=Tk()
w.title("DEFEAT COVID")
img=PhotoImage(file="bg1.png")
l0=Label(w,image=img);l0.grid(row=1,column=1,rowspan=1,columnspan=2)
b1=Button(w,text=("PLAY"),font=("arial",20,"bold"),command=game);b1.grid(row=1,column=1)
b2=Button(w,text=("COVID 19 INFO"),font=("arial",20,"bold"),command = l);b2.grid(row=1,column=2)
w.mainloop()
    #clock.tick(60)

#######