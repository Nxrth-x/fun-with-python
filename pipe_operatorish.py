"""
Some fun bringing functional concepts to Python

Note that this is not optimized nor makes your code
more readable or maintainable.
This is just some experiment on bringing the pipe
operator "|>" to Python.
"""

class Piped(object):
	def __init__(self, value):
		self.value = value
	def __rshift__(self, function):
		return Piped(function(self.value))
	def __str__(self):
		return str(self.value)

def _(function, *args, **kwargs):
	"""Generates a callback function to use in combination with the piped object"""
	def decorated(*outer_args, **outer_kwargs):
		return function(*outer_args, *args, **kwargs, **outer_kwargs)
	return decorated

first_function = _(lambda x, y, z = 5: x + y + z, 10, z=6) # Named arguments
second_function = _(lambda x: x - 10) # Basic function without parameters
third_function = lambda x: x * 2 # Same function as before but without the decoration

# Piping
value = (
	Piped(2)
	>> first_function
	>> second_function
	>> third_function
)

print(value)
