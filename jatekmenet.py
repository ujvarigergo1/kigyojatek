import pygame
import rajzol
import osztalyok
import jatekszamol

def jatek_indul(jatek):
    
    while True:
        jatek = osztalyok.Jatek(jatek.ablak,ketjatekos=jatek.ketjatekos)
        jatek.ablak.bg = pygame.transform.scale(pygame.image.load("media/hatter2.jpg"), (jatek.ablak.x, jatek.ablak.y))  #Eredeti kép letöltve innen: https://pxhere.com/en/photo/1053776 (2019.11.03) (A mérete le lett kicsinyítve mert túl nagy lett volna a file)
        rajzol.hatterrajz(jatek)
        pygame.display.update()
        kilepes=kigyomozog(jatek)
        if kilepes == "vege":
            return kilepes
        if kilepes == "restart":
            continue


def kigyomozog(jatek):
    jatek.alma=jatekszamol.ujalma(jatek.ablak,int((jatek.ablak.y+jatek.ablak.x)/60))
    jatek.kigyofej=osztalyok.Kigyofej(int(jatek.ablak.x/2),int(jatek.ablak.y/2),1,0,int((jatek.ablak.y+jatek.ablak.x)/40),"media/kigyofej.png")
    jatek.farokszunet=(jatek.kigyofej.meret/2)+(jatek.kigyofej.meret/8)
    jatek.kigyofarok=jatekszamol.kezdokigyofarok(jatek)
    pygame.time.set_timer(pygame.USEREVENT, 20)
    if jatek.ketjatekos:
        jatek.kigyofej2=osztalyok.Kigyofej(int(jatek.ablak.x/2)-jatek.farokszunet*10,int(jatek.ablak.y/2),1,0,jatek.kigyofej.meret,"media/kigyofej_kek.png")
        jatek.kigyofarok2=jatekszamol.kezdokigyofarok(jatek,True,szin=(47,169,219))
        jatek.pontszam2=0
    while True:
        event = pygame.event.wait()
        
        if event.type == pygame.USEREVENT:
            jatek = jatekszamol.kigyolepes(jatek)
            jatek = rajzol.jatekterkirajzol(jatek)
            jatek = jatekszamol.almanak_nekimegye(jatek)
            pygame.display.update()
            rajzol.jatektertorol(jatek)
            if jatekszamol.faroknak_nekimegye(jatek) or (jatek.ketjatekos and jatek.kigyofej.rect.colliderect(jatek.kigyofej2.rect)):
                halottkigyo(jatek)
                return "vege"
        visszater = jatekszamol.gombnyomas(jatek,event)
        if visszater == "vege":
            pygame.time.set_timer(pygame.USEREVENT, 0)
            return "vege"
        elif visszater=="restart":
            pygame.time.set_timer(pygame.USEREVENT, 0)
            return "restart"
        else:
            jatek = visszater
        

def halottkigyo(jatek):
    pygame.time.set_timer(pygame.USEREVENT, 0)
    rajzol.halottkigyo_kep(jatek)
    pygame.display.update()
    nev = rajzol.text_input(jatek,int(jatek.ablak.x/2),int(jatek.ablak.y/2),int(jatek.ablak.y/25),color=(255,255,255),maxlen=24)
    jatekszamol.elment(nev,jatek.pontszam,jatekszamol.beolvas())
    if jatek.ketjatekos:
        rajzol.halottkigyo_kep(jatek,True)
        pygame.display.update()
        nev = rajzol.text_input(jatek,int(jatek.ablak.x/2),int(jatek.ablak.y/2),int(jatek.ablak.y/25),color=(255,255,255),maxlen=24)
        jatekszamol.elment(nev,jatek.pontszam2,jatekszamol.beolvas())
    rajzol.TOP10(jatek)
    return