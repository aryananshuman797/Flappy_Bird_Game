import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60		# 60 frames per second

screen_width = 864
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height)) #create a screen
pygame.display.set_caption('Flappy Bird')


#define game variables
ground_scroll = 0
scroll_speed = 4

#load images
bg = pygame.image.load('img/bg.png')	# For background
ground_img = pygame.image.load('img/ground.png')



class Bird(pygame.sprite.Sprite):
	def __init__(self, x, y):	# (x , y) is where the bird(self) will be drown
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		self.index = 0
		self.counter = 0
		for num in range(1, 4):
			img = pygame.image.load(f'img/bird{num}.png') 	# python terminology. f' will just conver and append num into string'
			self.images.append(img)
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

	def update(self):

		#handle the animation
		self.counter += 1
		flap_cooldown = 5

		if self.counter > flap_cooldown:
			self.counter = 0
			self.index += 1
			if self.index >= len(self.images):
				self.index = 0
		self.image = self.images[self.index]


bird_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 2))

bird_group.add(flappy)



run = True
while run:

	clock.tick(fps)	# Tick at the frame rate of fps

	#draw background
	# copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.
	screen.blit(bg, (0,0)) 		# When it runs, import background image


	bird_group.draw(screen)	# draw in a buildin function in prite class
	bird_group.update()		# It will update the bird images


	#draw and scroll the ground
	screen.blit(ground_img, (ground_scroll, 668))
	ground_scroll -= scroll_speed
	if abs(ground_scroll) > 35:	# Create an illusion of ground scrolling
		ground_scroll = 0 		# 35 is the difference of the width of background and ground image


	for event in pygame.event.get():	# It will help to close the window
		if event.type == pygame.QUIT:	#When you will click x to close
			run = False

	pygame.display.update()		# It will comtinuously update the visuals

pygame.quit()
