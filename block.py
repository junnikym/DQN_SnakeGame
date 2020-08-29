import pygame
from enum import Enum

class Direction(Enum):
	up = 1
	down = 2
	left = 3
	right = 4
	
	def opposite(direction):
		if direction == Direction.up:
			return Direction.down
		elif direction == Direction.down:
			return Direction.up
		elif direction == Direction.left:
			return Direction.right
		elif direction == Direction.right:
			return Direction.left

		return 0

class Block :
	def __init__(self, code, category, img_url) :
		self.code = code
		self.cate_code = category
		self.img = pygame.image.load(img_url)

	def code(self) :
		self.code

	def cate_code(self) :
		self.cate_code

	def draw(self, screen, x, y, size, angle = 0, offset = [0, 0]):
		transform_img = pygame.transform.scale(self.img, (size, size))
		transform_img = pygame.transform.rotate(transform_img, angle)

		screen.blit(
			transform_img,
			(x*size + offset[0], y*size + offset[1])
		)

board_block = Block(0, 0, "resource/board.png")

fruit_block = Block(1, 1, "resource/fruit.png")

snake_head_block = Block(2, -1, "resource/snake_head.png")
snake_straight_block = Block(3, -1, "resource/snake_straight.png")
snake_curve_block = Block(4, -1, "resource/snake_curve.png")
snake_tail_block = Block(5, -1, "resource/snake_tail.png")

CurveAngle = {
	"up_left" 	: 270,
	"up_right"	: 0,
	"down_right": 90,
	"down_left" : 180,
	"left_up"	: 90,
	"left_down" : 0,
	"right_up" 	: 180,
	"right_down": 270,
}

StrightAngle = {
	"up" : 0,
	"down" : 180,
	"left" : 90,
	"right" : 270,
}