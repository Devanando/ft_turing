# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    turingmachine.py                                   :+:    :+:             #
#                                                      +:+                     #
#    By: devanando <devanando@student.codam.nl>       +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/20 23:58:10 by devanando      #+#    #+#                 #
#    Updated: 2019/10/20 23:58:10 by devanando     ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import sys
from utils import *

def		swap_characters(string, index, character):
	
	new = string[:index] + character + string[index + 1:]
	return(new)

def		movement(action, index):
	if action == "LEFT":
		index = index - 1


	if action == "RIGHT":
		index = index + 1
	return index

class Transitions():

	def __init__(self, transition, actions):
		self.transition = transition
		self.actions = actions

	#def state_actions(self, )


class TuringMachine():

	def __init__(self, data):

		self.data = data
		self.name = self.data["name"]
		self.alphabet = self.data["alphabet"]
		self.blank = self.data["blank"]
		self.transitions = self.data["transitions"]
		self.final = self.data["finals"]
		self.initial = self.data["initial"]
		self.states = self.data["states"]

	def alpa_test(self, string):
		if validate_alphabet(self.alphabet):
			print("Length of alphabet argument in json file is not 1")
			exit()
		if validate_character(self.alphabet, string):
			print("Invalid alphabet character")
			exit()

	 
def		process(tmachine, input):

	i = 0
	current_state = tmachine.initial
	transitions = tmachine.transitions


	while current_state != tmachine.final:
		for key,value in transitions.items():
			if key == current_state:
				transit = Transitions(key, value)
		for actions in transit.actions:
			if actions["read"] == input[i] and len(input) > i and transit.transition == current_state:
				print("current state : {}, tape: <{}> read : {} , to_state : {}, write : {}, " 
				"action : {}".format(current_state, input, actions["read"],  actions["to_state"],  actions["write"],  actions["action"]))
				input = swap_characters(input, i, actions["write"])
				i = movement(actions["action"], i)
				current_state = actions["to_state"]
				print(input)
				if i < 0:
					input = tmachine.blank + input
					i = 0
				if current_state == tmachine.final[0]:
					exit()