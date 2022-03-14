import pygame

pygame.init()

PLAYER_WIDTH, PLAYER_HEIGHT = 65,65
all_positions = []
jumping_positions = []
defeat_positions = []

for i in range(3):
	jumping_positions.append(pygame.transform.scale(pygame.image.load("images/Player/player_jumping_"+str(i+1)+".png"), (PLAYER_WIDTH, PLAYER_HEIGHT)))
for i in range(5):
	all_positions.append(pygame.transform.scale(pygame.image.load("images/Player/player_right_"+str(i+1)+".png"), (PLAYER_WIDTH, PLAYER_HEIGHT)))
for i in range(3):
	defeat_positions.append(pygame.transform.scale(pygame.image.load("images/Player/player_right_died_"+str(i+1)+".png"), (PLAYER_WIDTH, PLAYER_HEIGHT)))



class Player : 
	def __init__(self, x, y):
		global all_positions,  jumping_positions, defeat_positions, PLAYER_WIDTH, PLAYER_HEIGHT

		self.all_positions = all_positions
		self.jumping_positions = jumping_positions
		self.defeat_positions = defeat_positions
		self.current_position = all_positions[0]
		self.x , self.y = x, y
		self.width, self.height = PLAYER_WIDTH, PLAYER_HEIGHT

		self.jump_init_vel = 25
		self.jump_vel = self.jump_init_vel
		self.g = 2


	def draw(self, screen):
		screen.blit(self.current_position, (self.x, self.y))

	def findIndex(self,arr,item):
		for i in range(len(arr)):
			if arr[i]==item:
				return i

		return -1

	def move(self, player_jumping):

		if not player_jumping : 
			if self.current_position == self.all_positions[-1]:
				self.current_position = self.all_positions[0]
			else:
				self.current_position = self.all_positions[self.findIndex(all_positions,self.current_position)+1]
		else:
			if self.current_position == self.jumping_positions[-1]:
				self.current_position = self.jumping_positions[0]
			else:
				index = self.findIndex(jumping_positions, self.current_position)
				if index == -1:
					self.current_position = self.jumping_positions[0]
				else:
					self.current_position = self.jumping_positions[index+1]


	def jump(self):
		self.y -= self.jump_vel
		self.jump_vel -= self.g 
		if self.jump_vel < -self.jump_init_vel:
			self.jump_vel = self.jump_init_vel
			return False

		return True


	def collides(self,obj):
		rect1 = pygame.Rect(self.x, self.y, self.width, self.height)
		rect2 = pygame.Rect(obj.x, obj.y, obj.width, obj.height)

		return rect1.colliderect(rect2)


	def is_score(self, obj, offset):
		if obj.x+offset > self.x > obj.x:
			return True

		return False