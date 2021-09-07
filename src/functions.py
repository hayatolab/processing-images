import numpy as np
import cv2 as cv


def dec_int(image, folder_path, name_image):
    # Resize
    scale = 0.5

    original_width = image.shape[0]
    original_height = image.shape[1]

    width = int(original_width*scale)
    height = int(original_height*scale)

    xNearestNeighbour = width/(original_width-1)
    yNearestNeighbour = height/(original_height-1)

    imageResized = np.zeros([width, height, 3])

    for i in range(width-1):
        for j in range(height-1):
            imageResized[i + 1, j + 1] = image[1 + int(i / xNearestNeighbour),
                                               1 + int(j / yNearestNeighbour)]

    cv.imwrite(folder_path + "/" + name_image + "-resized.png", imageResized)

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

    cv.imwrite(folder_path + "/" + name_image +
               "-interpolated.png", imageInterpolated)


def egde_improv():
    return
