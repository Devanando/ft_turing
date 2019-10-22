# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    turing_classes.py                                  :+:    :+:             #
#                                                      +:+                     #
#    By: dkroeke <dkroeke@student.codam.nl>           +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/22 14:28:52 by dkroeke        #+#    #+#                 #
#    Updated: 2019/10/22 14:28:52 by dkroeke       ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import utils
import validate_input

class Transitions():

	def __init__(self, transition, actions):
		self.transition = transition
		self.actions = actions


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
		if validate_input.validate_alphabet(self.alphabet):
			print("Length of alphabet argument in json file is not 1")
			exit()
			
		if validate_input.validate_character(self.alphabet, string):
			print("Invalid alphabet character")
			exit()
			