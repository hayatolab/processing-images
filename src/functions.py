import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


class ImageType:
    def __init__(self, image, folder_path, name_image):
        self.image = image
        self.folder_path = folder_path
        self.name_image = name_image


def dec_int(image: ImageType):
    # Resize
    scale = 0.5

    original_width = image.image.shape[0]
    original_height = image.image.shape[1]

    width = int(original_width*scale)
    height = int(original_height*scale)

    xNearestNeighbour = width/(original_width-1)
    yNearestNeighbour = height/(original_height-1)

    imageResized = np.zeros([width, height, 3])

    for i in range(width-1):
        for j in range(height-1):
            imageResized[i + 1, j + 1] = image.image[1 + int(i / xNearestNeighbour),
                                                     1 + int(j / yNearestNeighbour)]

    cv.imwrite(image.folder_path + "/" + image.name_image +
               "-resized.png", imageResized)

    # Interpolation
    original_width = imageResized.shape[0]
    original_height = imageResized.shape[1]

    width = int(original_width*2)
    height = int(original_height*2)

    xNearestNeighbour = width/(original_width-1)
    yNearestNeighbour = height/(original_height-1)

    imageInterpolated = np.zeros([width, height, 3])

    for i in range(width-1):
        for j in range(height-1):
            imageInterpolated[i + 1, j + 1] = imageResized[1 + int(i / xNearestNeighbour),
                                                           1 + int(j / yNearestNeighbour)]

    cv.imwrite(image.folder_path + "/" + image.name_image +
               "-interpolated.png", np.hstack((image.image, imageInterpolated)))


def egde_improv():
    return


def power_law(image: ImageType, values):
    for gamma in values:
        # Apply gamma correction.
        gamma_corrected = np.array(
            255*(image.image / 255) ** gamma, dtype='uint8')
        # Save edited images.
        cv.imwrite(image.folder_path + "/" + image.name_image +
                   '-gamma_transformed'+str(gamma)+'.png', np.hstack((image.image, gamma_corrected)))
    return


def hist_eq(image: ImageType, showCdf=False):
    image.image = cv.cvtColor(image.image, cv.COLOR_BGR2GRAY)
    hist_corrected = cv.equalizeHist(image.image)

    # Save edited images.
    cv.imwrite(image.folder_path + "/" + image.name_image +
               '-equalized.png', np.hstack((image.image, hist_corrected)))

    if(showCdf):
        # Original Image
        hist, bins = np.histogram(image.image.flatten(), 256, [0, 256])
        cdf = hist.cumsum()
        cdf_normalized = cdf * float(hist.max()) / cdf.max()
        plt.plot(cdf_normalized, color='b')
        plt.hist(image.image.flatten(), 256, [0, 256], color='r')
        plt.xlim([0, 256])
        plt.grid()
        plt.title('Antes - Histograma e CDF ')
        plt.legend(('cdf', 'histogram'), loc='upper left')
        plt.savefig(image.folder_path + "/" + image.name_image +
                    '-before.png')
        plt.close()

        # Equalized Image
        hist, bins = np.histogram(hist_corrected.flatten(), 256, [0, 256])
        cdf = hist.cumsum()
        cdf_normalized = cdf * float(hist.max()) / cdf.max()
        plt.plot(cdf_normalized, color='b')
        plt.hist(hist_corrected.flatten(), 256, [0, 256], color='r')
        plt.xlim([0, 256])
        plt.grid()
        plt.title('Depois - Histograma e CDF ')
        plt.legend(('cdf', 'histogram'), loc='upper left')
        plt.savefig(image.folder_path + "/" + image.name_image +
                    '-after.png')
        plt.close()
    return


def laplace(image: ImageType, filterType: int):

    # Question 3.1
    if(filterType == 1):
        kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
        dst = cv.filter2D(image.image, cv.CV_16S, kernel)
    # Question 3.2
    elif(filterType == 2):
        gaussian = cv.GaussianBlur(image.image, (3, 3), 0.5)
        kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
        dst = cv.filter2D(gaussian, cv.CV_16S, kernel)
    # Question 3.3
    else:
        gaussian = cv.GaussianBlur(image.image, (3, 3), 1)
        kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
        dst = cv.filter2D(gaussian, cv.CV_16S, kernel)

    # Save edited images.
    cv.imwrite(image.folder_path + "/" + image.name_image +
               '-filtered.png', np.hstack((image.image, dst)))
    return
