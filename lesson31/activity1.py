import pygame 

pygame.init()
sceen = pygame.display.set_mode((400,300))
done = False

while not done:
    for event in pygame.event.grt():
        if event.typr == pygame.QUIT:
            done = True

    pygame.draw.rect(sceen, (0, 125, 255). pygame.Rect(30, 30, 60, 60))
    
    pygame.display.flip()