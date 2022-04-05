
import random
import pygame
import sys

balik_karet_plny = ["c_desitka","z_osma","k_spodek","l_eso", 
                    "z_sedma", "z_spodek", "c_spodek", "k_eso", "k_desitka"]

#vybrat náhodnou kartu a nevracet ji
def select_card(balicek):
    karta =random.choice(balicek)
    balicek.remove(karta)
    return karta 

def secti_kartu(karta_vstup):
    hodnota_karty=[]
    for i in range(len(karta_v)):
        if karta_vstup[i] is decimal :
            hodnota_karty+=karta_vstup[i]
    return hodnota_karty


if __name__== "__main__" :
    pygame.init()
    clock=pygame.time.Clock()
    windows = pygame.display.set_mode((800, 700))
    pozadi = pygame.image.load("ostatni/pozadi.jpg")
    milos = pygame.image.load("ostatni/milos.jpeg")

    windows.blit(pozadi,(0,0))
    windows.blit(milos, (300, 10))

    karta=[]
    karty_hrac=[]
    karty_milos=[]
    karty=balik_karet_plny
    #nacitani prvnich dvou karet hrace
    for i in range(2):
         
         karty_hrac.append(pygame.image.load("karty/"+select_card(karty)+".jpg"))
         karty_milos.append(pygame.image.load("karty/"+select_card(karty)+".jpg"))
         windows.blit(karty_hrac[i], (300+(i*105), 500))
         windows.blit(karty_milos[i], (250+(i*105), 250)) 
   

  




    while True :

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        clock.tick_busy_loop()
        




    




        pygame.display.update()
        clock.tick(60)
