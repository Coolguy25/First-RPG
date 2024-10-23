import pygame

pygame.init()

#const

white = (255,255,255)
black = (0,0,0)

run = True

height , width = 800,600 

# screen 

win = pygame.display.set_mode((height,width))



while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    #clear the screen
    win.fill(black)
     

    # flip() updates the screen to make our changes visible
    pygame.display.update()
 
pygame.quit()