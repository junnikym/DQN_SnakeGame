import block
from random import randint
import pygame

class Board :

	def __init__(self, width, height, inc_sride, block_size = 15) :
		self.level = 1
		self.fruit = [0, 0]
		self.wall = []
		
		self.is_fruit_hide = False

		self.width = width
		self.height = height
		self.inc_sride = inc_sride
		self.block_size = block_size

	def decrease_size(self) :
		self.level += 1
		self.width  -= self.inc_sride
		self.height -= self.inc_sride

	def set_block_size(self, size):
		self.block_size = size
	
	def hide_fruit(self):
		self.is_fruit_hide = True
		self.fruit = [-1, -1]

	def place_fruit_randomly(self, checker):
		result = True

		while result:
			self.fruit[0] = randint(0, self.width - 1)
			self.fruit[1] = randint(0, self.height - 1)

			result = checker(self.fruit)

		self.is_fruit_hide = 0

	def check_collision(self, x, y):
		if x < 0 or x > self.width - 1 :
			return True
		
		if y < 0 or y > self.height - 1 :
			return True

		for w in self.wall:
			if w[0] == x and w[1] == y :
				return True

		return False

	def is_got_fruit(self, x, y):
		if self.fruit[0] == x and self.fruit[1] == y :
			return True

		return False

	def get_boarderline(self, width, height):
		boarder_line = (width - self.block_size*self.width) / 2
		return boarder_line

	def draw(self, screen, width, height, background_color, score_size) :
		intire_board = width - self.block_size*self.width
		boarder_line =  intire_board / 2

		# Boarder Line
		pygame.draw.rect(
			screen, 
			background_color, 
			[0, score_size, width + boarder_line, height + boarder_line]
		)

		for i in range(self.width) :
			for j in range(self.height) :
				x = i
				y = j

				block.board_block.draw(screen, x, y, self.block_size, offset=[boarder_line, boarder_line + score_size])
		
		if not self.is_fruit_hide:
			block.fruit_block.draw(
				screen, 
				self.fruit[0], self.fruit[1],
				self.block_size,
				offset=[boarder_line, boarder_line + score_size]
			)