"""
File: Draw line
Name: David
-------------------------
This program provides users with a line-drawing tool
that draws a line after users click the starting point
and end point.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow()
SIZE = 15
hollow_circle = GOval(SIZE, SIZE)
# The position oh the first click
x1 = 0
y1 = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    # Add the hollow circle and place it out of the window.
    window.add(hollow_circle, -2*hollow_circle.width, 0)
    onmouseclicked(draw_line)


def draw_line(m):
    """
    :param m: the position of mouse-click
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    global x1
    global y1
    # A click is the first click when the circle is not on the window
    if hollow_circle.x < 0:
        x1 = m.x-hollow_circle.width/2
        y1 = m.y-hollow_circle.height/2
        hollow_circle.x = x1
        hollow_circle.y = y1
    # The second click
    else:
        # Move out the hollow circle
        hollow_circle.x = -2*hollow_circle.width
        x2 = m.x - hollow_circle.width / 2
        y2 = m.y - hollow_circle.height / 2
        stroke = GLine(x1, y1, x2, y2)
        window.add(stroke)


if __name__ == "__main__":
    main()
