
import pygame,sys,random,math
from pygame.locals import*

pygame.init()

infoObject=pygame.display.Info()
screen=pygame.display.set_mode((1600,900))
pygame.display.set_caption("UK Simulator")
clock=pygame.time.Clock()

mapImg=pygame.image.load("UK.png").convert()
mapImg=pygame.transform.scale(mapImg,(800,900))

westImg=pygame.image.load("westeros.png").convert()
westImg=pygame.transform.scale(westImg,(800,900))

worldImg=pygame.image.load("world.png").convert()
worldImg=pygame.transform.scale(worldImg,(1600,900))


font= pygame.font.Font('freesansbold.ttf', 15)##font

size=6
direction=[-size,0,size]


red,black,white,pink=0,0,0,0
redLimit,whiteLimit,blackLimit,pinkLimit=0,0,0,0
numberList=[500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000,10500,11000,11500,12000]


draw=False
drawSize=20


class Human():
    def __init__(self,x,y,colour):
        self.x=x
        self.y=y
        self.colour=colour
        self.count=0
    def draw(self,number):
        global humanList
        #screen.set_at((self.x,self.y),self.colour)
        pygame.draw.rect(screen,self.colour,(self.x,self.y,size,size),0)
        if self.count>=1:
            new=Human((self.x+random.choice(direction)),(self.y+random.choice(direction)),self.colour)
            humanList.append(new)
            self.count=0
            return
        xChange=random.choice(direction)
        yChange=random.choice(direction)
        if screen.get_at((self.x+xChange,self.y+yChange))!=(119,255,107):
            humanList.pop(number)
            return
        self.x+=xChange
        self.y+=yChange
        self.count+=1

class City():
    def __init__(self,x,y,colour):
        self.x=x
        self.y=y
        self.colour=colour
    def draw(self):
        under=screen.get_at((self.x,self.y))
        if under!=self.colour and under!=(119,255,107):
            self.colour=under



        
        pygame.draw.circle(screen,(0,0,0),(self.x,self.y),size*3)
        pygame.draw.circle(screen,self.colour,(self.x,self.y),size*2)

class Grass():
    def __init__(self,x,y):
        self.x=x-drawSize/2
        self.y=y-drawSize/2
    def draw(self):
        pygame.draw.circle(screen,(119,255,107),(round(self.x),round(self.y)),drawSize,0)

        



def drawMap():
    screen.blit(mapImg,(400,0))
    #screen.blit(worldImg,(0,0))
    
    for i in grassList:
        i.draw()
    fpsText=font.render(str(round(clock.get_fps(),1)),True,(0,0,0))
    screen.blit(fpsText,(10,10))
    fpsText=font.render("red: "+str(red)+" white: "+str(white)+" pink: "+str(pink)+" black: "+str(black),True,(255,255,255))
    screen.blit(fpsText,(10,30))


def drawHumans():
    global humanList,red,black,white,pink
    
    red,black,white,pink=0,0,0,0
    number=0
    for i in humanList:
        i.draw(number)
        number+=1
        if i.colour==(255,0,0):
            red+=1
        elif i.colour==(50,50,50):
            black+=1
        elif i.colour==(255,255,255):
            white+=1
        elif i.colour==(255,0,255):
            pink+=1

    for c in cityList:
        c.draw()

        
def myRound(x, base=5):
    return base * round(x/base)


def cities():
    global redLimit,whiteLimit,blackLimit,pinkLimit,cityList

    redList=[]
    pinkList=[]
    whiteList=[]
    blackList=[]
    
    for number in numberList:
        if redLimit<number and red>number:
            for i in humanList:
                if i.colour==(255,0,0):
                    redList.append(i)
            location=random.choice(redList)
            cityList.append(City(location.x,location.y,(255,0,0)))
        elif pinkLimit<number and pink>number:
            for i in humanList:
                if i.colour==(255,0,255):
                    pinkList.append(i)
            location=random.choice(pinkList)
            cityList.append(City(location.x,location.y,(255,0,255)))                
        elif whiteLimit<number and white>number:
            for i in humanList:
                if i.colour==(255,255,255):
                    whiteList.append(i)
            location=random.choice(whiteList)
            cityList.append(City(location.x,location.y,(255,255,255)))
        elif blackLimit<number and black>number:
            for i in humanList:
                if i.colour==(50,50,50):
                    blackList.append(i)
            location=random.choice(blackList)
            cityList.append(City(location.x,location.y,(50,50,50)))

            
    if redLimit<red:
        redLimit=red
    if whiteLimit<white:
        whiteLimit=white
    if blackLimit<black:
        blackLimit=black
    if pinkLimit<pink:
        pinkLimit=pink



humanList=[]
cityList=[]
grassList=[]





setColour=(50,50,50)

mousex,mousey=0,0
down=False

while True:
    screen.fill((79,108,255))
    drawMap()
    drawHumans()
    cities()
    if draw==True and down==True:
        grassList.append(Grass(event.pos[0],event.pos[1]))

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==MOUSEBUTTONUP:
            if draw==False:
                humanList.append(Human(myRound(event.pos[0],size),myRound(event.pos[1],size),setColour))
            down=False   
        elif event.type==MOUSEBUTTONDOWN:
            down=True
        elif event.type==MOUSEMOTION:
            mousex,mousey=event.pos
            
        elif event.type==KEYUP:
            if event.key==K_1:
                setColour=(50,50,50)
                draw=False
            elif event.key==K_2:
                setColour=(255,0,0)
                draw=False
            elif event.key==K_3:
                setColour=(255,255,255)
                draw=False
            elif event.key==K_4:
                setColour=(255,0,255)
                draw=False
            elif event.key==K_5:
                draw=True

    pygame.display.update()
    clock.tick(60)

##Add border map










    
