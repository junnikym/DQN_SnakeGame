import pygame

class Block :
	def __init__(self, code, category, img_url) :
		self.code = code
		self.cate_code = category
		self.img = pygame.image.load(img_url)

	def code(self) :
		self.code

	def cate_code(self) :
		self.cate_code

	def draw(self, screen, x, y, size):
		screen.blit(
			pygame.transform.scale(self.img, (size, size)),
			(x, y)
		)

board_block = Block(0, 0, "resource/board.png")

fruit_block = Block(1, 1, "resource/fruit.png")

snake_head_block = Block(2, -1, "resource/snake_head.png")
snake_straight_block = Block(3, -1, "resource/snake_straight.png")
snake_curve_block = Block(4, -1, "resource/snake_curve.png")
snake_tail_block = Block(5, -1, "resource/snake_tail.png")