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

import json
import sys
from turingmachine import TuringMachine
from turingmachine import process

def validate_input():
	
	json_file = sys.argv[1]
	if len(sys.argv) > 3:
			print("To many Arguments")
			exit()
	#if len(sys.argv) == 1

	while True:
		try:
			with open(json_file) as f:
				data = json.load(f)
		except:
			json_file = input("Incorrect json format or incorrect file\n"
							"Please re-enter a valid json Path\n json Path : ")
		else:
			data = TuringMachine(data)
			break
	data.alpa_test(sys.argv[2])
	return data
			

if __name__ == "__main__":
	data = validate_input()
	process(data, sys.argv[2])
	pass

