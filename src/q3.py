from functions import *
import os

absolute_path = os.path.join(os.getcwd(), 'images')

# Image path
image1 = absolute_path + '/Image1.pgm'


def question_3():
    # Read image
    image = cv.imread(image1)

    # Question 3.1
    laplace(ImageType(image, "q3/3.1", "image1"), 1)

    # Question 3.2
    laplace(ImageType(image, "q3/3.2", "image1"), 2)

    # Question 3.3
    laplace(ImageType(image, "q3/3.3", "image1"), 3)
