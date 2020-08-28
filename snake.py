import block

class Direction(enum.Enum):
	up = 1
	down = 2
	left = 3
	right = 4

class Snake :
	body = []
	
	def __init__(self, body) :
		self.body = body

	def impossible_way(self) :
		head = self.body[len(self.body) - 1]
		pre_head = self.body[len(self.body) - 2]

		# vertical check
		step = head[1] - pre_head[1]

		if step > 0 :
			return Direction.up
		elif step < 0 :
			return Direction.down

		# horizontal check
		step = head[0] - pre_head[0]

		if step > 0 :
			return Direction.left
		elif step < 0 :
			return Direction.right

		return 0

	def move(self, direction, board):
		head = self.body[len(self.body)-1]
		do_not_go = self.impossible_way()

		if do_not_go == direction :
			return -1

		# get next step
		if direction == Direction.up:
			head[1] -= 1
		elif direction == Direction.down:
			head[1] += 1
		elif direction == Direction.left:
			head[0] -= 1
		elif direction == Direction.right:
			head[0] += 1

		# check collision with tail
		for tail in body :
			if tail[0] == head[0] and tail[1] == head[1] :
				return 1

		# check collision with wall
		if board.check_collision(head[0], head[1]) :
			return 1

		# moving head
		self.body.append(head)

		# check snake got fruit
		if board.is_got_fruit(head[0], head[1]):
			del self.body[0]

		return 0

	def draw(self, screen, block_size):
		block.snake_tail_block.draw(
			screen, 
			self.body[0][0],
			self.body[0][1],
			block_size
		)
		pre = self.body[0]

		for i in range(1, self.body-1) :
			next_b = self.body[i+1]

			# stright body
			if pre[0] == next_b[0] and pre[1] == next_b[0] :
				block.snake_straight_block.draw(
					screen, 
					self.body[i][0],
					self.body[i][1],
					block_size
				)

			# curve body
			else :
				block.snake_curve_block.draw(
					screen, 
					self.body[i][0],
					self.body[i][1],
					block_size
				)

		block.snake_head_block.draw(
			screen, 
			self.body[len(self.body)][0],
			self.body[len(self.body)][1],
			block_size
		)