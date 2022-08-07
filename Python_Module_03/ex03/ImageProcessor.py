import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.image as mpimg
import numpy as np


class ImageProcessor():

    def __init__(self) -> None:
        pass

    def load(self, path):
        try:
            im = mpimg.imread(path)
            print("Loading image of dimensions", im.shape[0], "x", im.shape[1])
            return im
        except Exception as e:
            print(f"Exception : {e.__class__.__name__} -- strerror: {e}")
        return None

    def display(self, array):
        # tmp = np.multiply(array[:, :, 0:3], 255)
        # img = Image.fromarray(array, 'RGB')

        plt.figure('loaded image')
        plt.imshow(array)
        plt.axis('off')
        plt.show()
