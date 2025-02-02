from ImageProcessor import ImageProcessor
import numpy as np

# ref:
# https://numpy.org/devdocs/user/basics.indexing.html#dimensional-indexing-tools


class ColorFilter:

    def __init__(self) -> None:
        pass

    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        copy = np.copy(array)
        # ref: https://stackoverflow.com/questions/47382482/inverting-pixels-of-an-rgb-image-in-python
        copy[:, :, :3] = 1 - copy[:, :, :3]
        return copy

    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        copy = np.zeros(array.shape)
        copy[:, :, 2:] = array[:, :, 2:]
        return copy

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        copy = np.copy(array)
        copy[..., : 3:2] = copy[..., : 3:2] * 0
        return copy

    def to_red(self, array):
        """
            Applies a red filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        copy = np.copy(array)
        copy = copy - (self.to_blue(array) + self.to_green(array))
        copy[..., 3:] = array[..., 3:]
        return copy

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
            celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """

    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = ’mean’/’m’: performs the mean of RBG channels.
        For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
            filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
            weights: [kwargs] list of 3 floats where the sum equals to 1,
                        corresponding to the weights of each RBG channels.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """


if __name__ == "__main__":
    ip = ImageProcessor()
    arr = ip.load("./elon_canaGAN.png")
    print(arr)
    cf = ColorFilter()
    ip.display(cf.to_red(arr))
