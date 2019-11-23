#Authors: Izzy Charlton and Lucklita Theng
#Import library and initiate it

import pygame
pygame.init()

#Create Player and Enemy classes
class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y

# Sets, scales and draws the player and enemies onto the game window
    def drawImage(self, image, xscale, yscale):
        self.image = image
        self.xscale = xscale
        self.yscale = yscale
        self.sprite = pygame.image.load(self.image)
        self.transformed = pygame.transform.scale(self.sprite, (self.xscale, self.yscale))
        return gameDisplay.blit(self.transformed), (self.x, self.y))

# Creating player movement controls for Level 2

    def movePlayer(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == ord('w'):
                    print('jump')

                if event.key == ord('esc'):
                    pygame.quit()
                    menu()

class Enemy:

    player = Player()

    def __init__(x, y, image):
        self.x = x
        self.y = y
        self.picture = picture

    def move(dy):
        self.y = dy + self.y
        return self.y

def level1():

    player = Player()

    display_width = 500
    display_height = 500

    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Grow Up!")

    brown = (51, 21, 0)
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (76, 153, 0)

    def seedshell():
        gameDisplay.blit(player.setImage("seedshell.png", 200, 200), (170, 200))

    def maintext():
        display_surface = pygame.display.set_mode((display_width, display_height))
        font = pygame.font.Font("freesansbold.ttf", 20)
        text = font.render("Keep clicking to crack the seed!", True, white, brown)
        gameDisplay.fill(brown)
        seedshell()
        textbox = text.get_rect()
        textbox.center = (250, 150)
        display_surface.blit(text, textbox)

    maintext()
    pygame.display.update()

    def cracking():

        def crackedtext():
            display_surface = pygame.display.set_mode((display_width, display_height))
            font = pygame.font.Font("freesansbold.ttf", 20)
            text = font.render("You cracked the seed! Press SPACE to continue.", True, white, brown)
            gameDisplay.fill(brown)
            seedshell()
            textbox = text.get_rect()
            textbox.center = (250, 150)
            display_surface.blit(text, textbox)

        clickCount = 0
        cracked = False

        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()

        while cracked is False:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickCount += 1
                    print(clickCount)
                if clickCount >= 20:
                    seed()
                    pygame.display.update()
                    crackedtext()


def level2():

    player = Player()

    enemy1 = Enemy(0, 100)
    enemy1.setImage("insect.png", 200, 200)
    for i in range(100):
        enemy1.move(1)

    enemy2 = Enemy(0, 200)
    enemy2.setImage("insect.png", 200, 200)
    for i in range(100):
        enemy1.move(1)

    enemy3 = Enemy(0, 300)
    enemy1.setImage("insect.png", 200, 200)
    for i in range(100):
        enemy1.move(1)

    enemy4 = Enemy(0, 400)
    enemy1.setImage("insect.png", 200, 200)
    for i in range(100):
        enemy1.move(1)

    display_width = 500
    display_height = 500
    gameDisplay = pygame.display.set_mode((display_width, display_height))

    player.setImage("aarnie.png", 200, 200)

    gameDisplay.blit(sprite, sprite_rect)
    pg.display.flip()



def main():
    close = False
    while not close:
        level2()
main()

pygame.quit()
quit()
