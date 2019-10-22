# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    print_functions.py                                 :+:    :+:             #
#                                                      +:+                     #
#    By: dkroeke <dkroeke@student.codam.nl>           +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/22 14:22:19 by dkroeke        #+#    #+#                 #
#    Updated: 2019/10/22 14:22:19 by dkroeke       ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

from utils import get_transition_actions

def		print_help():
	print("Usage: ./ft_turing.py [-h | --help] jsonfile input\n")
	print("positional arguments:")
	print("   jsonfile\t\t\t\tJson description of the machine\n")
	print("   input\t\t\t\t\tJson description of the machine\n")
	print("optional arguments:")
	print("   -h, --help\t\t\t\tShow this help message and exit\n")
	

def		print_line(char, length):

	i = 0
	while i < length:
		print(char, end = '')
		i += 1

def		print_header(machine_name):
	
	j = 0
	while j != 5:
		if (j == 0):
			print_line("*", 81)
		if (j == 1 or j == 3):
			print('%s'%'*', '%79s'%'*', end = '')
		if (j == 2):
			print ('%s'%'*', '%39s' % machine_name, '%39s' % '*', end = '')
		if (j == 4):
			print_line("*", 81)
		print("")
		j += 1

def		print_machine(machine):

	print("Alphabet : {}".format(machine.alphabet))
	print("States   : {}".format(machine.states))
	print("Initial  : {}".format(machine.initial))
	print("Final    : {}".format(machine.final))
	for trans in machine.transitions:
		transit = get_transition_actions(machine.transitions, trans)
		for actions in transit.actions:
			print("({}, ".format(trans), end = '')
			print("{}) ->".format(actions["read"]), end = '')
			print("({}, ".format(actions["to_state"]), end = '')
			print("{}, ".format(actions["write"]), end = '')
			print("{})".format(actions["action"]))
	print_line("*", 81)
	print("")

def		print_tape(state, input, actions):
	i = 0
	print("[{}".format(input), end = '')
	while i < len(input):
		print(".", end = '')
		i += 1
	print("] current state : {}, read : {} , to_state : {}, write : {}, " 
	"action : {}".format(state, actions["read"],  actions["to_state"],  actions["write"],  actions["action"]))
