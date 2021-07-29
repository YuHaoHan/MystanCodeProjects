"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.3

# Controls the upper bound for black pixel
BLACK_PIXEL = 120


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, the background image
    :param figure_img: SimpleImage, green screen figure image
    :return: SimpleImage, the green screen pixels are replaced by pixels of background image
    """
    # Make the size of background image as big as figure image.
    background_img.make_as_big_as(figure_img)
    for y in range(background_img.height):
        for x in range(background_img.width):
            pixel = figure_img.get_pixel(x, y)
            avg = (pixel.red + pixel.blue + pixel.green) // 3
            total = pixel.red + pixel.blue + pixel.green
            """
            The definition of green screen is the green pixel is bigger than 
            the average of RGB pixels. To accurately show the figure's hair,
            the total of the RGB pixels has to be larger than the BLACK_PIXEL.
            """
            if pixel.green > avg*THRESHOLD and total > BLACK_PIXEL:
                b_pixel = background_img.get_pixel(x, y)
                pixel.red = b_pixel.red
                pixel.green = b_pixel.green
                pixel.blue = b_pixel.blue
    return figure_img


def main():
    """
    This function conducts green screen replacement
    which is able to photoshop a person onto any background
    創作理念：我就爛迷因
    """
    background = SimpleImage("images/background.jpg")
    figure = SimpleImage("images/figure.jpg")
    result = combine(background, figure)
    result.show()


if __name__ == '__main__':
    main()
