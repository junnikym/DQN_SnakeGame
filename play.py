from block import Direction

import block
import board
import snake

import pygame
import sys

from block import CurveAngle

from datetime import datetime, timedelta

from copy import deepcopy

import math

BOARDER_LINE = 15
SCORE_BOARD = 25
BOARD_DECREASE_DELAY = 2.0
BOARD_WARNING_BLINK = 0.25

def timedelta2float(td):
	res = td.microseconds/float(1000000) + (td.seconds + td.days * 24 * 3600)
	return res

class SnakeGame:
	def __init__( self,
				  min_size = 10, 
				  max_size = 20, 
				  block_size = 15,
				  fruit_score = 25,
				  size_down_per = 2,
				  init_speed = 0.225,
				  speed_up_per = 0.01,
				  score_each_level = 50, 
				  init_snake_shape = [[0,0], [1,0], [2,0], [3,0]], 
				  init_snake_pos = [3,0]
				):
		self.block_size = block_size

		self.score = 0
		self.fruit_score = fruit_score
		self.size_down_per = size_down_per
		self.speed = init_speed
		self.speed_up_per = speed_up_per
		self.score_each_level = score_each_level
		self.min_size = min_size

		# create pygame screen
		# ==================================================
		pygame.init()
		pygame.display.set_caption("Snake Game")
		self.screen_width = (max_size) * block_size + BOARDER_LINE
		self.screen_height = self.screen_width + SCORE_BOARD
		self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
		self.clock = pygame.time.Clock()

		self.font = pygame.font.Font('dung_geun_mo.ttf', SCORE_BOARD)

		# create game board
		# ==================================================
		self.game_board = board.Board(max_size, max_size, 1, self.block_size)
		self.init_snake_pos = init_snake_pos
		self.init_snake_shape = init_snake_shape
		self.snake = snake.Snake(
			self.init_snake(),
			self.block_size
		)

		self.game_board.place_fruit_randomly(self.snake.is_on_body)

		self.key_pressed = 0
		self.pre_pressed_key = self.snake.get_step_direction(3)
		self.last_moved_time = datetime.now()
		self.dec_delay_t = 0.0
		self.board_backgournd_color = (0, 0, 0)

	def init_snake(self):
		result = deepcopy(self.init_snake_shape)
		for i in result :
			i[0] += self.init_snake_pos[0]
			i[1] += self.init_snake_pos[1]

		return result

	# Only for AI
	def step(direction):
		"""
			game over 	: return -1
			other 		: return reward value
		"""

		pass

	# Only for Player
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:	
					if event.key == pygame.K_UP:
						self.key_pressed = Direction.up
					if event.key == pygame.K_DOWN:
						self.key_pressed = Direction.down
					if event.key == pygame.K_LEFT:
						self.key_pressed = Direction.left
					if event.key == pygame.K_RIGHT:
						self.key_pressed = Direction.right

			if timedelta(seconds=self.speed) <= datetime.now() - self.last_moved_time:
				result = self.snake.move(self.key_pressed, self.game_board)
				if result == -1:
					self.key_pressed = self.pre_pressed_key
					result = self.snake.move(self.key_pressed, self.game_board)

				if result == 1:
					sys.exit()
				elif result == snake.EATEN_CODE:
					self.score += self.fruit_score
					if (self.score >= self.score_each_level * self.game_board.level) and (self.game_board.width > self.min_size):
						self.dec_delay_t = datetime.now()
						print(self.score_each_level * self.game_board.level)
					else:
						self.game_board.place_fruit_randomly(self.snake.is_on_body)

				self.pre_pressed_key = self.key_pressed

				self.last_moved_time = datetime.now()

			if self.dec_delay_t != 0 :
				delta_t = datetime.now() - self.dec_delay_t

				if timedelta(seconds=BOARD_DECREASE_DELAY) <= delta_t :
					self.speed -= self.speed_up_per
					self.game_board.decrease_size()
					self.game_board.place_fruit_randomly(self.snake.is_on_body)
					self.dec_delay_t = 0.0

				blink = timedelta2float(delta_t)/ timedelta2float(timedelta(seconds=BOARD_WARNING_BLINK))
				blink = 112.5 * (math.cos( blink * math.pi ) + 1)
				self.board_backgournd_color = (225, blink, blink)
			
			else:
				self.board_backgournd_color = (225, 225, 225)

			self.screen.fill((225, 225, 225))

			self.game_board.draw(self.screen, self.screen_width, self.screen_height, self.board_backgournd_color, SCORE_BOARD)

			boarder_line = self.game_board.get_boarderline(self.screen_width, self.screen_height)
			self.snake.draw(self.screen, [boarder_line, boarder_line+SCORE_BOARD])

			# Score
			score_text = " score : " + str(self.score)
			text = self.font.render(score_text,True,(100,100,100))
			self.screen.blit(text,(0,0))

			pygame.display.update()

game = SnakeGame()
game.run();