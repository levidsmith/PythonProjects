#2020 Levi D. Smith - levidsmith.com
#Displays various drawing primitives (line, rectangle, circle)
import pygame

pygame.init()
display = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Test Window')


clock = pygame.time.Clock()


keepLooping = True
while keepLooping:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepLooping = False

    #Draw Line
    c = (255, 0, 0)
    pygame.draw.line(display, c, (50, 50), (100, 100), 5)
    
    #Draw Rectangle
    c = (0, 255, 0)
    pygame.draw.rect(display, c, (150, 50, 50, 50))
    
    #Draw Circle
    c = (0, 255, 255)
    pygame.draw.circle(display, c, (250, 75), 25)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

