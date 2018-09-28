import pygame, sys, random
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS
#import keyboard


pygame.init()

clock = pygame.time.Clock()

blob = pygame.image.load('images/img1.jpg')

windowWidth = 800
windowHeight = 800
#playerX = 10.0
#playerY = 10.0
#playerVX = 30.0
#playerVY = 20.0
#rectXmv = 1
#rectYmv = 1

# Square Variables
#playerSize = 200
#playerX = (windowWidth / 2) - (playerSize / 2)
#playerY = windowHeight - playerSize
#playerVX = 1]
#
#playerVY = 0
#jumpHeight = 25.0
#moveSpeed = 1.0
#maxSpeed = 10.0
#gravity = 1.0
playerSize = 400
playerX = (windowWidth / 2) - (playerSize / 2)
playerY = windowHeight - playerSize
playerVX = 1.0
playerVY = 0.0
jumpHeight = 25.0
moveSpeed = 1.0
maxSpeed = 10.0
gravity = 1.0





# Keyboard Variables
leftDown = False
rightDown = False
haveJumped = False

def quitgame():
	pygame.quit()
	sys.exit()
	
def move():

	global playerX, playerY, playerVX, playerVY, haveJumped, gravity

	# Move left 
	if leftDown:
		#If we're already moving to the right, reset the moving speed and invert the direction
		if playerVX > 0.0:
			playerVX = moveSpeed
			playerVX = -playerVX	
		# Make sure our square doesn't leave our window to the left
		if playerX > 0:
			playerX += playerVX	

	# Move right
	if rightDown:
		# If we're already moving to the left reset the moving speed again
		if playerVX < 0.0:
			playerVX = moveSpeed
		# Make sure our square doesn't leave our window to the right
		if playerX + playerSize < windowWidth:
			playerX += playerVX

	if playerVY > 1.0:
		playerVY = playerVY * 0.9
	else :
		playerVY = 0.0
		haveJumped = False

	# Is our square in the air? Better add some gravity to bring it back down!
	if playerY < windowHeight - playerSize:
		playerY += gravity
		gravity = gravity * 1.1
	else :
		playerY = windowHeight - playerSize
		gravity = 1.0

	playerY -= playerVY

	if playerVX > 0.0 and playerVX < maxSpeed or playerVX < 0.0 and playerVX > -maxSpeed:
		if haveJumped == False:
			playerVX = playerVX * 1.1

window = pygame.display.set_mode( (windowWidth, windowHeight) ) #creating a surface
pygame.display.set_caption('Pygame Keyboard!')
direction = 1
while True:
	window.fill((0,0,0))
	#put an if just here
	pygame.draw.rect(window, (60, 209, 37), (playerX, playerY, playerVX, playerVY), 20)
	#if playerX > 800:
	#	direction = -1
	#if playerX < 0:
	#	direction = 1
	#playerX += direction * random.randint(1, 10)
	#if playerY > 800:
	#	direction = -1
	#if playerX < 0:
	#	direction = 1 * random.randint(1, 10)
	playerY += direction
	#rectY += direction
	 #location, colour
	#rectX = rectX + 1
	#rectEndX += 1
	#rectEndY += 1
	pygame.draw.ellipse(window, (232, 62, 130), (300, 10, 50, 20))
	pygame.draw.lines(window, (60, 209, 37), False, [(100, 100), (50, 100), (50, 300), (100, 300)], 3)
	pygame.draw.lines(window, (60, 209, 37), False, [(50, 200), (80, 200)], 3)
	pygame.draw.lines(window, (60, 209, 37), False, [(150, 100), (150, 300), (200, 300)], 3)
	pygame.draw.lines(window, (60, 209, 37), False, [(250, 100), (250, 300), (300, 300)], 3)
	pygame.draw.lines(window, (60, 209, 37), False, [(350, 100), (400, 200), (400, 300)], 3)
	pygame.draw.lines(window, (60, 209, 37), False, [(450, 100), (400, 200)], 3)
	window.blit(blob, (playerX, playerY, playerSize, playerSize))
		# Get a list of all events that happened since the last redraw
	for event in GAME_EVENTS.get():

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_LEFT:
				leftDown = True
			if event.key == pygame.K_RIGHT:
				rightDown = True
			if event.key == pygame.K_UP:
				if not haveJumped:
					haveJumped = True
					playerVY += jumpHeight
			if event.key == pygame.K_ESCAPE:
				quitGame()

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				leftDown = False
				playerVX = moveSpeed
			if event.key == pygame.K_RIGHT:
				rightDown = False
				playerVX = moveSpeed

		if event.type == GAME_GLOBALS.QUIT:
			quitGame()
		
	move()


	clock.tick(100)
	pygame.display.update()
	
	
