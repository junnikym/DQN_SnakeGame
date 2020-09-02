from block import Direction, Block, CurveAngle, StrightAngle
import block
from copy import deepcopy

EATEN_CODE = 2

class Snake :
	body = []
	
	def __init__(self, body, block_size = 15) :
		self.body = body
		self.block_size = block_size

	def get_step_direction(self, i) :
		cur = self.body[i]
		pre = self.body[i - 1]

		# vertical check
		step = cur[1] - pre[1]

		if step > 0 :
			return Direction.down
		elif step < 0 :
			return Direction.up

		# horizontal check
		step = cur[0] - pre[0]

		if step > 0 :
			return Direction.right
		elif step < 0 :
			return Direction.left
		
		return 0

	# opposite_direction of get_step
	def impossible_way(self) :
		d = self.get_step_direction(len(self.body) - 1)

		return Direction.opposite(d)

	def is_on_body(self, pos) :
		for b in self.body :
			if b[0] == pos[0] and b[1] == pos[1] :
				return True

		return False

	def move(self, direction, board):
		is_eaten = 0
		head = deepcopy( self.body[len(self.body)-1] )
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
		else :
			return -1

		# check collision with tail
		for i in range(len(self.body)-1) :
			if self.body[i][0] == head[0] and self.body[i][1] == head[1] :
				return 1

		# check collision with wall
		if board.check_collision(head[0], head[1]) :
			return 1

		# moving head
		self.body.append(head)
		# check snake got fruit
		if board.is_got_fruit(head[0], head[1]):
			board.hide_fruit()
			return EATEN_CODE
		else :
			del self.body[0]

		return 0

	def draw(self, screen, offset):
		pre_d = self.get_step_direction(1)
		cur_d = 0

		# Tail
		block.snake_tail_block.draw(
			screen, 
			self.body[0][0],
			self.body[0][1],
			self.block_size,
			StrightAngle[pre_d.name],
			offset
		)

		# Middel Body
		for i in range(1, len(self.body)-1) :
			cur_d = self.get_step_direction(i+1)

			if cur_d == pre_d :		# stright body
				block.snake_straight_block.draw(
					screen, 
					self.body[i][0],
					self.body[i][1],
					self.block_size,
					StrightAngle[cur_d.name],
					offset
				)

			else :					# curve body
				block.snake_curve_block.draw(
					screen, 
					self.body[i][0],
					self.body[i][1],
					self.block_size,
					CurveAngle[pre_d.name + '_' + cur_d.name],
					offset
				)

			pre_d = self.get_step_direction(i+1)

		# Head
		block.snake_head_block.draw(
			screen, 
			self.body[len(self.body)-1][0],
			self.body[len(self.body)-1][1],
			self.block_size,
			StrightAngle[cur_d.name],
			offset
		)