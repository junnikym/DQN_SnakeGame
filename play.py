import block
import board
import snake

import pygame
import sys

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Rain")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

game_board = board.Board(25, 25, 1, 18)
key_pressed = 0
pre_key = 0

while True:
	clock.tick(60)
	for event in pygame.event.get():
		pre_key = key_pressed

		if event.type == pygame.KEYDOWN: 
			key_pressed = snake.Direction.down
		elif event.type == pygame.KEYUP:
			key_pressed = snake.Direction.up
		elif event.type == pygame.KEYLEFT:
			key_pressed = snake.Direction.left
		elif event.type == pygame.KEYRIGHT:
			key_pressed = snake.Direction.right
		elif event.type == pygame.QUIT:
			sys.exit()
			

	screen.fill(black)

	game_board.draw(screen, 15, 15)
	#block.board_block.draw(screen, 5, 5, 40, 40)

	pygame.display.update()
