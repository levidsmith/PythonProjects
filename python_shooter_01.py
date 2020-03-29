import pygame

class Ship:
    x = 640
    y = 600
    w = 64
    h = 64
    
    vel_x = 0
    vel_y = 0
    
    def draw(self, display):
        #Draw Ship
        c = (0, 255, 255)
        pygame.draw.rect(display, c, (self.x, self.y, self.w, self.h))
        
    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y



ship = Ship()


def update():
    ship.update()


def draw(display):
    c = (0, 0, 0)
    display.fill(c)
    ship.draw(display)



def main():
    pygame.init()
    display = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Test Window')

    clock = pygame.time.Clock()

    keepLooping = True
    while keepLooping:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepLooping = False
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                    ship.vel_x = -5
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                    ship.vel_x = 5
                elif (event.key == pygame.K_UP or event.key == pygame.K_w):
                    ship.vel_y = -5
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                    ship.vel_y = 5

        update()
        draw(display)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()
    
main()

