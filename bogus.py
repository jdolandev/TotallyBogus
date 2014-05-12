"""
This is the source code to Totally Bogus!
Because I have to appease the dark lord Stallman, I'm giving away the source code.
As you will probably discover, I'm not the world's greatest programmer, but whatever.
I made a game and that's all that matters.
Python's pretty dope, yo. I quite like it.
Feel free to dick around as you wish. I'd love to see spin-off games or extra missions
Hell, steal my source and claim you made this fucker.

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
THIS GAME WAS PROGRAMMED FOR PYTHON 3.X
Since it's pygame, you should be able to run it on a 2.X version
but no guarantees. 
I'll whip up a 2.X version soon, don't worry, kiddos. 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

if you want to contact me and show me what you've done, my e-mail should be
jdolandev@gmail.com

if it isn't, well shit...

have fun,
-Joe
"""

import pygame
import sys
import os
from pygame.locals import *
from player import *
from sound import * 
from background import *
from camera import *


SCREEN_WIDTH = 512			# I used the original NES resolution
SCREEN_HEIGHT = 480			# because the theme was '8-bit'

rezh = int(SCREEN_WIDTH / 256)			#resolution scaling.
rezv = int(SCREEN_HEIGHT / 240) 

timer = pygame.time.Clock()
os.environ['SDL_VIDEO_CENTERED'] = '1'		#Black magic that centers the window
global window
window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Totally Bogus!')

pygame.init()

global objects
backgrounds = []
objects = []		#Array of objects on the screen

c_black = (0,0,0)
c_red = (255,0,0)
c_green = (0,255,0)
c_blue = (0,0,255)
c_white = (255,255,255)
c_cornflower = (100, 149, 237)

player = Player(128,128,16,16, "img/player/playerD.png")
objects.append(player)
backgrounds.append(Background("img/bg1.png"))

"""
Window properties object. It handles all the properties pertaining to the window.
Whoda thunk it, right? Like, holy shit, I couldn't have figured it out myself
If not for this very useful documentation header. Thanks, Joe, you're a real pal.
"""
class windowProps(object):
	def __init__(self):
		objects.append(self)
		self.visible = False
		self.debug = False
		self.collisionBox = False
	def update(self):
		key = pygame.key.get_pressed()
		if( key[pygame.K_ESCAPE]):
			pygame.quit()
			sys.exit()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
	def draw(self):
		pass

def update():
	global camx
	global camy
	for i in backgrounds:
		i.update()
	for i in objects:
		i.update()
	
	camx = player.x
	camy = player.y
	
"""
	If you're interested in how I chose the aesthetic, refer to this:
	https://www.youtube.com/watch?v=Hvx4xXhZMrU
	
	I tried to follow all the constraints set up in the video,
	namely the use of 4 color tiles.
"""
		
def draw():	

	camx = player.x
	camy = player.y
	
	window.fill(c_cornflower)
	for i in backgrounds:
		#draw the image, taking into account the camera.
		window.blit(pygame.transform.scale(i.image, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0,0), (camx, camy, SCREEN_WIDTH, SCREEN_HEIGHT))
		#This works fine without any problems. So, like, what the fuck, man?
	for i in objects:
		if(i.visible):
			window.blit(pygame.transform.scale(i.image, (i.w * rezh, i.h * rezv)), (camx, camy), (i.x, i.y, SCREEN_WIDTH, SCREEN_HEIGHT))
			#This seems to fuck up. Huh...
		if(i.debug):
			pass
	
	pygame.display.update()
	pygame.display.flip()

def mainLoop():
	while True:
		update()
		draw()
		timer.tick(60)
	
def init():
	pygame.mouse.set_visible(False)
	w = windowProps()
	
init()
mainLoop()