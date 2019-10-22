# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    utils.py                                           :+:    :+:             #
#                                                      +:+                     #
#    By: devanando <devanando@student.codam.nl>       +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/21 00:06:07 by devanando      #+#    #+#                 #
#    Updated: 2019/10/21 00:06:07 by devanando     ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import turing_classes

def 	get_transition_actions(transitions, current_state):

	for key,value in transitions.items():
		if key == current_state:
			return turing_classes.Transitions(key, value)

def		movement(action, index):
	if action == "LEFT":
		index = index - 1
	if action == "RIGHT":
		index = index + 1
	return index

def		swap_characters(string, index, character):
	
	new = string[:index] + character + string[index + 1:]
	return(new)
