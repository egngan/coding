import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

bird_height = 36

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Bouncing Avian')
clock = pygame.time.Clock()

birdImg = pygame.image.load('bird.png')

class Pole:
    pole_width = 70
    def __init__(self, x_pos, y_gap, h_gap):
        self.x_pos = x_pos
        self.y_gap = y_gap
        self.h_gap = h_gap

    def move(self,x_delta):
        self.x_pos += x_delta
        
    def draw(self):
        h_gap2 = self.h_gap*0.5
        y1 = self.y_gap - h_gap2
        y2 = self.y_gap + h_gap2
        pygame.draw.rect(gameDisplay, black, [self.x_pos, y2 , self.pole_width, display_height - y2])
        pygame.draw.rect(gameDisplay, black, [self.x_pos, 0 , self.pole_width, y1])

def things(thingx, y_pass, thingw, h_pass, color):
    y1 = y_pass - h_pass*0.5
    y2 = y_pass + h_pass*0.5
    pygame.draw.rect(gameDisplay, color, [thingx, y2 , thingw, display_height - y2])
    pygame.draw.rect(gameDisplay, color, [thingx, 0 , thingw, y1])

def bird(x,y):
    gameDisplay.blit(birdImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
    

def crash():
    message_display('You Died :(')
    
def game_loop():
    x = (display_width * 0.25)
    y = (display_height * 0.1)

    y_velocity = 0
    x_velocity = -2

    #thing_startx = random.randrange(display_width*0.5, display_width)
    pole_x = display_width*1.1
    h_pass =  random.randrange(60, 150)
    y_pass =  random.randrange(100, display_height)
    #y_pass =  random.randrange(h_pass * 0.5, display_height - h_pass * 0.5)
    thing_speed = 7
    thing_width = 70
    gravity = 0.1
    y_acceleration = gravity
    lift = 0

    poles = [Pole(display_width*1.1,  random.randrange(int(h_pass * 0.5), int(display_height - h_pass * 0.5)), random.randrange(60, 150))]

    gameExit = False
    firstTime = True
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    lift = -0.35


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    lift = 0
        y_acceleration = gravity + lift
        y_velocity += y_acceleration
        y += y_velocity
        gameDisplay.fill(white)
        
        for pole in poles: 
            pole.move(x_velocity)
            pole.draw()
        
        # # things(thingx, thingy, thingw, thingh, color)
        #things(thing_startx, y_pass, thing_width, h_pass, black)
        #thing_starty += thing_speed
        bird(x,y)
        if y > display_height - bird_height or y <= 0:
            crash()

        #pole_x += x_velocity

        #if thing_startx > display_height:
            #thing_startx = 0 - thing_height
            #thing_startx = random.randrange(0,display_width)

        # ####
        # if y < thing_starty+thing_height:
        #     print('y crossover',y,thing_starty)

        #     if x > thing_startx and x < thing_startx + thing_width or x+bird_width > thing_startx and x + bird_width < thing_startx+thing_width:
        #         print('x crossover')
        #         crash()
        # ####
        
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()


