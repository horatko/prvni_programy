
from cgitb import text
import random
from tkinter import *
import pygame
import sys

balik_karet_plny = ["c_desitka_10","z_osma_8","k_spodek_1","l_eso_11", 
                    "z_sedma_7", "z_spodek_1", "c_spodek_1", "k_eso_11", "k_desitka_10"]

#vybrat náhodnou kartu a nevracet ji
def select_card(balicek):
    karta =random.choice(balicek)
    balicek.remove(karta)
    return karta 

def secti_kartu(karta_vstup):
    hodnota_karty=""
    for i in range(len(karta_vstup)):
        if karta_vstup[i].isdigit()==True:
            hodnota_karty+=karta_vstup[i]
    return int(hodnota_karty)

karty=balik_karet_plny
     






if __name__== "__main__" :
    pygame.init()
    clock=pygame.time.Clock()
    windows = pygame.display.set_mode((800, 700))
    pozadi = pygame.image.load("ostatni/pozadi.jpg")
    milos = pygame.image.load("ostatni/milos.jpeg")
    game_font = pygame.font.SysFont("comicsans", 35)
    windows.blit(pozadi,(0,0))
    milos_okno=windows.blit(milos, (300, 10))
    incerment=1

    
    prvni_kolo=2
    """
    dalsi_kolo=1
    karta=[]
    karty_hrac=[]
    karty_milos=[]
    karty=balik_karet_plny

    """
    
    #nacitani prvnich dvou karet hrace
    """
         karty_hrac_pomoc=select_card(karty)
         karty_milos_pomoc=select_card(karty)
         karty_hrac.append(pygame.image.load("karty/"+(karty_hrac_pomoc)+".jpg"))
         karty_milos.append(pygame.image.load("karty/"+(karty_milos_pomoc)+".jpg"))
         score_milos+=secti_kartu(karty_milos_pomoc)
         windows.blit(karty_hrac[i], (300+(i*105), 500))
         windows.blit(karty_milos[i], (250+(i*105), 250)) 
    """
    #score_milos_text = game_font.render(f"Score Miloš {lizni()}", True, (255, 255, 255))
    #windows.blit(score_milos_text,(500,85))
   


    while True :
     

            


        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                    
                    pozice_X=100
                    windows.blit(pygame.image.load("karty/"+(select_card(karty))+".jpg"),   ((pozice_X*incerment),250))
                    incerment+=1
             

        
                
        
        




    




        pygame.display.update()
        clock.tick(60)
