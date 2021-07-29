"""
File: sierpinski.py
Name: David
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	This program draws Sierpinski triangle by recursion.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: the order of stacks
	:param length: the length of triangles
	:param upper_left_x: the x coordinate of the upper-left point of the triangle
	:param upper_left_y: the y coordinate of the upper-left point of the triangle
	:return: a triangle with given size and position
	"""
	if order == 0:
		return
	else:
		line_1 = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
		line_2 = GLine(upper_left_x, upper_left_y, upper_left_x+length/2, upper_left_y+length*0.866)
		line_3 = GLine(upper_left_x+length/2, upper_left_y+length*0.866, upper_left_x+length, upper_left_y)
		window.add(line_1)
		window.add(line_2)
		window.add(line_3)
		# Upper-left triangle
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)
		# Upper-right triangle
		sierpinski_triangle(order-1, length/2, upper_left_x+length/2, upper_left_y)
		# Lower triangle
		sierpinski_triangle(order-1, length/2, upper_left_x+length/4, upper_left_y+length*0.433)


if __name__ == '__main__':
	main()
