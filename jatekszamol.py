import pygame
import osztalyok
import rajzol
import random

def farokmozgat(jatek, kigyofarok):
    for elem in kigyofarok:
        if len(elem.iranyok) != 0:
            if (elem.pont.x == elem.iranyok[0].pont.x and elem.irany.vx == 0 and
                abs(elem.pont.y - elem.iranyok[0].pont.y) < int(jatek.sebesseg)):
                    elem.pont.x += elem.iranyok[0].irany.vx * (int(jatek.sebesseg) - abs(elem.pont.y - elem.iranyok[0].pont.y))
                    elem.pont.y = elem.iranyok[0].pont.y
                    elem.pont = palyaszele(elem.pont, jatek.ablak)
                    elem.irany.vx = elem.iranyok[0].irany.vx
                    elem.irany.vy = elem.iranyok[0].irany.vy
                    elem.iranyok.pop(0)
            elif (elem.irany.vy == 0 and elem.pont.y == elem.iranyok[0].pont.y and
                 abs(elem.pont.x - elem.iranyok[0].pont.x) < int(jatek.sebesseg)):
                    elem.pont.y += elem.iranyok[0].irany.vy * (int(jatek.sebesseg) - abs(elem.pont.x - elem.iranyok[0].pont.x))
                    elem.pont.x = elem.iranyok[0].pont.x
                    elem.pont = palyaszele(elem.pont, jatek.ablak)
                    elem.irany.vx = elem.iranyok[0].irany.vx
                    elem.irany.vy = elem.iranyok[0].irany.vy
                    elem.iranyok.pop(0)
            else:
                    elem.pont.x += elem.irany.vx * int(jatek.sebesseg)
                    elem.pont.y += elem.irany.vy * int(jatek.sebesseg)
                    elem.pont = palyaszele(elem.pont, jatek.ablak)
        else:
            elem.pont.x += elem.irany.vx * int(jatek.sebesseg)
            elem.pont.y += elem.irany.vy * int(jatek.sebesseg)
            elem.pont = palyaszele(elem.pont, jatek.ablak)

    return kigyofarok


def palyaszele(pont, ablak):
    if pont.y < 0:
        pont.y = ablak.y + pont.y
    elif pont.x < 0:
        pont.x = ablak.x + pont.x
    elif pont.y > ablak.y:
        pont.y = abs(ablak.y - pont.y)
    elif pont.x > ablak.x:
        pont.x = abs(ablak.x - pont.x)
    return osztalyok.Pont(pont)


def ujalma(ablak, meret):
    x = random.randint(meret, ablak.x - meret)
    y = random.randint(meret, ablak.y - meret)
    alma = osztalyok.Alma(x, y, meret)
    return alma


def kezdokigyofarok(jatek, masodikkigyoe=False, szin=(143, 216, 39), kigyoeltolas=0, kigyoeltolas2=None, yeltolas=0):
    kigyoeltolas2 = -10 * jatek.farokszunet
    kigyofarok = []
    if masodikkigyoe:
        farokx = int(jatek.ablak.x / 2 - jatek.kigyofej.meret / 4 - jatek.kigyofej.meret / 15) + kigyoeltolas2
    else:
        farokx = int(jatek.ablak.x / 2 - jatek.kigyofej.meret / 4 - jatek.kigyofej.meret / 15) + kigyoeltolas
    for i in range(5):
        iranyok = []
        kigyofarok.append(osztalyok.Kigyofarokresz(int(farokx), int(jatek.ablak.y / 2 + jatek.kigyofej.meret / 2) + yeltolas, 1, 0, jatek.kigyofej.meret / 4, iranyok, szin))
        farokx -= jatek.farokszunet

    return kigyofarok


def kigyolepes(jatek):
    jatek.kigyofej.pont += jatek.kigyofej.irany * int(jatek.sebesseg)
    jatek.kigyofej.pont = palyaszele(jatek.kigyofej.pont + osztalyok.Pont(jatek.kigyofej.meret / 2, jatek.kigyofej.meret / 2), jatek.ablak) - osztalyok.Pont(jatek.kigyofej.meret / 2, jatek.kigyofej.meret / 2)
    if jatek.ketjatekos:
        jatek.kigyofej2.pont += jatek.kigyofej2.irany * int(jatek.sebesseg)
        jatek.kigyofej2.pont = palyaszele(jatek.kigyofej2.pont + osztalyok.Pont(jatek.kigyofej2.meret / 2, jatek.kigyofej2.meret / 2), jatek.ablak) - osztalyok.Pont(jatek.kigyofej2.meret / 2, jatek.kigyofej2.meret / 2)
    jatek.kigyofarok = farokmozgat(jatek, jatek.kigyofarok)
    if jatek.ketjatekos:
        jatek.kigyofarok2 = farokmozgat(jatek, jatek.kigyofarok2)
    return jatek


