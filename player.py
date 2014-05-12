"""
This is the player class, if you couldn't figure that out.
Basically, this class controls the things to do with the player.

All objects in the engine break down into 3 things:
	- Creation code
	- Step (input) function
	- Destroy
	
__init__() - the create function is called when the player is initialized
instantiating all the variables and other things to do with the player.

update() - the step event, is called once per frame, checks for input, then 
updates the play accordingly.

__del__() - this function is called when the object is destroyed.
Basically, it'll free up memory space and clean things up in order to make sure
The game runs smoothly. Especially with an interpreted language like python,
You have to worry about performance.
"""

import pygame
from sound import *
from camera import *

theme = Sound("snd/maintheme.wav", False)


class Player(object):
	def __init__(self, x, y, w, h, src):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.pos = (self.x,self.y)
		self.src = src
		self.image = pygame.image.load(src).convert()
		self.visible = True
		self.debug = False
		self.image_index = 0
		self.image_length = 1
		#theme.play()
	
	"""
	Sprite animation. I did a pretty shitty job of implementing this
	In hindsight, it would have been more efficient to find out how to make sprite sheets;
	but oh well, I've got a fucking week to do this.
	"""
	def animate(self):
		pass
		
	def update(self):
		self.pos = (self.x, self.y)	#update the player's location
		self.image_index += 1	#Add one to the cycle
		key = pygame.key.get_pressed()	#check for current key presses
		#keyboard press logic
		if key[pygame.K_UP]:
			self.y -= 0.5
			self.image = pygame.image.load("img/player/playerU.png").convert()
			
		elif key[pygame.K_DOWN]:
			self.y += 0.5
			self.image = pygame.image.load("img/player/playerD.png").convert()
			
		if key[pygame.K_LEFT]:
			self.x -= 0.5
			#if you're not pressing up or down
			if (not key[pygame.K_UP]) and ( not key[pygame.K_DOWN]):
				self.image = pygame.image.load("img/player/playerL.png").convert()
				
		elif key[pygame.K_RIGHT]:
			self.x += 0.5
			#if you're not pressing up or down
			if (not key[pygame.K_UP]) and ( not key[pygame.K_DOWN]):
				self.image = pygame.image.load("img/player/playerR.png").convert()
				
	def __del__(self):
		pass