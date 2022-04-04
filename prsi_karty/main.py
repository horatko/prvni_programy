
import random
import pygame
import sys

balik_karet_plny = ["c_desitka","z_osma","k_spodek","l_eso"]

#vybrat náhodnou kartu a nevracet ji
def select_card(balicek):
    karta =random.choice(balicek)
    balicek.remove(karta)
    return karta 



if __name__== "__main__" :
    pygame.init()
    clock=pygame.time.Clock()
    windows = pygame.display.set_mode((800, 800))
    pozadi = pygame.image.load("ostatni/pozadi.jpg")
    milos = pygame.image.load("ostatni/milos.jpeg")

    windows.blit(pozadi,(0,0))
    windows.blit(milos, (300, 100))

    karta=[]
    karty_obr=[]
    karty=balik_karet_plny
    #nacitani prvnich dvou karet hrace
    for i in range(2):
         karta.append("karty/"+select_card(karty)+".jpg")
         karty_obr.append(pygame.image.load(karta[i]))
         
         windows.blit(karty_obr[i], (300+(i*200), 500)) 
   

  




    while True :

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        clock.tick_busy_loop()
        




        
        




        pygame.display.update()
        clock.tick(60)
