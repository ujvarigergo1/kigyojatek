import pygame
import math

class Jatek:
    def __init__(self,ablak,kigyofej=None,kigyofarok=None,alma=None,sebesseg=5.5,pontszam=0,elozo=1,
                farokszunet=None,kigyofej2=None,kigyofarok2=None,elozo2=1,pontszam2=0,ketjatekos=False,
                pontszamrect=None,pontszamrect2=None):
        self.ablak = ablak
        self.kigyofej = kigyofej
        self.kigyofarok = kigyofarok
        self.alma = alma
        self.sebesseg = sebesseg
        self.pontszam = pontszam
        self.elozo = elozo
        self.farokszunet = farokszunet
        self.kigyofej2 = kigyofej2
        self.kigyofarok2 = kigyofarok2
        self.elozo2 = elozo2
        self.pontszam2 = pontszam2
        self.ketjatekos = ketjatekos
        self.pontzsmarect=pontszamrect
        self.pontszamrect2 = pontszamrect2

class Iranynev:
    FEL=0
    JOBB=1
    LE=2
    BAL=3

class Eredmeny:
    def __init__(self,nev,pont):
        self.nev = nev
        self.pontszam = pont
    def __str__(self):
        return "{:24} {:04}".format(self.nev.upper(),self.pontszam)

class Pont:
    def __init__(self,x=None,y=None):
        if type(x) is int and type(y) is int:
            self.x = x
            self.y = y
        elif type(x) is float or type(y) is float:
            self.x = int(x)
            self.y = int(y)
        elif type(x) is Pont:
            self.x = x.x
            self.y = x.y
        elif type(x) is Pont and y==None:
            self.x = x.x
            self.y = x.y
        elif x==None and y==None:
            self.x=0
            self.y=0
        else:
            raise ValueError("Hibás bemenet. Kapott típusok: {} és {}".format(type(x),type(y)))
    def __sub__(self,jobb):
        return Pont(self.x - jobb.x, self.y - jobb.y)
    def __div__(self,jobb):
        return Pont(self.x / jobb, self.y / jobb)

        
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)
    def __add__(self,jobb):
        if type(jobb) is Irany:
            return Pont(self.x + jobb.vx, self.y + jobb.vy)
        if type(jobb) is Pont:
            return Pont(self.x + jobb.x, self.y + jobb.y)

        
    

class Irany:
    def __init__(self,vx=None,vy=None):
        if type(vx) is int and vy==None:
            self.irany=vx
            if vx==0:
                self.vx=0
                self.vy=-1
            elif vx==1:
                self.vx=1
                self.vy=0
            elif vx==2:
                self.vx=0
                self.vy=1
            elif vx==3:
                self.vx=-1
                self.vy=0
            else:
                raise ValueError("Hibás bemenet")
        elif type(vx) is int and type(vy) is int:
            self.vx=vx
            self.vy=vy
            if self.vx==1 and self.vy==0:
                self.irany=1
            elif self.vx==-1 and self.vy==0:
                self.irany=3
            elif self.vx==0 and self.vy==1:
                self.irany=2
            elif self.vx==0 and self.vy==-1:
                self.irany=0
            
        else:
            raise ValueError("Hibás bemenet")
        
    def __mul__(self,jobb):
        if type(jobb) is int:
            return Irany(self.vx * jobb, self.vy * jobb)




class Kigyofej:
    def __init__(self,x,y,vx,vy,meret,kephely):
        self.pont = Pont(x,y)
        self.irany = Irany(vx,vy)
        self.meret = meret
        self.kep = pygame.image.load(kephely)
        self.kep = pygame.transform.scale(self.kep, (self.meret, self.meret))
        self.rect = self.kep.get_rect()
class Ablak:
    def __init__(self,kephely,window):
        self.window = window
        self.x = self.window.get_width()
        self.y = self.window.get_height()
        self.bg = pygame.image.load(kephely)
        self.bg = pygame.transform.scale(self.bg, (self.x, self.y))

class Fordulat:
    def __init__(self,x,y,vx,vy):
        self.pont = Pont(x,y)
        self.irany = Irany(vx,vy)

class Kigyofarokresz:
    def __init__(self,x,y,vx,vy,r,iranyok,szin):
        self.szin = szin
        self.pont=Pont(x,y)
        self.irany=Irany(vx,vy)
        self.r = r
        self.iranyok=iranyok
        self.rect=pygame.Rect(x-r,y-r,int(r*2),int(r*2))
class Alma:
    def __init__(self,x,y,meret):
        self.pont = Pont(x,y)
        self.meret = meret
        self.kep = pygame.image.load("media/alma.png")
        self.kep = pygame.transform.scale(self.kep, (self.meret, self.meret))
        self.rect = self.kep.get_rect()