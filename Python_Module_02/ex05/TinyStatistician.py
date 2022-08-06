import numpy

# todo: didn't do anything for array and numpy


class TinyStatistician(object):

    def __init__(self):
        pass

    def mean(self, x):
        sum = 0
        if x == []:
            return None
        for item in x:
            sum += item
        return float(sum / len(x))

    def median(self, x):
        if x == []:
            return None
        if len(x) == 1:
            return float(x[0])
        tmp = x[:]
        tmp.sort()
        if (len(tmp) % 2 == 0):
            return float((tmp[int(len(tmp) / 2)] + tmp[int(len(tmp) / 2) + 1])
                         / 2)
        else:
            return float(tmp[int(len(tmp) / 2)])

    def quartile(self, x):
        tmp = x[:]
        tmp.sort()
        median_val = self.median(x)
        # print("tmp", [i for i in tmp if i <= median_val],
        #       [i for i in tmp if i >= median_val])
        if (len(x) % 2 == 0):
            return [self.median(tmp[0:int(len(tmp) / 2)]),
                    self.median(tmp[int(len(tmp) / 2):len(tmp)])]
        else:
            return [self.median(tmp[0:int(len(tmp) / 2) + 1]),
                    self.median(tmp[int(len(tmp) / 2): len(tmp)])]

    def var(self, x):
        mean = self.mean(x)
        sum = 0
        for item in x:
            sum += (item - mean) ** 2
        return sum / len(x)

    def std(self, x):
        return self.var(x)**(1/2)


if __name__ == "__main__":

    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    print(tstat.mean(a))
    # Expected result: 82.4
    print(tstat.median(a))
    # Expected result: 42.0
    b = [1, 42, 300, 10, 59, 60, 11, 12]
    print("a", tstat.quartile(a))
    print("b", tstat.quartile(b))
    # Expected result: [10.0, 59.0]
    print(tstat.var(a))
    # Expected result: 12279.439999999999
    print(tstat.std(a))
    # Expected result: 110.81263465868862
