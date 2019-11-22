import pygame
import jatekszamol
import osztalyok

def hatterrajz(jatek):
    
    jatek.ablak.window.blit(jatek.ablak.bg,jatek.ablak.bg.get_rect())

def menu(menupontok,jatek,alapertelmezett=0,leptetheto=[0,None],btip='freesansbold.ttf'):
    if leptetheto[1]==None:
        leptetheto[1]=len(menupontok)
    kijelolt=alapertelmezett
    while True:
        
        for i in range(0,len(menupontok)):
            if i==kijelolt:
                color=(0,255,0)
            else:
                color=(255,255,255)
            szoveg(str(menupontok[i]),jatek,jatek.ablak.x/2,int((jatek.ablak.y/2)-(len(menupontok)*60/2)+(60*i)),40,color,btip)
            pygame.display.update()

            
        event = pygame.event.wait()
        if event.type==pygame.KEYDOWN:
            if leptetheto[0] != leptetheto[1]:
                if event.key==pygame.K_DOWN:
                    if kijelolt+1>leptetheto[1]-1:
                        kijelolt=leptetheto[0]
                    else:
                        kijelolt+=1
                    continue
                
                elif event.key==pygame.K_UP:
                    if kijelolt-1<leptetheto[0]:
                        kijelolt=leptetheto[1]
                    kijelolt-=1
            if event.key==pygame.K_RETURN:
                return kijelolt

def szoveg(felirat,jatek,x=0,y=0,size=40,color=(255, 255, 255),btip='freesansbold.ttf'):
    font = pygame.font.Font(btip, int(size)) 
    text = font.render(felirat, True, color) 
    textRect = text.get_rect()
    textRect.center = (x , y) 
    jatek.ablak.window.blit(text,textRect)
    return textRect

def jatekterkirajzol(jatek):
    jatek.kigyofarok = farok(jatek.ablak,jatek.kigyofarok)
    jatek.kigyofej.rect = jatek.ablak.window.blit(jatek.kigyofej.kep,(jatek.kigyofej.pont.x,jatek.kigyofej.pont.y))
    jatek.alma.rect = jatek.ablak.window.blit(jatek.alma.kep,(jatek.alma.pont.x,jatek.alma.pont.y))
    jatek = pontszam_kirajzol(jatek)
    if jatek.ketjatekos:
        jatek.kigyofarok2 = farok(jatek.ablak,jatek.kigyofarok2)
        jatek.kigyofej2.rect = jatek.ablak.window.blit(jatek.kigyofej2.kep,(jatek.kigyofej2.pont.x,jatek.kigyofej2.pont.y))
    return jatek


def jatektertorol(jatek):
    farokdel(jatek.kigyofarok,jatek.ablak)
    kigyofejdel(jatek.ablak,jatek.kigyofej)
    almadel(jatek.alma,jatek.ablak)
    pontszamdel(jatek)
    if jatek.ketjatekos:
        farokdel(jatek.kigyofarok2,jatek.ablak)
        kigyofejdel(jatek.ablak,jatek.kigyofej2)

def farok(ablak,kigyofarok):
    for elem in kigyofarok:
        elem.rect = pygame.draw.circle(ablak.window, elem.szin, (elem.pont.x,elem.pont.y),int(elem.r))
    return kigyofarok

def pontszam_kirajzol(jatek):
    jatek.pontszamrect = szoveg("Pontszám: {}".format(jatek.pontszam),jatek, int(jatek.ablak.x/10
    ) if jatek.ketjatekos else int(jatek.ablak.x/2),int(jatek.ablak.y/25),int(jatek.ablak.y/20),jatek.kigyofarok[0].szin)
    if jatek.ketjatekos:
        jatek.pontszamrect2 = szoveg("Pontszám: {}".format(jatek.pontszam2),jatek, int(jatek.ablak.x/10*9),int(jatek.ablak.y/25),int(jatek.ablak.y/20),jatek.kigyofarok2[0].szin)
    return jatek

def bgdel(bg,x,y,w,h,ablak):
    ablak.window.blit(ablak.bg, (x, y), pygame.Rect((x, y), (w, h)))


def pontszamdel(jatek):
    jatek.ablak.window.blit(jatek.ablak.bg,(jatek.pontszamrect.x,jatek.pontszamrect.y),jatek.pontszamrect)
    if jatek.ketjatekos:
        jatek.ablak.window.blit(jatek.ablak.bg,(jatek.pontszamrect2.x,jatek.pontszamrect2.y),jatek.pontszamrect2)

def almadel(alma,ablak):
    bgdel(ablak.bg,alma.pont.x,alma.pont.y,alma.meret,alma.meret,ablak)

def kigyofejdel(ablak,kigyofej):
    bgdel(ablak.bg,kigyofej.pont.x,kigyofej.pont.y,kigyofej.meret,kigyofej.meret,ablak)

def farokdel(kigyofarok,ablak):
    for elem in kigyofarok:
        bgdel(ablak.bg,elem.pont.x-elem.r,elem.pont.y-elem.r,elem.r*2,elem.r*2,ablak)


