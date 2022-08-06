from hashlib import new
import numpy as np


class ScrapBooker():
    def __init__(self) -> None:
        pass

    # within the class
    def crop(self, array, dim, position=(0, 0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        -----
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Return:
        -------
        new_arr: the cropped numpy.ndarra  y.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        if position[0] + dim[0] > len(array) or \
                position[1] + dim[1] > len(array[0]):
            return None
        return array[int(position[0]):int(position[0]+dim[0]),
                     int(position[1]):int(position[1]+dim[1])]

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
        Args:
        -----
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Return:
        -------
        new_arr: thined numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        new_arr = array[:]

        new_arr = np.delete(new_arr, np.arange(
            n - 1, new_arr[0].size, n), 1 if axis is 0 else 0)
        return new_arr

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Return:
        -------
        new_arr: juxtaposed numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or not isinstance(n, int) or n <= 0 or axis not in (0, 1):
            return None
        if axis:
            return np.tile(array, (1, n))
        else:
            return np.tile(array, (n, 1))

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Return:
        -------
        new_arr: mosaic numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or not isinstance(dim, tuple):
            return None
        if not isinstance(dim[0], int) or not isinstance(dim[1], int) or dim[0] <= 0 or dim[1] <= 0:
            return None
        return np.tile(array, dim)


if __name__ == "__main__":
    spb = ScrapBooker()
    arr1 = np.arange(0, 25).reshape(5, 5)
    print(arr1)
    print(spb.crop(arr1, (3, 1), (1, 0)))

    arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1, 9)
    print(spb.thin(arr2, 3, 0))

    arr3 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    print(spb.juxtapose(arr3, 3, 1))

    arr4 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print(spb.mosaic(arr4, (2, 5)))
