import pygame
import ctypes
import osztalyok
import rajzol
import jatekmenet
import jatekszamol

def main():
    jatek = osztalyok.Jatek(alap())

    while True:
        if jatek.ablak == None:
            jatek.ablak = alap()
        rajzol.hatterrajz(jatek)
        kijelolt=rajzol.menu(["1 PLAYER","2 PLAYER","TOP 10","EXIT"],jatek)
        
        if kijelolt==0:
            jatek.ketjatekos = False
            jatekmenet.jatek_indul(jatek)
            jatek.ablak=None
        elif kijelolt==1:
            jatek.ketjatekos = True
            jatekmenet.jatek_indul(jatek)
            jatek.ablak=None
        elif kijelolt==2:
            rajzol.TOP10(jatek)
        elif kijelolt==3:
            pygame.quit()
            break

def alap():
    pygame.init()

    #Ez a három sor a kápernyő pontos felbontását álítja be. Enélküll rosszul jelenik meg a kép.
    #Az kódrészletet itt találtam: https://gamedev.stackexchange.com/questions/105750/pygame-fullsreen-display-issue (2019.11.11)
    ctypes.windll.user32.SetProcessDPIAware()
    true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
    window = pygame.display.set_mode(true_res,pygame.FULLSCREEN)
    
    logo = pygame.image.load("media/ikon.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption('Kígyó játék')
    return osztalyok.Ablak("media/hatter1.jpg",window)
    #Eredeti kép letöltve innen: https://pxhere.com/en/photo/1057578 (2019.11.03) (A mérete le lett kicsinyítve mert túl nagy lett volna a file)


main()
