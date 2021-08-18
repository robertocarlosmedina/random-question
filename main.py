import pygame 
from pygame.locals import *
from random import randint

screen_size = (700, 420)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Random number generator test')
pygame.init()

#  variables to control the display
stopStartControl = False
showHiddeHelp = True
keep_going = True
font = pygame.font.SysFont("arial", 20)
font_2 = pygame.font.SysFont("arial", 13)
rects=[]
optionsDict = {pygame.K_1:1, pygame.K_2:2,pygame.K_3:4,pygame.K_4:8,pygame.K_5:16,pygame.K_6:32}
nrRandomNumbers = 1
x=30

class Rectangle:
    def __init__(self, x):
        self.color = (0, 255, 0)
        self.widht = 0
        self.height = 0
        self.y = 380
        self.x = x

    def draw(self, screen):
        if(self.widht != 0):
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.widht, self.height))
    
    def setHeight(self):
        self.widht = 4
        self.height += 8
        self.y -= 8

def generateRects(x):
    for _ in range (160):
        rects.append(Rectangle(x))
        x+=4

# Initializating the array of rects
generateRects(x)

#  this will build a string from an array
def stringBuilder(array):
    string = ['']
    mult_of_16 = [16, 32, 48]
    i = 0
    index = 0
    for value in array:
        # control the end of the string
        if(i in mult_of_16):
            index += 1
            string.append('')

        if(i == 0):
            string[index] += f'{value}'
        elif (i == len(array)-1):
            string[index] += f' + {value} = {sum(array)}'
        else:
            string[index] += f' + {value}'
        i+=1

    return string

# this will draw the grafic and also generate the random values
def randomGrafic(nrValues):
    [rectangle.draw(screen) for rectangle in rects]
    if (stopStartControl):
        randomGeneratedValues = []
        screenText = ''
        [randomGeneratedValues.append(randint(0, int(160/nrValues))) for _ in range(nrValues)]
        screenText = stringBuilder(randomGeneratedValues)
        y = 20
        # bliting the text on the screen line by line
        for text in screenText:
            size = pygame.font.Font.size(font,text)
            line = font.render(text, True, (255, 255,255))
            screen.blit(line, (int(screen_size[0]/2-size[0]/2), y))
            y+=20
        # incrementing a value in the rect that as randomly selected
        rects[sum(randomGeneratedValues)-1].setHeight()

# display the informations of the keyboard controls
def keyboardControls():
    infoText = ['List of keyboard controlers: ', '  -> "1": to generate 1 random values', '  -> "2": to generate 2 random values',
         '  -> "3": to generate 4 random values', '  -> "4": to generate 8 random values', '  -> "5": to generate 16 random values',
         '  -> "6": to generate 32 random values', '  -> "ENTER": to start and stop the generator',
         '  -> "BACKSPACE": to reset the values to default','  -> "q": to quit program','  -> "h": to hidde and show this painel',
         ]
    y = 50
    # bliting the text on the screen line by line
    for text in infoText:
        # size = pygame.font.Font.size(font_2,text)
        line = font_2.render(text, True, (255, 255,255))
        screen.blit(line, (20, y))
        y+=15

clock = pygame.time.Clock()

while keep_going:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_q]:
                exit()

            if pygame.key.get_pressed()[pygame.K_RETURN]:
                stopStartControl = not stopStartControl

            if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                rects = []
                generateRects(x)
            
            if pygame.key.get_pressed()[pygame.K_h]:
                showHiddeHelp = not showHiddeHelp

            for key, value in zip(optionsDict.keys(), optionsDict.values()):
                if pygame.key.get_pressed()[key]:
                    nrRandomNumbers = value
                
    screen.fill((25, 25, 25))
    pygame.draw.line(screen, (130, 130, 130), (x, 381), (670, 381), 2)
    randomGrafic(nrValues=nrRandomNumbers)

    if (showHiddeHelp):
        keyboardControls()

    clock.tick(30)
    pygame.display.update()