def gombtoirany(event):
    gombok = (pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT)
    gombok2 = (pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a)
    for i in range(len(gombok)):
        if event.key == gombok[i]:
            return (i, False)
        if event.key == gombok2[i]:
            return (i, True)

    return (None, None)


def gombnyomas(jatek, event):
    if event.type == pygame.KEYDOWN:
        if  event.key == pygame.K_ESCAPE:
            rajzol.hatterrajz(jatek)
            pygame.time.set_timer(pygame.USEREVENT, 0)
            kijelolt = rajzol.menu(['RESUME', 'RESTART', 'MAIN MENU', 'EXIT'], jatek)
            if kijelolt == 3:
                pygame.quit()
            elif kijelolt == 0:
                pygame.time.set_timer(pygame.USEREVENT, 20)
                rajzol.hatterrajz(jatek)
                return jatek
            elif kijelolt == 2:
                return 'vege'
            elif kijelolt == 1:
                pygame.time.set_timer(pygame.USEREVENT, 20)
                return 'restart'
                
        else:
            lenyomott, masikkigyoe = gombtoirany(event)
            if lenyomott != None:
                
                if masikkigyoe and jatek.ketjatekos:
                        kigyofej = jatek.kigyofej2
                        kigyofarok = jatek.kigyofarok2
                        elozo = jatek.elozo2
                else:
                    kigyofej = jatek.kigyofej
                    kigyofarok = jatek.kigyofarok
                    elozo = jatek.elozo
                if abs(kigyofej.irany.vx) != lenyomott % 2 or (jatek.ketjatekos and abs(kigyofej.irany.vy) == lenyomott % 2):
                    kigyofej.irany = osztalyok.Irany(lenyomott)
                    fejforgat(elozo, lenyomott, kigyofej)
                    elozo = lenyomott
                    ujhely = osztalyok.Pont(kigyofej.pont.x + int(kigyofej.meret / 2), kigyofej.pont.y + int(kigyofej.meret / 2))
                    for elem in kigyofarok:
                        elem.iranyok.append(osztalyok.Fordulat(ujhely.x, ujhely.y, kigyofej.irany.vx, kigyofej.irany.vy))

                if abs(kigyofej.irany.vx) != lenyomott % 2 or (jatek.ketjatekos and abs(kigyofej.irany.vy) == lenyomott % 2):
                    kigyofej2.irany = osztalyok.Irany(lenyomott)
                    fejforgat(elozo, lenyomott, kigyofej)
                    elozo = lenyomott
                    ujhely = osztalyok.Pont(kigyofej.pont.x + int(kigyofej.meret / 2), kigyofej.pont.y + int(kigyofej.meret / 2))
                    for elem in kigyofarok:
                        elem.iranyok.append(osztalyok.Fordulat(ujhely.x, ujhely.y, kigyofej.irany.vx, kigyofej.irany.vy))

                if masikkigyoe and jatek.ketjatekos:
                        jatek.kigyofej2 = kigyofej
                        jatek.kigyofarok2 = kigyofarok
                        jatek.elozo2 = elozo
                else:
                    jatek.kigyofej = kigyofej
                    jatek.kigyofarok = kigyofarok
                    jatek.elozo = elozo
    return jatek


