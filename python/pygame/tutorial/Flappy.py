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
bird_width = 52

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Bouncing Avian')
clock = pygame.time.Clock()

birdImg = pygame.image.load('bird.png')

class Pole:
    pole_width = 70
    def __init__(self, x_pos, gap_position, gap_height):
        self.x_pos = x_pos
        self.gap_position = gap_position
        self.gap_height = gap_height

    def move(self,x_delta):
        self.x_pos += x_delta
        
    def draw(self, pole_colour):
        gap_height_half = self.gap_height*0.5
        y1 = self.gap_position - gap_height_half
        y2 = self.gap_position + gap_height_half
        pygame.draw.rect(gameDisplay, pole_colour, [self.x_pos, y2 , self.pole_width, display_height - y2])
        pygame.draw.rect(gameDisplay, pole_colour, [self.x_pos, 0 , self.pole_width, y1])

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
    bird_x = (display_width * 0.25)
    bird_y = (display_height * 0.1)

    y_velocity = 0
    x_velocity = -2
    gravity = 0.1
    y_acceleration = gravity
    lift = 0
    pole_x_position = display_width*1.1
    pole_gap_height = random.randrange(100, 150)
    pole_gap_position = random.randrange(int(pole_gap_height * 0.5), int(display_height - pole_gap_height * 0.5))

    poles = [Pole(pole_x_position, pole_gap_position, pole_gap_height)]
    pole_colour = black

    gameExit = False
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
        bird_y += y_velocity
        gameDisplay.fill(white)
        
        for pole in poles: 
            pole.move(x_velocity)
            pole.draw(pole_colour)
        
        # # things(thingx, thingy, thingw, thingh, color)
        #things(thing_startx, y_pass, thing_width, h_pass, black)
        #thing_starty += thing_speed
        bird(bird_x,bird_y)

        #bird will crash if it touched the top and bottom of the pole gap
        pole_gap_height_half = pole_gap_height*0.5
        gap_top = pole_gap_position - pole_gap_height_half
        gap_bottom = pole_gap_position + pole_gap_height_half
        avoid_hitting_top = bird_y > gap_top
        avoid_hitting_bottom = (bird_y + bird_height) < gap_bottom
        can_pass_through = avoid_hitting_top and avoid_hitting_bottom
        if bird_y > display_height - bird_height or bird_y <= 0:
            crash()
        # the bird won't crash before and after pole
        bird_front = bird_x + bird_width
        pole_front = pole.x_pos
        bird_back = bird_x
        pole_back = pole.x_pos + pole.pole_width
        if (bird_front >= pole_front) and (bird_back <= pole_back) and not can_pass_through:
            crash()

        if not can_pass_through:
            pole_colour = red 
        else:
            pole_colour = black

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


