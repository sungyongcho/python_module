
from typing import Type


# todo:
# exeception handling for elements of vector

class Vector:

    def __init__(self, values):
        if not (any(isinstance(i, list) for i in values) or isinstance(values, list)):
            raise TypeError("vector must have a list given")
        else:
            for list_inside in values:
                for j in list_inside:
                    if not (isinstance(j, float)):
                        raise TypeError("The element must be float type")

            self.values = values

        if len(values) == 1:
            # print(len(values[0]))
            self.shape = (1, len(values[0]))
        else:
            # print(len(values))
            self.shape = (len(values), 1)

    def dot_row(self, vector):
        output = 0
        for i in range(0, max(self.shape)):
            output += (self.values[0][i] * vector.values[0][i])
        return output

    def dot_column(self, vector):
        output = 0
        for i in range(0, max(self.shape)):
            output += (self.values[i][0] * vector.values[i][0])
        return output

    def dot(self, vector):
        if (self.shape != vector.shape):
            raise ValueError("the shape must be the same")
        dimension_check = self.shape.index(max(self.shape))
        if dimension_check == 1:
            return self.dot_row(vector)
        else:
            return self.dot_column(vector)

    def T_row_to_col(self):
        tmp = []
        for i in range(0, max(self.shape)):
            tmp.append([self.values[0][i]])
        return Vector(tmp)

    def T_col_to_row(self):
        tmp = []
        for i in range(0, max(self.shape)):
            tmp.append(self.values[i][0])
        return Vector([tmp])

    def T(self):
        dimension_check = self.shape.index(max(self.shape))
        if (self.shape == (1, 1)):
            return self
        if dimension_check == 1:
            return self.T_row_to_col()
        else:
            return self.T_col_to_row()
