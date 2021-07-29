"""
File: largest_digit.py
Name: David
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	This function finds the biggest digit in the input integer.
	"""
	# Make negative integer positive
	if n < 0:
		n = -n
	# Count the number of digits in the input integer
	# Because while loop and other data structures are not allowed to be used, this function can only deal with
	# integer that has the number of digits lower than 5
	digit = 0
	if n % 10 == n:
		digit = 1
	elif n % 100 == n:
		digit = 2
	elif n % 1000 == n:
		digit = 3
	elif n % 10000 == n:
		digit = 4
	elif n % 100000 == n:
		digit = 5
	return helper(n, digit, 0)


def helper(n, order, current_max):
	"""
	This function help find the biggest digit.
	:param n: the input integer
	:param order: the number of digits
	:param current_max: the currently biggest digit
	:return: the biggest digit
	"""
	# +-(0~9)
	if order == 0:
		return int(current_max)
	# +-(10~99999)
	else:
		# Get digit
		division = 10**(order-1)
		num = (n - (n % division))/division
		if num > current_max:
			current_max = num
		return helper(n % division, order-1, current_max)


if __name__ == '__main__':
	main()
