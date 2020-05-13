"""
This program generates the Warhol effect based on the original image.
"""
from random import uniform

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    final_image = draw_patches()
    final_image.show()


def draw_patches():
    image = SimpleImage(PATCH_NAME)
    width = image.width
    height = image.height
    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    for col in range(N_COLS):
        for row in range (N_ROWS):
            image = make_recolored_patch(uniform(0,1.4),uniform(0,1.4),uniform(1,1.4))
            for y in range(height):
                for x in range(width):
                    pixel = image.get_pixel(x, y)
                    final_image.set_pixel(x + width * col, y + height * row , pixel)
    return final_image



def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch






if __name__ == '__main__':
    main()
