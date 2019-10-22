#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    ft_turing.py                                       :+:    :+:             #
#                                                      +:+                     #
#    By: devanando <devanando@student.codam.nl>       +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/19 23:07:13 by devanando      #+#    #+#                 #
#    Updated: 2019/10/19 23:07:13 by devanando     ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import sys
import turing_classes
import print_functions
import utils
from validate_input import validate_input

def		process(machine, input):

	i = 0
	current_state = machine.initial
	transitions = machine.transitions

	print_functions.print_header(machine.name)
	print_functions.print_machine(machine)
	while current_state != machine.final:
		transit = utils.get_transition_actions(transitions, current_state)
		if current_state == machine.final[0]:
			exit()
		for actions in transit.actions:
			if actions["read"] == input[i] and transit.transition == current_state:
				print_functions.print_tape(current_state, input, actions)
				input = utils.swap_characters(input, i, actions["write"])
				i = utils.movement(actions["action"], i)
				current_state = actions["to_state"]
				if i < 0:
					print("\nError: This Turing machine only works in one"
					"direction.")
					exit()

if __name__ == "__main__":
	data = validate_input()
	process(data, sys.argv[2])

