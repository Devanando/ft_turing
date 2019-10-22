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