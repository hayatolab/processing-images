from functions import *
import os

absolute_path = os.path.join(os.getcwd(), 'images')

# Images path
car = absolute_path + '/car.png'
crowd = absolute_path + '/crowd.png'
image1 = absolute_path + '/Image1.pgm'
test80 = absolute_path + '/test80.jpg'
university = absolute_path + '/university.png'


def question_2():
    # Read images
    img1 = cv.imread(car)
    img2 = cv.imread(crowd)
    img3 = cv.imread(university)

    # Question 2.1

    # PowerLaw
    power_law(ImageType(img1, "q2/2.1", "car"), [1.7, 2.0, 2.3, 0.9, 0.8, 0.7])
    power_law(ImageType(img2, "q2/2.1", "crowd"),
              [1.7, 2.0, 2.3, 0.9, 0.8, 0.7])
    power_law(ImageType(img3, "q2/2.1", "university"),
              [1.7, 2.0, 2.3, 0.9, 0.8, 0.7])

    # Question 2.2

    hist_eq(ImageType(img1, "q2/2.2", "car"))
    hist_eq(ImageType(img2, "q2/2.2", "crowd"))
    hist_eq(ImageType(img3, "q2/2.2", "university"), True)
