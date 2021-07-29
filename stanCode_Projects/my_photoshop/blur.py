"""
File: blur.py
Author: David
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, the image to be blurred
    :return: SimpleImage, the blurred image
    """
    # Create a blank frame for blurred pixels.
    blur_img = SimpleImage.blank(img.width, img.height)
    # Loop the original image.
    for x in range(img.width):
        for y in range(img.height):
            # Set up variables for pixels to be processed.
            red_total = 0
            green_total = 0
            blue_total = 0
            """
            Because the number of pixels to be processed is not sure, 
            I create a variable, count, to calculate how many pixels are added in the process. 
            """
            count = 0
            # Loop the pixels to be processed (pixels in the style box while the designated pixel at the middle)
            for x1 in range(x-1, x+2):
                for y1 in range(y-1, y+2):
                    """
                    I wrote this if condition to ensure some special cases, like corners and sides,
                    will not fail during the calculation.
                    """
                    if 0 <= x1 < img.width and 0 <= y1 < img.height:
                        img_p = img.get_pixel(x1, y1)
                        count += 1
                        red_total += img_p.red
                        green_total += img_p.green
                        blue_total += img_p.blue
            # Calculate the average of the pixels in the style box and put them into the blank frame.
            blur_img_p = blur_img.get_pixel(x, y)
            blur_img_p.red = red_total//count
            blur_img_p.green = green_total//count
            blur_img_p.blue = blue_total//count
    return blur_img


def main():
    """
    This program blurs the smiley-face image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    # Blur the image for 5 times.
    blurred_img = blur(old_img)
    for i in range(4):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