def fejforgat(elozoirany, koviirany, kigyofej):
    if elozoirany == osztalyok.Iranynev.FEL:
        if koviirany == osztalyok.Iranynev.JOBB:
            kigyofej.kep = pygame.transform.rotate(kigyofej.kep, -90)
        elif koviirany == osztalyok.Iranynev.BAL:
            kigyofej.kep = pygame.transform.rotate(kigyofej.kep, -90)
            kigyofej.kep = pygame.transform.flip(kigyofej.kep, True, False)
    elif elozoirany == osztalyok.Iranynev.JOBB:
        if koviirany == osztalyok.Iranynev.FEL:
            kigyofej.kep = pygame.transform.rotate(kigyofej.kep, 90)
        elif koviirany == osztalyok.Iranynev.LE:
            kigyofej.kep = pygame.transform.rotate(kigyofej.kep, -90)
    elif elozoirany == osztalyok.Iranynev.LE:
        if koviirany == osztalyok.Iranynev.JOBB:
            kigyofej.kep = pygame.transform.rotate(kigyofej.kep, 90)
        elif koviirany == osztalyok.Iranynev.BAL:
            kigyofej.kep = pygame.transform.rotate(kigyofej.kep, 90)
            kigyofej.kep = pygame.transform.flip(kigyofej.kep, True, False)
    elif elozoirany == osztalyok.Iranynev.BAL:
        if koviirany == osztalyok.Iranynev.FEL:
            kigyofej.kep = pygame.transform.flip(kigyofej.kep, True, False)
            kigyofej.kep = pygame.transform.rotate(kigyofej.kep, 90)
        elif koviirany == osztalyok.Iranynev.LE:
            kigyofej.kep = pygame.transform.flip(kigyofej.kep, True, False)
            kigyofej.kep = pygame.transform.rotate(kigyofej.kep, -90)


def almanak_nekimegye(jatek):
    if jatek.alma.rect.colliderect(jatek.kigyofej.rect):
        if jatek.sebesseg <= jatek.kigyofarok[0].r * 2:
            jatek.sebesseg += 0.25
        jatek.pontszam += 1
        jatek = elkapottalma(jatek, 1)
    elif jatek.ketjatekos:
        if jatek.alma.rect.colliderect(jatek.kigyofej2.rect):
            jatek.pontszam2 += 1
            if jatek.sebesseg <= jatek.kigyofarok[0].r * 2:
                jatek.sebesseg += 0.25
            jatek = elkapottalma(jatek, 2)
    return jatek


def elkapottalma(jatek, kigyoszam):
    rajzol.almadel(jatek.alma, jatek.ablak)
    jatek.alma = ujalma(jatek.ablak, jatek.alma.meret)
    kigyofarokno = jatek.kigyofarok if kigyoszam == 1 else jatek.kigyofarok2
    utolso = kigyofarokno[(len(kigyofarokno) - 1)]
    kigyofarokno.append(osztalyok.Kigyofarokresz(int(utolso.pont.x - utolso.irany.vx * jatek.farokszunet), int(utolso.pont.y - utolso.irany.vy * jatek.farokszunet), utolso.irany.vx, utolso.irany.vy, kigyofarokno[0].r, list(kigyofarokno[(len(kigyofarokno) - 1)].iranyok), kigyofarokno[0].szin))
    jatek.kigyofarok if kigyoszam == 1 else jatek.kigyofarok2 == kigyofarokno
    return jatek


def faroknak_nekimegye(jatek):
    for elem in jatek.kigyofarok[2:]:
        if elem.rect.colliderect(jatek.kigyofej.rect) or jatek.ketjatekos and elem.rect.colliderect(jatek.kigyofej2.rect):
            return True

    if jatek.ketjatekos:
        for elem in jatek.kigyofarok2[2:]:
            if elem.rect.colliderect(jatek.kigyofej.rect) or elem.rect.colliderect(jatek.kigyofej2.rect):
                return True

    return False


def elment(nev, pontszam, dicsoseglista):
    dicsoseglista.append(osztalyok.Eredmeny(nev, pontszam))
    dicsoseglista.sort(key=(lambda x: x.pontszam), reverse=True)
    while len(dicsoseglista) > 10:
            dicsoseglista.pop()

    with open('dicsoseglista.txt', 'w') as (f):
        for elem in dicsoseglista:
            f.write('{},{}\n'.format(elem.nev, elem.pontszam))


def beolvas():
    dicsoseglista = []
    try:
        with open('dicsoseglista.txt') as (f):
            for line in f:
                try:
                    line = line.rstrip('\n')
                    line = line.split(',')
                    dicsoseglista.append(osztalyok.Eredmeny(line[0], int(line[1])))
                except:
                    print('Hibás file')

    except:
        print('A file nem letezik')

    return dicsoseglista
