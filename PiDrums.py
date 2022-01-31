import pygame
import time
import random

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init() 
pygame.init()

# Set the width and height of the screen (width, height).
screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption("Pi Drums")

clock = pygame.time.Clock()

#my silly sound set
#sound 0 is green
#sound 1 is red
#sound 2 is blue
#sound 3 is yellow
#sound 4 is the foot pedal
#sound0 = pygame.mixer.Sound("sound0.wav")
#sound1 = pygame.mixer.Sound("sound1.wav")
#sound2 = pygame.mixer.Sound("sound2.wav")
#sound3 = pygame.mixer.Sound("sound3.wav")
#sound4 = pygame.mixer.Sound("sound4.wav")


sound0 = pygame.mixer.Sound("0-Snare-Drum-Hit-Level-4a.wav")
sound1 = pygame.mixer.Sound("1-Hi-Hat-Closed-Hit-D1.wav")
sound2 = pygame.mixer.Sound("2-Floor-Tom-Drum-Hit-Level-5B.wav")
sound3 = pygame.mixer.Sound("3-Medium-Tom-Drum-Hit-Level-5A.wav")
sound4 = pygame.mixer.Sound("4-Bass-Drum-Hit-Level-6a.wav")

#poppy playtime sound effect set
#sound0 = pygame.mixer.Sound("huggy_jumpscare.mp3")
#sound1 = pygame.mixer.Sound("PoppyPlaytimeWalking.wav");
#sound2 = pygame.mixer.Sound("HuggieVenting.wav")
#sound3 = pygame.mixer.Sound("PoppyBadIdea.wav")


sound0.set_volume(0.9)
sound1.set_volume(0.9)
sound2.set_volume(0.9)
sound3.set_volume(0.9)
sound4.set_volume(0.9)

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

joystick = pygame.joystick.Joystick(0)
joystick.init()

def game_loop():
	global pause
	gameExit = False    

	while not gameExit:
		#print("test")		
		for event in pygame.event.get(): # User did something.
			print("Event: ",event)
			if event.type == pygame.QUIT: # If user clicked close.
				gameExit = True # Flag that we are done so we exit this loop.
			elif event.type == pygame.JOYBUTTONDOWN:
				#pygame.mixer.Sound.play(sound1)
				print("Joystick button pressed.")
				#print(event.dict, event.joy, event.button, 'pressed')
				print("Button: ", event.button)
				if(event.button == 0):
					pygame.mixer.Sound.play(sound0)
				if(event.button == 1):
					pygame.mixer.Sound.play(sound1)
				if(event.button == 2):
					pygame.mixer.Sound.play(sound2)
				if(event.button == 3):
					pygame.mixer.Sound.play(sound3)
				if(event.button == 4):
					pygame.mixer.Sound.play(sound4)
			elif event.type == pygame.JOYBUTTONUP:
				print("Joystick button released.")
 
 
game_loop()



