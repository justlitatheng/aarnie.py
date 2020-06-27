# authors: Izzy Charlton and Lucklita Theng
# import needed libraries
import pygame
from random import randint

# initaite PyGame
pygame.init()

# setting colors for later use and the display window for the game
brown = (51, 21, 0)
white = (55, 255, 255)
green = (76, 153, 0)
blue = (0, 50, 128)

# creating a window for the game
display_surface = pygame.display.set_mode((500,500))

# create Character class which includes
# constructor and methods for Aarnie and the insects
class Character:

# constructor for characters
	def __init__(self, x, y, image, size):
		self.x = x
		self.y = y
		self.image = image
		self.size = size

# method to draw and scale the characters onto the screen
	def drawCharacter(self):
		self.image = pygame.image.load(self.image)
		self.image = pygame.transform.scale(self.image, (self.size, self.size))
# attach a rectangle object to the character image
# which allows tracking and movement of characters on screen
		self.imagerect = self.image.get_rect()
		self.imagerect.center = (self.x, self.y)
		display_surface.blit(self.image, self.imagerect)

# method to update the rectangle object within the character image
# according to the changes on the image
	def updateRect(self):
		self.imagerect.center = (self.x, self.y)
		display_surface.blit(self.image, self.imagerect)

# method to get the x-coordinate of the character
	def getX(self):
		return self.x

# method to get the y-coordinate of the character
	def getY(self):
		return self.y

# method to set a new x-coordinate for the character
	def setX(self, n):
		self.x = n

# method to set a new y-coordinate for the character
	def setY(self, n):
		self.y = n

# method to set a new image for the character
	def setImage(self, image):
		self.image = image

# method to get the radius of the size of the character
# to use for calculating distance between two objects
# needed for the collision check method between characters
	def getRadius(self):
		radius = (self.size**(1/2)) // 2
		return radius

# create class Game which includes several objects and methods
class Game:

# constructor of the Game class,
# primarily includes features of the game display
	def __init__(self, x, y, caption, color):
		self.x = x
		self.y = y
		self.caption = caption
		self.color = color

# set method to change color of the window
	def setColor(self, n):
		self.color = n

# method to draw a window for the game
	def drawWin(self):
		pygame.display.set_mode((self.x, self.y))
		pygame.display.set_caption(self.caption)
		display_surface.fill(self.color)

# method to display text inside the window of the game
# includes setting the font, size, color and location of the text
	def displayText(self, string, color, size, x, y):
		font = pygame.font.Font("freesansbold.ttf", size)
		text = font.render(string, True, color)
		textbox = text.get_rect()
		textbox.center = (x, y)
		display_surface.blit(text, textbox)

# method to display a winning screen when the player wins the game,
# which is when Aarnie reaches the top of the screen
	def showWin(self):
		self.color = white
		self.drawWin()
		self.displayText("You win! You freed Aarnie!", brown, 32, 250, 120)
		self.displayText("Press SPACE to start again", green, 25, 250, 180)
# creating Aarnie as an object within the class Character
# to be shown on the winning screen
		aarnie = Character(60, 400, "aarnie.png", 700)
		aarnie.drawCharacter()

# method to display a game-over screen when the player loses the Game
# which is when Aarnie collides with one of the bugs
	def showGameover(self):
		self.color = brown
		self.drawWin()
		self.displayText("Game Over", white, 32, 250, 150)
		self.displayText("Press SPACE to start again!", white, 25, 250, 250)
# creating the insect to appear in the game-over screen
		bug = Character(240, 370, "insect.png", 500)
		bug.drawCharacter()

# method to initiate level 1 of the game
	def level1(self):

# creating aarnie as a character to be played in the game
		aarnie = Character(300, 400, "seedshell.png", 300)
		aarnie.drawCharacter()
		pygame.display.update()
# keeps track of the number of clicks,
# and create condition for clicking to occur
		clickCount = 0
		cracked = False
# get the mouse click and its position so the user can use it to click
# on the seedshell to crack Aarnie free
		click = pygame.mouse.get_pressed()
		mouse = pygame.mouse.get_pos()

# initiating a while loop so user can click until seedshell cracks
		while cracked is False:
			for event in pygame.event.get():

# detecting the mouse click, and keeps track of clicks
				if event.type == pygame.MOUSEBUTTONDOWN:
					clickCount += 1
# sets condition for when the seed will crack (set to 7 clicks by default)
					if clickCount >= 7:
# draws a window for the text to show that seed has cracked, and Aarnie is free
						self.drawWin()
						self.displayText("Yay! Aarnie's free!", white, 25, 250, 250)
						self.displayText("Press SPACE to continue.", white, 25, 250, 150)
						aarnie.setImage("aarnie.png")
						aarnie.drawCharacter()
						pygame.display.update()

