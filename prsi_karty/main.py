from cgitb import text
import random


import pygame
import sys
import os

balik_karet_plny =os.listdir("karty")
 
                   

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
    


     






def main() :
     karty=balik_karet_plny
     pygame.init()
     clock=pygame.time.Clock()
     windows = pygame.display.set_mode((800, 700))
     pozadi = pygame.image.load("ostatni/pozadi.jpg")
     milos = pygame.image.load("ostatni/milos.jpeg")
     game_font = pygame.font.SysFont("comicsans", 35)
     windows.blit(pozadi,(0,0))
     karty_hrac=[]
     karty_milos=[]
     neprohra=True
     milos_okno=windows.blit(milos, (300, 10))
     celkove_score_milos=0
     celkove_skore_hrac=0
    
     score_hrac=0
     score_milos=0
     running=True
     nova_hra=True

    
     
 

     while running :
         

        
     

                


            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    
                        if event.key==pygame.K_SPACE:
                            if neprohra:
                        
                
                                incerment=0
                                karty_hrac_pomoc=select_card(karty)
                                karty_hrac.append(karty_hrac_pomoc)
                                score_hrac+=secti_kartu(karty_hrac_pomoc)
                                pozice_X=100
                                windows.blit(pozadi,(0,0))
                                for karta in karty_hrac:
                            
                                    windows.blit(pygame.image.load("karty/"+(karta)),   ((pozice_X+(pozice_X*incerment),500)))
                                    incerment+=1
                                if score_hrac>21 :
                                    celkove_score_milos+=celkove_score_milos
                                    prohra = game_font.render(f"Přejel jsi ", True, (255, 255, 255))
                                    windows.blit(prohra,(250,450))
                                    neprohra=False
                                
                        if event.key==pygame.K_KP_ENTER:
                            neprohra=False
                            
                            while score_milos <=21 and score_milos<score_hrac :
                                
                                incerment_milos=0
                                karty_milos_pomoc=select_card(karty)
                                karty_milos.append(karty_milos_pomoc)
                                score_milos+=secti_kartu(karty_milos_pomoc)
                                pozice_X=100
                                windows.blit(pozadi,(0,0))
                                for kart in karty_milos:
                            
                                    windows.blit(pygame.image.load("karty/"+(kart)),   ((pozice_X+(pozice_X*incerment_milos),200)))
                                    incerment_milos+=1
                                    
                                if score_milos>21 :
                                    celkove_skore_hrac+=1
                                    prohra = game_font.render(f"Přejel Miloš ", True, (255, 255, 255))
                                    celkove_skore_hrac+=1
                                    windows.blit(prohra,(600,10))
                                if score_milos>=score_hrac and score_milos<=21 :
                                    vyhra = game_font.render(f"Vyhrál Miloš ", True, (255, 255, 255))
                                    celkove_score_milos+=1
                                    windows.blit(vyhra,(600,10))
                        if event.key==pygame.K_ESCAPE:
                            main()            

                
                        
                    

        
        




    



            milos_okno=windows.blit(milos, (300, 10))
            score_hrac_text = game_font.render(f"Score Hráč {score_hrac}", True, (255, 255, 255))
            celkove_score_hrac_text = game_font.render(f"{celkove_skore_hrac}", True, (255, 255, 255))
            score_milos_text = game_font.render(f"Score Miloš {score_milos}", True, (255, 255, 255))
            windows.blit(score_hrac_text,(400,400))
            windows.blit(celkove_score_hrac_text,(370,400))

            windows.blit(score_milos_text,(50,10))
                
            pygame.display.flip()
            clock.tick(60)
main()
