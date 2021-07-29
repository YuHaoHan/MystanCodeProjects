"""
File: shrink.py
Author: David
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the filename of the image to be processed
    :return img: SimpleImage, the shrunk image
    """
    img = SimpleImage(filename)
    # Create a blank frame with shrunk size.
    shrink_img = SimpleImage.blank(img.width//2, img.height//2)
    # Loop the pixels of the original image by a step of 2.
    for x in range(0, img.width, 2):
        for y in range(0, img.height, 2):
            red_total = 0
            green_total = 0
            blue_total = 0
            count = 0
            # Loop the pixels in a 2*2 square whose upper left position is (x, y)
            for x1 in range(x, x+2):
                for y1 in range(y, y+2):
                    """
                    Because I am not sure if the width and the height are even or odd, 
                    I add this if condition to fit in with image of any size.
                    """
                    if 0 <= x1 < img.width and 0 <= y1 < img.height:
                        img_p = img.get_pixel(x1, y1)
                        count += 1
                        red_total += img_p.red
                        green_total += img_p.green
                        blue_total += img_p.blue
            # Calculate the average of the pixels in the square and put them into the blank frame.
            shrink_img_p = shrink_img.get_pixel(x/2, y/2)
            shrink_img_p.red = red_total // count
            shrink_img_p.green = green_total // count
            shrink_img_p.blue = blue_total // count
    return shrink_img
            

def main():
    """
    This program shrinks the image in the x and y direction by a factor of 2.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
