"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

This program set up a class to help construct a breakout game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.
NUM_LIVES = 3          # Number of lives


class BreakoutGraphics:

    def __init__(self, num_lives = NUM_LIVES, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (self.window.width-self.paddle.width)/2, self.window.height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        # Default initial velocity for the ball
        self.__dy = 0
        self.__dx = 0
        # Four corner of the ball.
        self.upper_left = None
        self.upper_right = None
        self.lower_left = None
        self.lower_right = None
        # Points
        self.__point = 0
        self.score_label = GLabel("Score: " + str(self.__point))
        self.score_label.color = "green"
        self.score_label.font = "-25"
        self.window.add(self.score_label, 10, self.window.height)
        # Lives
        self.lives = num_lives
        self.lives_label = GLabel("Lives :" + str(self.lives))
        self.lives_label.color = "red"
        self.lives_label.font = "-25"
        self.window.add(self.lives_label, 130, self.window.height)
        # White board used in the end of a game.
        self.white_board = GRect(self.window.width, self.window.height)
        self.white_board.filled = True
        self.white_board.fill_color = "white"

        # Initialize our mouse listeners
        onmouseclicked(self.start_game)
        onmousemoved(self.paddle_move)
        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if i == 0 or i == 1:
                    self.brick.fill_color = "red"
                elif i == 2 or i == 3:
                    self.brick.fill_color = "orange"
                elif i == 4 or i == 5:
                    self.brick.fill_color = "yellow"
                elif i == 6 or i == 7:
                    self.brick.fill_color = "green"
                else:
                    self.brick.fill_color = "blue"
                x_spacing = self.brick.width + brick_spacing
                y_spacing = self.brick.height + brick_spacing
                self.window.add(self.brick, x_spacing*j, brick_offset+y_spacing*i)
        # Create starting view
        self.title = GLabel("Welcome to Breakout !")
        self.title.font = "-30"
        self.window.add(self.title, (self.window.width-self.title.width)/2, self.window.height//2)
        self.author = GLabel("Author: David Han")
        self.author.font = "-25"
        self.window.add(self.author, (self.window.width-self.author.width)/2, self.window.height//1.8)
        self.start_button = GRect(self.window.width//3, self.window.height//7)
        self.start_button.filled = True
        self.start_button.fill_color = "blue"
        self.window.add(self.start_button, (self.window.width-self.start_button.width)/2, self.window.height//1.5)
        self.start_word = GLabel("Click to start")
        self.start_word.color = "white"
        self.start_word.font = "-20"
        self.window.add(self.start_word, (self.window.width-self.start_word.width)/2,
                        self.start_button.y+self.start_button.height/2+self.start_word.height/2)

    def paddle_move(self, m):
        """
        :param m: the position of player's mouse
        :return: the paddle's midpoint moves with player's mouse
        """
        if 0 + self.paddle.width/2 <= m.x <= self.window.width-self.paddle.width/2:
            self.paddle.x = m.x-self.paddle.width/2

    def set_ball_speed(self):
        """
        At the beginning of every round, set an initial speed for the ball.
        """
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def get_dx(self):
        """
        Getter of horizontal velocity
        """
        return self.__dx

    def get_dy(self):
        """
        Getter of vertical velocity
        """
        return self.__dy

    def game_has_started(self):
        """
        Determine if the game has started
        """
        if self.__dx == 0 and self.__dy == 0:
            return False
        return True

    def start_game(self, m):
        """
        When the game has not started and player click the start button, start the game.
        """
        if self.window.get_object_at(m.x, m.y) == self.start_button or self.window.get_object_at(m.x, m.y) == self.start_word:
            self.window.remove(self.title)
            self.window.remove(self.author)
            self.window.remove(self.start_button)
            self.window.remove(self.start_word)
        if self.window.get_object_at(self.start_button.x, self.start_button.y) is None \
                and not self.game_has_started():
            self.set_ball_speed()

    def collide(self):
        """
        Determine if the ball has collided with bricks or the paddle.
        """
        self.upper_left = self.window.get_object_at(self.ball.x, self.ball.y)
        self.upper_right = self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y)
        self.lower_left = self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.ball_radius)
        self.lower_right = self.window.get_object_at(self.ball.x + 2 * self.ball_radius,
                                                     self.ball.y + 2 * self.ball_radius)
        if self.upper_left is not None and self.upper_left is not self.score_label and self.upper_left is not self.lives_label:
            return True
        if self.upper_right is not None and self.upper_right is not self.score_label and self.upper_right is not self.lives_label:
            return True
        if self.lower_right is not None and self.lower_right is not self.score_label and self.lower_right is not self.lives_label:
            return True
        if self.lower_left is not None and self.lower_left is not self.score_label and self.lower_left is not self.lives_label:
            return True
        return False

    def is_paddle(self):
        """
        Determine if the ball has collided with the paddle.
        """
        if (self.upper_left is self.paddle or self.upper_right is self.paddle
                or self.lower_right is self.paddle or self.lower_left is self.paddle):
            return True
        return False

    def brick_out(self):
        """
        Remove the bricks hit by the ball.
        """
        if self.upper_left is not None:
            self.window.remove(self.upper_left)
            self.__point += 1
        if self.upper_right is not None and self.upper_right is not self.upper_left:
            self.window.remove(self.upper_right)
            self.__point += 1
        if self.lower_right is not None and self.lower_right is not self.upper_right:
            self.window.remove(self.lower_right)
            self.__point += 1
        if (self.lower_left is not None and self.lower_left is not self.lower_right
                and self.lower_left is not self.upper_left):
            self.window.remove(self.lower_left)
            self.__point += 1
        self.score_label.text = ("Score: " + str(self.__point))

    def set_ball(self):
        """
        Set ball position
        """
        self.window.add(self.ball, (self.window.width - self.ball.width) / 2,
                        (self.window.height - self.ball.height) / 2)

    def remove_ball(self):
        """
        Remove the ball from the window
        """
        self.window.remove(self.ball)

    def reset_ball(self):
        """
        When player lose a round and the number of lives is not zero, reset ball velocity and ball position.
        """
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        self.__dx = 0
        self.__dy = 0

    def get_point(self):
        """
        Getter of points.
        """
        return self.__point

    def win(self):
        """
        Winning condition
        """
        win_point = self.brick_rows*self.brick_cols
        if self.__point == win_point:
            return True
        return False

    def get_lives(self):
        """
        Getter of number of lives
        """
        return self.lives

    def lose_game(self):
        """
        When a player lose, show "You lose"
        """
        self.remove_ball()
        self.window.add(self.white_board)
        lose = GLabel("You lose")
        lose.font = "-50"
        self.window.add(lose, (self.window.width - lose.width) / 2, (self.window.height - lose.height) / 2)

    def win_game(self):
        """
        When a player win, show "You win !"
        """
        self.remove_ball()
        self.window.add(self.white_board)
        win = GLabel("You win !")
        win.font = "-50"
        self.window.add(win, (self.window.width - win.width) / 2, (self.window.height - win.height) / 2)



