"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO: This program integrates a group of images to create a photo without passerby.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (float): color distance between red, green, and blue pixel values

    """
    p_green = pixel.green
    p_red = pixel.red
    p_blue = pixel.blue
    # Calculate distance of color
    dist = ((p_green-green)**2+(p_red-red)**2+(p_blue-blue)**2)**0.5
    return float(dist)


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    rgb = []
    r_sum = 0
    g_sum = 0
    b_sum = 0
    count = 0
    # Calculate the sum of given pixels.
    for pixel in pixels:
        count += 1
        r_sum += pixel.red
        g_sum += pixel.green
        b_sum += pixel.blue
    # Average
    rgb.append(int(r_sum/count))
    rgb.append(int(g_sum/count))
    rgb.append(int(b_sum/count))
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    avg = get_average(pixels)
    # The smallest distance of color
    min_dist = float("inf")
    # The pixel corresponding to the smallest distance of color
    best_pixel = pixels[0]
    for i in range(len(pixels)):
        pixel = pixels[i]
        dist = get_pixel_dist(pixel, avg[0], avg[1], avg[2])
        if dist < min_dist:
            min_dist = dist
            best_pixel = pixel
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    # Loop over every pixel
    for i in range(width):
        for j in range(height):
            pixels = []
            for img in images:
                img_p = img.get_pixel(i, j)
                pixels.append(img_p)
            result_pixel = result.get_pixel(i, j)
            # Get best pixel
            best = get_best_pixel(pixels)
            result_pixel.red = best.red
            result_pixel.green = best.green
            result_pixel.blue = best.blue
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
