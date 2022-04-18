from operator import truediv
import pygame
import sys
import random






def novy_smer(smer_snake, keys):
    if keys[pygame.K_UP] :
        return "UP" if smer_snake != "DOWN" else smer_snake
    if keys[pygame.K_DOWN] :
        return "DOWN" if smer_snake != "UP" else smer_snake
        
    if keys[pygame.K_LEFT] :
        return "LEFT" if smer_snake != "RIGHT" else smer_snake
    if keys[pygame.K_RIGHT] :
        return "RIGHT" if smer_snake != "LEFT" else smer_snake
    return smer_snake

def zmen_pozici(smer_snake, snake, snake_size):
    snak={}
    if smer_snake=="LEFT":
        snak={"x":snake["x"]-snake_size, "y":snake["y"]}
    if smer_snake=="RIGHT":
        snak={"x":snake["x"]+snake_size, "y":snake["y"]}
        
    if smer_snake=="UP":
        snak={"x":snake["x"], "y":snake["y"]-snake_size}
    if smer_snake=="DOWN":
        snak={"x":snake["x"], "y":snake["y"]+snake_size}
    return snak

def control_position(snake):
    if snake["x"]>=okno[0] :
        return False
    elif snake["x"]<0:
        return False
    elif snake["y"]>=okno[0] :
        return False
    elif snake["y"]<0 :
        return False
    return True

def generate_eat(snake_size, snake, okno):

    x= random.choice(range(0,okno[0],snake_size))
    y= random.choice(range(0,okno[1],snake_size))
    for part in snake:
        if x==part["x"] and y==part["y"]:
            x= random.choice(range(0,okno[0],snake_size))
            y= random.choice(range(0,okno[1],snake_size))
    return {"x":x, "y":y}


def is_collision(snake, eat):
    if snake["x"] == eat["x"] and snake["y"] == eat["y"] :
        return True
    return False
    
def self_colision(snake):
    for part in snake[1:]:
        if snake[0]==part:
            return True
    return False

    


    
        







if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Snake by Jarmen")
    BIGFONT = pygame.font.SysFont("comicsans", 20)
    snake_size=20
    okno=[400,400]
    game_speed=8
    clock = pygame.time.Clock()
    barva_hada=pygame.Color(98,32,98)
    eat_color =pygame.Color(10,150,150)
    okno_hry=pygame.display.set_mode((okno))
    pygame.draw.rect(okno_hry, barva_hada, pygame.Rect(okno[0]/2, okno[1]/2, snake_size, snake_size))

    
    snake_size=20
    snake = [{"x": okno[0]/2 , "y" : okno[1]/2}]
    smer_snake="RIGHT"
    eat = generate_eat(snake_size,snake, okno)
    running=True
    


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        keys= pygame.key.get_pressed()
        smer_snake=novy_smer(smer_snake, keys)
        new_smer=zmen_pozici(smer_snake, snake[0], snake_size)
        snake.insert(0,new_smer)

        if is_collision(snake[0],eat):
            
            eat = generate_eat(snake_size,snake,okno)
        else:
            snake.pop()

        if not control_position(snake[0]):
            
            running=False

            while not running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        
                        if event.key == pygame.K_ESCAPE:
                            snake=[]
                            snake = [{"x": okno[0]/2 , "y" : okno[1]/2}]
                            eat = generate_eat(snake_size,snake,okno)
                            running=True
                            
                else:
                    pygame.display.update()
                    okno_hry.fill(pygame.Color(0,0,0))
                    score = BIGFONT.render(f" SCORE {len(snake)} pro novou hru stiskni ESC", False, (255, 255, 255))
                    okno_hry.blit(score,(10,okno[0]/2))
                    
        if self_colision(snake):
            running=False
            
            while not running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            snake=[]
                            snake = [{"x": okno[0]/2 , "y" : okno[1]/2}]
                            eat = generate_eat(snake_size,snake,okno)
                                                 
                        running=True
                else:
                    pygame.display.update()
                    okno_hry.fill(pygame.Color(0,0,0))
                    score = BIGFONT.render(f" SCORE {len(snake)} pro novou hru stiskni ESC", False, (255, 255, 255))
                    okno_hry.blit(score,(10,okno[0]/2))
                  
                    
                
        
        




        

            



        
        
        #draw snake and window update tick tack
        for part in snake:
            pygame.draw.rect(okno_hry, barva_hada, pygame.Rect(part["x"], part["y"], snake_size, snake_size))
        pygame.draw.rect(okno_hry, eat_color, pygame.Rect(eat["x"], eat["y"], snake_size, snake_size))
        score2 = BIGFONT.render(f" SCORE {len(snake)}", False, (255, 255, 255))
        okno_hry.blit(score2,(10,10))
        
        pygame.display.update()
        okno_hry.fill(pygame.Color(0,0,0))
        clock.tick(game_speed)
        
