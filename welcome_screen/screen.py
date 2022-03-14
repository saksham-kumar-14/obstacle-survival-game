import pygame
from .button import Button

pygame.init()


class Screen:
	def __init__(self):
		self.width = 100
		self.height = 100
		self.playBtn = Button((0,200,0), (0,255,0) , 100 , 450, 'PLAY')
		self.quitBtn = Button((200,0,0) , (255,0,0), 400, 450, 'EXIT')

	def draw(self, screen):
		stop_welcome_screen = self.playBtn.draw(screen)
		self.quitBtn.draw(screen)

		return stop_welcome_screen
		