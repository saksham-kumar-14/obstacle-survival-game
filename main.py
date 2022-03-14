import pygame, sys, random, time

from welcome_screen.screen import Screen
from player.player import Player
from obstacle.obstacle import Obstacle

pygame.init()
pygame.font.init()

WIDTH,HEIGHT = 900,600
SCREEN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Obstacle Survival")
GROUND_LEVEL = 450

# defining variables
BG_IMG = pygame.transform.scale(pygame.image.load("images/other-images/background.png"), (WIDTH,HEIGHT))



# main execution
def run():
	global BG_IMG , GROUND_LEVEL

	# for welcome screen 
	welcome_screen = Screen()
	display_welcome_screen = True
	game_over = False

	# for main game
	player = Player(75, GROUND_LEVEL)
	player_jumping = False

	obstacle_probability = ['spikes','wood']
	obstacles = []   # [ x,y,width,height,image ]
	baseX = 900
	for i in range(5):

		image = random.choice(obstacle_probability)
		x = baseX
		baseX += random.randrange(275,350)
		y = GROUND_LEVEL+10
		height = 50
		if image == 'spikes':
			width = 75
		else:
			width = 50
		current_obstacle = Obstacle( x,y,width,height,image,15 )
		obstacles.append(current_obstacle)

		if i==3:
			reinitialize_x_pos = baseX - 500

	# velocity variables
	gameVelocity = 10
	increaseVelTimer = 0


	# for game over
	font  = pygame.font.Font("freesansbold.ttf",40)
	gameOverText = font.render("GAME OVER", True, (255,0,0))
	gameOverTimer = 0

	# current Score 
	score = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE] :
				pygame.quit()
				sys.exit()

		if display_welcome_screen!=False :
			SCREEN.fill(( 0,0,0 )) 
			display_welcome_screen = welcome_screen.draw(SCREEN)
		elif not game_over:
			SCREEN.fill(( 0,0,0 ))
			SCREEN.blit(BG_IMG, (0,0))
			player.draw(SCREEN)
			
			player.move(player_jumping)
			for i in obstacles:
				i.draw(SCREEN)
				i.move()

			#collision detection
			for i in obstacles:
				a = player.collides(i)
				if a:
					game_over = True


			if pygame.key.get_pressed()[pygame.K_UP]:
				player_jumping = True
			if player_jumping:
				player_jumping = player.jump()


			# re-initializing obstacles 
			for i in obstacles:
				if i.x < -25:
					i.reinitialize(reinitialize_x_pos)


			# increasing velocity timer
			increaseVelTimer += 1 
			if increaseVelTimer == 350:
				gameVelocity += 2
				for i in obstacles:
					i.vel += 2
				increaseVelTimer = 0

			# increasing score
			for i in obstacles:
				isScore = player.is_score(i, gameVelocity)
				if isScore:
					score += 1


			# displaying score
			font = pygame.font.Font("freesansbold.ttf", 40)
			scoreText = font.render(f"Score : {score}", True, (255,0,0))
			SCREEN.blit(scoreText, (0,0))


		else:
			gameOverTimer += 1 
			if gameOverTimer == 25:
				# for welcome screen 
				welcome_screen = Screen()
				display_welcome_screen = True
				game_over = False

				# for main game
				player = Player(25, GROUND_LEVEL)
				player_jumping = False

				obstacle_probability = ['spikes','wood']
				obstacles = []   # [ x,y,width,height,image ]
				baseX = 900
				for i in range(5):

					image = random.choice(obstacle_probability)
					x = baseX
					baseX += random.randrange(275,350)
					y = GROUND_LEVEL+10
					width = 75
					height = 50
					current_obstacle = Obstacle( x,y,width,height,image,10 )
					obstacles.append(current_obstacle)

					if i==3:
						reinitialize_x_pos = baseX - 400

				# velocity variables
				gameVelocity = 10
				increaseVelTimer = 0


				# for game over
				font  = pygame.font.Font("freesansbold.ttf",40)
				gameOverText = font.render("GAME OVER", True, (255,0,0))
				gameOverTimer = 0

				# current Score 
				score = 0
			SCREEN.blit(gameOverText, (300,200))


		pygame.time.Clock().tick(40)
		pygame.display.update()



run()