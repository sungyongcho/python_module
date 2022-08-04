import numpy

##todo: didn't do anything for array and numpy

class TinyStatistician(object):

    def __init__(self):
        pass

    def mean(self, x):
        if x == []:
            return None
        if isinstance(x, numpy.ndarray):
            return numpy.sum(x) / x.size
        return sum(x) / len(x)

    def median(self, x):
        if x == []:
            return None
        if len(x) == 1:
            return float(x[0])
        return float(sorted(x)[int(len(x) / 2 - 1) + (1 if len(x) % 2 is not 0 else 0)])

    def quartile(self, x):
        print("c", x)

    def var(self, x):
        print("d", x)

    def std(self, x):
        print("e", x)


if __name__ == "__main__":

    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    print(tstat.mean(a))
    # Expected result: 82.4
    print(tstat.median(a))
    print(tstat.median([0,1]))
    # Expected result: 42.0
    tstat.quartile(a)
    # Expected result: [10.0, 59.0]
    tstat.var(a)
    # Expected result: 12279.439999999999
    tstat.std(a)
    # Expected result: 110.81263465868862
