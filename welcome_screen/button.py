import pygame , sys

pygame.init()
pygame.font.init()


class Button():
	def __init__(self, color,alt_color,x,y, text):
		self.width = 100
		self.height = 50
		self.color = color
		self.alt_color = alt_color
		self.x = x
		self.y = y
		self.btn_text = text

		font = pygame.font.Font('freesansbold.ttf', 35)
		self.text = font.render(text, True, (255,255,255))


	def draw(self, screen):
		m_pos = pygame.mouse.get_pos()
		m_pressed = pygame.mouse.get_pressed()
		if ((self.x+self.width) > m_pos[0] > self.x) and ((self.y+self.height) > m_pos[1] > self.y) : 
			pygame.draw.rect(screen, self.alt_color, pygame.Rect(self.x, self.y, self.width, self.height))

			if True in m_pressed:
				if self.btn_text == 'PLAY':
					return False
				elif self.btn_text == 'EXIT':
					pygame.quit()
					sys.exit()

		else:
			pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

		screen.blit(self.text, (self.x+5, self.y+8))
