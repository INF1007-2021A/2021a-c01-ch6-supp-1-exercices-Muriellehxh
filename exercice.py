#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	list_max = []
	for single_list in numbers:
		list_max.append(max(single_list))

	return list_max

def join_integers(numbers):
	string = ''
	for number in numbers:
		string += str(number)
	return int(string)

def generate_prime_numbers(limit):
	list_prime = [2]
	n = 3
	while n <= limit:
		is_prime = True
		for div in range(2, n):
			if n != div:
				if n % div == 0:
					is_prime = False
					break
		if is_prime is True:
			list_prime.append(n)
		n += 1

	return list_prime


def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):

	list_string = []
	for numb in range(1, num_combinations + 1):
		for letter in strings:

			if excluded_multiples == None or numb % excluded_multiples != 0:
				list_string.append(f'{letter}{numb}')

	return list_string


if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
