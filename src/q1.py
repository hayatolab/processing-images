from functions import *
import os

absolute_path = os.path.join(os.getcwd(), 'images')

# Images path
car = absolute_path + '/car.png'
test80 = absolute_path + '/test80.jpg'


def question_1():
    # Question 1.1

    # Read image
    img = cv.imread(car)

    # My Interpolation
    dec_int(ImageType(img, "q1/1.1", "car"))

    # Question 1.3

    # Read image
    img = cv.imread(test80)

    # My Interpolation
    dec_int(ImageType(img, "q1/1.3", "test80"))

    width = int(img.shape[1]/2)
    height = int(img.shape[0]/2)

    # CV2 Resize
    resize_img = cv.resize(img, dsize=(width, height),
                           interpolation=cv.INTER_NEAREST)
    cv.imwrite("q1/1.3/cv-test80-resized.png", resize_img)

    # CV2 Interpolation
    new_img = cv.resize(resize_img, dsize=(img.shape[1], img.shape[0]),
                        interpolation=cv.INTER_CUBIC)

    # CV2 Save Interpolation
    cv.imwrite("q1/1.3/cv-test80-interpolated.png", new_img)

    image = cv.imread(car)

    kernel1 = np.array([[0, -1, 0],
                        [-1, 5, -1],
                        [0, -1, 0]])

    identity = cv.filter2D(src=image, ddepth=-1, kernel=kernel1)

    # cv.imshow('Original', image)
    # cv.imshow('Identity', identity)
    # cv.waitKey()
    # cv.imwrite('identity.jpg', identity)
    # cv.destroyAllWindows()
