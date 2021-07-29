"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program deliver a well-known game named breakout.
Player can only use a paddle to hit a ball in order to break all the bricks, and
player has only two chances to let the ball fly over the paddle.
"""

from campy.gui.events.timer import pause
from breakoutgraphics_extension import BreakoutGraphics
from campy.graphics.gobjects import GLabel

FRAME_RATE = 1000 / 120  # 120 frames per second


def main():
    """
    I use a class named BreakoutGraphics to construct this game.
    Game-ending conditions: player breaks all the bricks or player leaves zero live.
    """

    graphics = BreakoutGraphics()

    # Add animation loop here!
    dx = 0
    dy = 0
    lives = graphics.get_lives()

    while True:
        if dy == 0 and graphics.game_has_started():
            graphics.set_ball()
            dx = graphics.get_dx()
            dy = graphics.get_dy()
        pause(FRAME_RATE)
        graphics.ball.move(dx, dy)
        if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width-graphics.ball.width:
            dx = -dx
        if graphics.ball.y <= 0:
            dy = -dy
        if graphics.ball.y >= graphics.window.height-graphics.ball.height:
            lives -= 1
            graphics.lives_label.text = "Lives :" + str(lives)
            if lives > 0:
                dx = 0
                dy = 0
                graphics.reset_ball()
            else:
                graphics.lose_game()
                break
        if graphics.collide():
            if graphics.is_paddle() and dy > 0:
                dy = -dy
            elif not graphics.is_paddle():
                dy = -dy
                graphics.brick_out()
        if graphics.win():
            graphics.win_game()
            break


if __name__ == '__main__':
    main()
