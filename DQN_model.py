# Snake Game
from numpy.core.fromnumeric import argmax
import play as game

# Keras for Train Model
from keras.layers import Dense, Dropout
from keras.models import Sequential
from keras import optimizers

import numpy as np

from collections import deque

import random

class DQN_Model:
	model = None;
	current_ep = 0;

	def __init__( self,
				  game = game.SnakeGame(),
				  epsilon = 0.1,
				  target_ep = 10000,
				  target_step = 1000,
				  min_replay_size = 1000,
				  target_replay_size = 100000):
		self.game = game
		self.epsilone = epsilon
		self.target_ep = target_ep
		self.target_step = target_step

		self.replay_memory = deque(maxlen=target_replay_size)

	def create_model(self, summary = True):
		self.model = Sequential([

			# Input Layer
			Dense(
				3,
				input_shape = (3, ),
				kernel_initializer = 'he_normal',
				activation = 'relu'
			),
			Dropout(0.1),

			# 1 Hidden Layer
			Dense(
				24,
				kernel_initializer = 'he_normal',
				activation = 'relu'
			),
			Dropout(0.1),

			# 2 Hidden Layer
			Dense(
				192,
				kernel_initializer = 'he_normal',
				activation = 'relu'
			),
			Dropout(0.1),

			# Output Layer
			Dense(
				3,
				activation = 'softmax'
			)
		])

		self.model.compile( optimizers = 'rmsprop', loss = 'mse' )

		if summary :
			print(" Created Model : ")
			self.Model.summary()


	def greedy_act(self, state) :
		n = random.random()

		if n < self.epsilone:
			return random.randint(0, 2);
		
		return np.argmax(self.model.predict(np.array(state)))


	def record(self):
		while self.current_ep < self.target_ep :
			
			done = False;
			step = 0;
			current_state = self.game.reset()

			while not done and step < self.target_step:
				action = self.greedy_act(current_state)
			
				reward = game.move(action)
				if reward == -1:
					done = True
			
				next_state = game.get_state()

				self.replay_memory.append((current_state, action, reward, next_state, done))

				current_state = next_state
				step += 1


	def train(self):
		
		"""
			최소한의 샘플이 확보되었는지 확인 :

			모델을 학습할 때 모델을 게임을 진행하며 한번씩 학습하는것 보다
			게임을 진행하고 기록하여 한번에 학습을 하는것이 더 효과적
			
			따라서 최소한의 리플레이 크기를 정한뒤 크기 할당을 채울 시 
			학습을 진행
		"""

		if len(self.replay_memory) < self.min_replay_size:
			print("It need at least " + self.min_replay_size + " of records to training this model ")
			return