import numpy


class NumpyCreator:

    def __init__(self) -> None:
        pass

    def from_list(self, lst):
        return numpy.array(lst)

    def from_tuple(self, tpl):
        return numpy.asarray(tpl)

    def from_iterable(self, itr):
        return numpy.fromiter(itr, dtype=int)

    def from_shape(self, shape, value=0):
        return numpy.full(shape=shape, fill_value=value, dtype=int)

    def random(self, shape):
        return numpy.random.rand(shape[0], shape[1])

    def identity(self, n):
        return numpy.identity(n)


if __name__ == "__main__":
    npc = NumpyCreator()
    print(npc.from_list([[1, 2, 3], [6, 3, 4]]))
    print(npc.from_list([[1, 2, 3], [6, 4]]))