# sets condition for user to hit spacebar to continue

				if event.type == pygame.KEYDOWN and clickCount >= 7:
						if event.key == pygame.K_SPACE:
							cracked = True
							self.drawWin()
# sets condition for user to quit by clicking
# upper left window quit button
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

# method for level 2 of the game
	def level2(self):
# create a list of bugs
		bugs = []
		for i in range(4):
			bug = Character(50, 100*(i+1), "insect.png", 200)
			bugs.append(bug)
			bug.drawCharacter()
		return bugs

# method to animate the bugs
	def moveBugs(self, bugs):
# loop to move the bugs by updating the x coordinates
# and using the random integer function from the random library
# for varying speed of the bugs across the screen
		for bug in bugs:
			if bug.getX() < 450:
				ranspeed = randint(2,8)
				bug.setX(bug.getX()+ ranspeed)
			else:
				bug.setX(0)
			bug.updateRect()
		return bugs

# method to get the distance between Aarnie and bugs
# needed for collision check
	def getDist(self, player, bug):
		# the formula of the Euclidean function ((p1 - q1)^2 + (p2 - q2)^2)^(1/2)
		distance = ((player.getX()- bug.getX())**2+(player.getY()-bug.getY())**2)**(1/2)
		return distance

# writing the main function of the game,
# here lies the general structure of the game
def main():
# creating a window
	game = Game(500, 500, "Aarnie's Adventure", blue)
	game.drawWin()

	game.displayText("Aarnie's Adventure", white, 32, 250, 100)
	game.displayText("Keep clicking to free Aarnie!", white, 27, 250, 170)

# calling the function to initiate level one from the class Game
	game.level1()

# setting the condition for level 2 to run
	level2 = True
# calling level 2 objects, Aarnie and the bugs
	bugs = game.level2()
	aarnie = Character(250, 480, "aarnie.png", 350)
	aarnie.drawCharacter()
	aarnie.updateRect()
	pygame.display.update()

# creating a loop for level 2 to run
# and for user to have controls to move Aarnie
	while level2 is True:
		game.setColor(green)
		game.drawWin()
		game.displayText("Help Aarnie escape to the top!", white, 20, 250, 40)
		game.displayText("Press UP, DOWN, LEFT, RIGHT to move Aarnie.", white, 15, 250, 60)
		aarnie.updateRect()
		bugs = game.moveBugs(bugs)

# creating controls for user to move Aarnie up, down, left and right
# to avoid colliding with the bugs
# within the visible parameters of the screen
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP and aarnie.getY() > 10:
					aarnie.setY(aarnie.getY() - 30)

				if event.key == pygame.K_DOWN and aarnie.getY() < 500 :
					aarnie.setY(aarnie.getY() + 30)

				if event.key == pygame.K_LEFT and aarnie.getX() > 0 :
					aarnie.setX(aarnie.getX() - 30)

				if event.key == pygame.K_RIGHT and aarnie.getX() < 400 :
					aarnie.setX(aarnie.getX() + 30)
# allowing the user to quit by closing the window
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		pygame.display.update()
# creating the winning condition for the game
# when Aarnie y-coordinate reaches beyond 70 on the screen (at the top)
		if aarnie.getY() < 70:
			while True:
# display winning window
				game.showWin()
				pygame.display.update()
# creates option for user to play again or they can close the window to end game
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_SPACE:
							main()
					if event.type == pygame.QUIT:
						pygame.quit()
						quit()

# for loop to check for collision between bugs and Aarnie
		for bug in bugs:
			distance = game.getDist(aarnie, bug)
			apart = aarnie.getRadius()+bug.getRadius()
			print(distance, apart)
			if distance <= apart + 20:
				level2 = False

# if there is a collision, the game-over window appears on the screen
	while True:
		game.showGameover()
		pygame.display.update()
# creates option for user to play again or they can close the window to end game
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					main()
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

# running the main function
main()

# quitting pygame library once the main function runs and quitting the game
pygame.quit()
quit()

# CITATIONS:

# Kellen Dorchen helped with understanding classes and objects of the code
# as well as understanding what a "clean code" means in general
# Jackie Chan helped clearing up the clutter of tabs and spaces inconsistency

# Sources that help us understand PyGame:
# "Introduction to PyGame", pythonprogramming.net
# "Changing Class Members in Python", geeksforgeeks.org
# "Using Pygame to move your game character around", opensource.com
# "Properties vs. Getters and Setters", python-course.eu
# "How to Calculate Euclidean Distance", Sciencing.com
# "Rect Collision Response", pygame.org
