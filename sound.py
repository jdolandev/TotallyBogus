"""
This is the sound library
Basically, it's a very simple sound playing/mixing function
supports playback, looping, panning, and volume control.
Nothing special beyond that, I'm too lazy to program anything like that

So, here are the variables you really have to pay attention to:
	
	Name			Type			Range			Desc.
	source			string			None			The source of the sound
	volume			float			0.0 - 1.0		The sound volume
	pan				float			-1.0 - 1.0		The sound pan attribute (which speaker it comes from)
	loop 			bool			False - True	Whether or not you want the sound to loop
"""

import pygame
import pygame.mixer

class Sound(object):
	#sets up the sound, and loads it into memory
	def __init__(self, source, loop=False):
		pygame.mixer.init()
		self.sound = pygame.mixer.Sound(source)
		self.volume = 1		#assume it's 1 unless otherwise specified.
		self.pan = 0		#assume the player wants it coming out both speakers
		self.loop = loop 	#assume you won't loop the sound, unless you say so
		
	#plays the sound you want.
	def play(self):
		self.sound.play()