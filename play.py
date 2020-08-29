from block import Direction

import block
import board
import snake

import pygame
import sys

from block import CurveAngle

from datetime import datetime, timedelta

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()
pygame.display.set_caption("Rain")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

game_board = board.Board(25, 25, 1, 18)
snake = snake.Snake(
	[[0,0], [1,0], [2,0], [3,0]],
	18
)

game_board.place_fruit_randomly(snake.is_on_body)

key_pressed = 0
pre_pressed_key = snake.get_step_direction(3)

last_moved_time = datetime.now()

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:	
			if event.key == pygame.K_UP:
				key_pressed = Direction.up
			if event.key == pygame.K_DOWN:
				key_pressed = Direction.down
			if event.key == pygame.K_LEFT:
				key_pressed = Direction.left
			if event.key == pygame.K_RIGHT:
				key_pressed = Direction.right

	if timedelta(seconds=0.25) <= datetime.now() - last_moved_time:
		result = snake.move(key_pressed, game_board)
		if result == -1:
			key_pressed = pre_pressed_key
			result = snake.move(key_pressed, game_board)

		if result == 1:
			sys.exit()
		
		pre_pressed_key = key_pressed

		last_moved_time = datetime.now()

	screen.fill((0, 0, 0))

	game_board.draw(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

	boarder_line = game_board.get_boarderline(SCREEN_WIDTH, SCREEN_HEIGHT)
	snake.draw(screen, [boarder_line, boarder_line])

	pygame.display.update()
