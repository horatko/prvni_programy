
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
    pozadi = pygame.image.load("prsi_karty/ostatni/pozadi.jpg")
    milos = pygame.image.load("prsi_karty/ostatni/milos.jpeg")

    windows.blit(pozadi,(0,0))
    windows.blit(milos, (300, 100))

    karta=[]
    karty_obr=[]
    karty=balik_karet_plny
    for i in range(2):
         karta.append(select_card(karty))
         print("prsi_karty/karty/"+karta[i]+".jpg")
        # karty_obr[i] = pygame.image.load("karty"+karta[i]+".jpg") 




    while True :

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        
        




        
        




        pygame.display.update()
        clock.tick(60)