def halottkigyo_kep(jatek,masodike=False):
    hatterrajz(jatek)
    betumeret=int(jatek.ablak.y/25)
    tajekoztato_uzenet = "(MAX 24 CHARACTER)" if not jatek.ketjatekos else("(BLUE PLAYER) (MAX 24 CHARACTER)" if masodike else "(GREEN PLAYER) (MAX 24 CHARACTER)")
    szoveg("GAME OVER",jatek,int(jatek.ablak.x/2),int(jatek.ablak.y/2)-betumeret*5,betumeret*3)
    szoveg("TYPE YOUR NAME HERE:",jatek,int(jatek.ablak.x/2),int(jatek.ablak.y/2)-betumeret,betumeret,jatek.kigyofarok2[0].szin if masodike else jatek.kigyofarok[0].szin)
    szoveg(tajekoztato_uzenet,jatek,int(jatek.ablak.x/2),int(jatek.ablak.y/2)+betumeret,int(betumeret/2))
    szoveg("_",jatek,int(jatek.ablak.x/2),int(jatek.ablak.y/2),betumeret)
    szoveg("PRESS ENTER TO CONTINUE",jatek,int(jatek.ablak.x/2),jatek.ablak.y-betumeret*2,int(betumeret/2),color=(143,216,39))
    pontszam_kirajzol(jatek)
    kigyofejwin = osztalyok.Kigyofej(int(jatek.ablak.x/2),int(jatek.ablak.y/3*2),1,0,int((jatek.ablak.y+jatek.ablak.x)/40),"media/kigyofej.png")
    kigyofarokwin = jatekszamol.kezdokigyofarok(jatek,yeltolas=jatek.ablak.y/6)
    
    if jatek.ketjatekos:
        kigyofejwin2= osztalyok.Kigyofej(int(jatek.ablak.x/6*5),int(jatek.ablak.y/2),1,0,int((jatek.ablak.y+jatek.ablak.x)/40),"media/kigyofej_kek.png")
        kigyofarokwin2 = jatekszamol.kezdokigyofarok(jatek,kigyoeltolas=(jatek.ablak.x/3),szin=(47,169,219))
        kigyofejwin = osztalyok.Kigyofej(int(jatek.ablak.x/4),int(jatek.ablak.y/2),1,0,int((jatek.ablak.y+jatek.ablak.x)/40),"media/kigyofej.png")
        kigyofarokwin = jatekszamol.kezdokigyofarok(jatek,kigyoeltolas=(-jatek.ablak.x/4))
        farok(jatek.ablak,kigyofarokwin2)
        jatek.ablak.window.blit(kigyofejwin2.kep,(kigyofejwin2.pont.x,kigyofejwin2.pont.y))
    farok(jatek.ablak,kigyofarokwin)
    jatek.ablak.window.blit(kigyofejwin.kep,(kigyofejwin.pont.x,kigyofejwin.pont.y))
    if not jatek.ketjatekos:
        koronat_felrak(jatek,kigyofejwin)
    elif jatek.pontszam > jatek.pontszam2:
        koronat_felrak(jatek,kigyofejwin)
    elif jatek.pontszam < jatek.pontszam2:
        koronat_felrak(jatek,kigyofejwin2)
    elif jatek.pontszam == jatek.pontszam2:
        koronat_felrak(jatek,kigyofejwin)
        koronat_felrak(jatek,kigyofejwin2)

def text_input(jatek,x,y,size,color=(255,255,255),maxlen=20):
    beirt=[]
    while True:
        event = pygame.event.wait()
        if event.type==pygame.KEYDOWN:
            event
            if event.key==pygame.K_RETURN:
                return "".join(beirt)
            if event.key==pygame.K_BACKSPACE:
                beirt=beirt[:-1]
            elif len(beirt) < maxlen:

                beirt.append(event.unicode.upper())
            szovegrect= szoveg("".join(beirt),jatek,x,y,size,color,btip='media/MonospaceBold.ttf')#https://www.wfonts.com/font/monospace (2019.11.11)
            
            
            pygame.display.update()
            jatek.ablak.window.blit(jatek.ablak.bg, (szovegrect.x, szovegrect.y), szovegrect)


def koronat_felrak(jatek, kigyofejwin):
    korona = pygame.image.load("media/korona.png")
    korona = pygame.transform.scale(korona, (jatek.kigyofej.meret, jatek.kigyofej.meret))
    jatek.ablak.window.blit(korona,pygame.Rect(kigyofejwin.pont.x,kigyofejwin.pont.y - kigyofejwin.meret/7*6,kigyofejwin.meret,kigyofejwin.meret))


def TOP10(jatek):
    hatterrajz(jatek)
    listafile=jatekszamol.beolvas()
    dicsoseglista=[]
    for i in range(10):
        try:
            dicsoseglista.append(listafile[i])
        except:
            dicsoseglista.append(osztalyok.Eredmeny("------",0))
    
    kijelolt = menu(dicsoseglista+["BACK TO MAIN MENU","DELETE ALL"],jatek,10,[10,12],'media/MonospaceBold.ttf')  #https://www.wfonts.com/font/monospace (2019.11.11)
    if kijelolt==10:
        return "vege"
    elif kijelolt==11:
        
        hatterrajz(jatek)
        if  menu(["ARE YOU SURE YOU DELETE HIGHSCORES?","YES","NO"],jatek,1,[1,3]) == 1:
            with open("dicsoseglista.txt","w") as f:
                f.write("")

        if TOP10(jatek) == "vege":
            return