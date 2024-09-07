def get_circle_length(x, y):
	"""
	>>> get_circle_length(100, 10)
	10

	>>> get_circle_length(50, 5)
	10

	>>> get_circle_length(67, 3)
	4

	>>> get_circle_length(1)
	Traceback (most recent call last):
	TypeError: get_circle_length() missing 1 required positional argument: 'y'

	>>> get_circle_length(1, 2, 3)
	Traceback (most recent call last):
	TypeError: get_circle_length() takes 2 positional arguments but 3 were given
	"""
	return int((y / x) * 100)


if __name__ == '__main__':
	import doctest
	doctest.testmod()
