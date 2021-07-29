"""
File: Bouncing ball
Name: David
-------------------------
This program shows a bouncing ball which drops and bounces when
users click the window. For each run, users can initiate the ball
drop three times.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked
# horizontal velocity
VX = 3
# Delay time for animation
DELAY = 10
# The velocity increased in each loop
GRAVITY = 1
# Ball size
SIZE = 20
# The velocity lost in each bounce
REDUCE = 0.85
START_X = 30
START_Y = 40
# Count the number of drop initiated by users.
count = 0
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)

window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    # Add the ball onto the window.
    ball.filled = True
    window.add(ball)
    # Launch onmouseclicked()
    onmouseclicked(start)


def start(m):
    """
    The ball start to drop and bounce if the click is effective
    (click when the ball is at (START_X, START_Y) and the count
    is smaller than three)
    """
    global count
    if ball.x == START_X and ball.y == START_Y and count < 3:
        count += 1
        bounce()
        # Move the ball back to starting position
        ball.x = START_X
        ball.y = START_Y
    else:
        # Prevent users from interfering bouncing ball process by clicking
        pass


def bounce():
    """
    The ball has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    vertical_velocity = 0
    while ball.x <= window.width:
        ball.move(VX, vertical_velocity)
        vertical_velocity += GRAVITY
        if ball.y >= window.height-ball.height and vertical_velocity > 0:
            vertical_velocity *= -REDUCE
        pause(DELAY)


if __name__ == "__main__":
    main()
