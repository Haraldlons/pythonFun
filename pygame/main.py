import sys, pygame
import time, random
import pandas as pd
from helper_functions import *
# from test//test import *

# Import leaderboard
leaderboard_df = pd.read_csv("leaderboard.csv")
print(leaderboard_df)

pygame.init()
speed = [2, 2]
black = 0, 0, 0
color = 23, 211, 23
left_border_width = 500

# Set screen size
size = width, height = 1200, 1000 # To make a tuple
screen = pygame.display.set_mode(size)

# Get ball and star
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
ballrect = ballrect.move(700,200)

star = pygame.image.load("star.png")
starrect = pygame.Rect((random.randint(left_border_width,width), random.randint(1,1000), 128, 128))


number_of_wall_touches = 0
touch_flag = 0

points = 0

myfont = pygame.font.SysFont("monospace", 40)
myfont2 = pygame.font.SysFont("monospace", 80)

label1 = myfont.render(str(leaderboard_df), 1, (255,255,255))
screen.blit(label1, (125, 150))
# Set up left side (leaderboard)
left_background = pygame.Rect(0, 0, left_border_width, height)


def exit_program():
	print("You lost with " + str(number_of_wall_touches) + " touches to the wall")

	screen.fill(color)
	label = myfont2.render("You lost!", 1, (255,255,255))
	screen.blit(label, (width/2-width/7, height/2))
	pygame.display.flip()

	time.sleep(2)
	sys.exit()

def touched_wall(number_of_wall_touches):
	print("You have touched the wall " + str(number_of_wall_touches) + " times!")
	global touch_flag
	touch_flag = 100
	return number_of_wall_touches + 1, touch_flag

def drawLeftSide():
	pygame.draw.rect(screen, (255,255,255), left_background, 0)
	label = myfont.render("Leaderboard", 1, (100,100,100))
	label2 = myfont.render("1: " + str(leaderboard_df.iloc[0]['name']), 1, (100,100,100))
	# label = myfont.render("Leaderboard", 1, (255,255,255))
	# label = myfont.render("Leaderboard", 1, (255,255,255))
	screen.blit(label, (20,20))
	screen.blit(label2, (20,60))

blue=(0,0,255)



while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			exit_program()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				speed[0] = -abs(speed[0])
			if event.key == pygame.K_RIGHT:
				speed[0] = abs(speed[0])
			if event.key == pygame.K_UP:
				speed[1] = -abs(speed[0])
			if event.key == pygame.K_DOWN:
				speed[1] = abs(speed[0])

	ballrect = ballrect.move(speed)
	if ballrect.left < left_border_width or ballrect.right > width:
		speed[0] = -speed[0]
		number_of_wall_touches, touch_flag = touched_wall(number_of_wall_touches)
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
		number_of_wall_touches, touch_flag = touched_wall(number_of_wall_touches)

	if number_of_wall_touches > 9:
		exit_program()

	time.sleep(0.001)
	screen.fill(black)
	screen.blit(ball, ballrect)
	screen.blit(star, starrect)

	drawLeftSide()


	if starrect.colliderect(ballrect):
		points += 1
		print("You got a star!")
		if speed[0] < 6:
			if speed[0] > 0:
				speed[0] = speed[0] + 0.2
			else:
				speed[0] = speed[0] - 0.2
		if speed[1] < 6:
			if speed[1] > 0:
				speed[1] = speed[1] + 0.2
			else:
				speed[1] = speed[1] - 0.2
		starrect = pygame.Rect(random.randint(left_border_width,width-starrect.width), random.randint(1,height-starrect.height), 128, 128)

	# Write number_of_wall_touches on screen
	label = myfont.render("Wall touches: " + str(number_of_wall_touches), 1, (0,0,0))
	label2 = myfont.render("Points: " + str(points), 1, (0,0,0))
	label_speed_x = myfont.render("Speed X: " + str(speed[0]), 1, (0,0,0))
	label_speed_y = myfont.render("Speed Y: " + str(speed[1]), 1, (0,0,0))
	screen.blit(label, (10, 900))
	screen.blit(label2, (10, 860))
	screen.blit(label_speed_x, (10, 500))
	screen.blit(label_speed_y, (10, 550))
	if touch_flag > 0:
		touch_flag -= 1
		label = myfont.render("Ouch!", 1, (255,255,255))
		screen.blit(label, (width*0.7, height*0.5))

	pygame.display.flip()
