import pygame
import random as r
pygame.init()
gamewindow=pygame.display.set_mode((400,500))
pygame.display.set_caption("first game")
font=pygame.font.SysFont(None,55)

def plot_snake(gamewindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size])

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])

def gameloop():
    snk_list=[]
    snk_length=1
    exit=False
    game_over=False
    snake_x=4
    snake_y=4
    food_x=r.randint(10,370)
    food_y=r.randint(20,490)
    food_size=10
    initial_velx=0
    initial_vely=0
    velocity_x=0
    velocity_y=0
    snake_size=20
    black=(0,0,0)
    white=(255,255,255)
    color1=(122,156,180)
    score=0
    clock=pygame.time.Clock()
    fps=60
    while not exit:
        if game_over:
            gamewindow.fill(white)
            text_screen("Game over",black,100,100)

            for event in pygame.event.get():
                # print(event)
                if event.type==pygame.QUIT:
                    exit=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():    
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=initial_velx+3
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x=initial_velx-3
                        velocity_y=0
                    if event.key==pygame.K_UP:
                        velocity_y=initial_vely-3
                        velocity_x=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=initial_vely+3
                        velocity_x=0

            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y
            if(abs(snake_x-food_x)<10 and abs(snake_y - food_y)<10):
                    score+=1   
                    snk_length+=5
                    # print("score",score*10)     
                    food_x=r.randint(10,370)
                    food_y=r.randint(20,490)
            gamewindow.fill(white)
            text_screen("score"+str(score*10),color1,50,50)
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>(snk_length):
                    del snk_list[0]

            if head in snk_list[:-1]:
                game_over=True
                
            if snake_x<0 or snake_x>400 or snake_y<0 or snake_y>500:
                    game_over =True


            pygame.draw.rect(gamewindow,color1,[food_x,food_y,food_size,food_size])
                # pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(gamewindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

gameloop()