import cv2
import numpy as np


class ImageProcessor():

    def __init__(self) -> None:
        pass

    def load(self, path):
        try:
            im = cv2.imread(path)
            print("Loading image of dimensions", im.shape[0], "x", im.shape[1])
            image_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            return np.divide(image_rgb[:, :, 0:3], 255)
        except Exception as e:
            print(f"Exception : {e.__class__.__name__} -- strerror: {e}")
        return None

    def display(self, array):
        array = np.multiply(array, 255)
        array = array.astype(np.uint8)

        image_rgb = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
        cv2.imshow('loaded image', image_rgb)
        cv2.waitKey(0)

