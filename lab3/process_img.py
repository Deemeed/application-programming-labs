import cv2
import matplotlib.pyplot as plt
import numpy as np


def read_image(img: str) -> np.ndarray:

    """
    Read image from file
    :param img: Path to file to read image
    :return: Readed image
    """

    image = cv2.imread(img)

    return image

def print_size(image: np.ndarray) -> None:

    """
    Print size of image
    :param image: Original image
    :return: None
    """

    print(image.shape)

def create_histogram(image: np.ndarray) -> None:

    """
    Creating and printing the histogram of image
    :param image: Original image
    :return: None
    """

    color = ('blue', 'green', 'red')
    for i, col in enumerate(color):
        histr = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histr, label = col + ' channel', color=col)
        plt.xlim([0, 256])
    plt.title('Histogram')
    plt.xlabel("pixel's tone")
    plt.ylabel('frequency')
    plt.legend()
    plt.show()

def make_binary(img: str) -> np.ndarray:

    """
    Convert original image to binary
    :param img: Path to file to read image
    :return: Binary image
    """

    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    ret, bin_img = cv2.threshold(image,127,255,cv2.THRESH_BINARY)

    return bin_img

def print_difference(img: np.ndarray, bin_img: np.ndarray):

    """
    Print two different images to compare
    :param img: Original image
    :param bin_img: Binary image
    :return: None
    """

    cv2.imshow('Original image', img)
    cv2.waitKey(0)

    cv2.imshow('Binary image', bin_img)
    cv2.waitKey(0)

def save_image(file: str, img: np.ndarray) -> None:

    """
    Save image to file
    :param file: Path to file to save
    :param img: Image to save
    :return: None
    """

    cv2.imwrite(file, img)