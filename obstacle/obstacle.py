import pygame, sys , random


class Obstacle:
	def __init__(self,x,y,width,height,img, velocity):
		self.x = x 
		self.y = y 
		self.vel = velocity
		self.width = width
		self.height = height
		self.img = pygame.transform.scale(pygame.image.load(f"images/Obstacles/{img}.png"), (width,height))


	def draw(self, screen):
		screen.blit(self.img, (self.x,self.y))


	def move(self):
		self.x -= self.vel


	def reinitialize(self, x_pos):
		self.x = x_pos
