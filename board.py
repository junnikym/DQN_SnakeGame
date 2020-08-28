import block

class Board :
	
	level = 1
	fruit = [0, 0]
	wall = []

	def __init__(self, width, height, inc_sride, block_size = 25) :
		self.width = width
		self.height = height
		self.inc_sride = inc_sride
		self.block_size = block_size

	def inc(self) :
		self.level += 1
		self.width  += self.inc_sride
		self.height += self.inc_sride

	def set_block_size(self, size):
		self.block_size = size

	def set_fruit(self, x, y):
		self.fruit[0] = x
		self.fruit[1] = y

	def check_collision(self, x, y):
		for w in self.wall:
			if w[0] == x and w[1] == y :
				return True

		return False

	def is_got_fruit(self, x, y):
		if self.fruit[0] == x and self.fruit[1] == y :
			return True

		return False

	def draw(self, screen, left, top) :
		
		for i in range(self.width) :
			for j in range(self.height) :
				x = i * self.block_size + left
				y = j * self.block_size + top

				block.board_block.draw(screen, x, y, self.block_size)