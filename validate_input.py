# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    validate_input.py                                  :+:    :+:             #
#                                                      +:+                     #
#    By: devanando <devanando@student.codam.nl>       +#+                      #
#                                                    +#+                       #
#    Created: 2019/10/20 23:58:10 by devanando      #+#    #+#                 #
#    Updated: 2019/10/20 23:58:10 by devanando     ########   odam.nl          #
#                                                                              #
# **************************************************************************** #

import sys
import json
import turing_classes
import print_functions

def validate_alphabet(alphabet):

	i = 0
	while i < len(alphabet):
		if len(alphabet[i]) > 1:
			return 1
		i = i + 1
	return 0

def validate_character(char, string):
		i = 0
		x = 0
		while i < len(string):
			j = 0
			while j < len(char):
				if string[i] == char[j]:					
					x = x + 1
				j = j + 1
			i = i + 1
		if x != len(string):
			return (1)
		else:
			return (0)

def validate_input():
	
	if len(sys.argv) > 3:
		print("To many Arguments"); exit()
	if len(sys.argv) == 1:
		print("Wrong number of arguments specified, specify arguments "
		"or type --help"); exit()
	if (len(sys.argv) == 2):
		if (sys.argv[1] == "--help") or (sys.argv[1] == "-h"):
			print_functions.print_help(); exit()
		else:
			print("Wrong number of arguments specified, specify arguments "
			"or type --help")
	try:
		with open(sys.argv[1]) as f:
			data = json.load(f)
	except:
		print("Json file error"); exit()
	else:
		data = turing_classes.TuringMachine(data)
	data.alpa_test(sys.argv[2])
	return data
			