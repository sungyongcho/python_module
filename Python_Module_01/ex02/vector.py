
import operator

ops = {"+": operator.add,
       "-": operator.sub,
       "*": operator.mul,
       "/": operator.truediv}

# todo:
# exeception handling for elements of vector
# raise NotImplemented for vector * vector


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

    def _dot_row(self, vector):
        output = 0
        for i in range(0, max(self.shape)):
            output += (self.values[0][i] * vector.values[0][i])
        return output

    def _dot_column(self, vector):
        output = 0
        for i in range(0, max(self.shape)):
            output += (self.values[i][0] * vector.values[i][0])
        return output

    def dot(self, vector):
        if (self.shape != vector.shape):
            raise ValueError("the shape must be the same")
        dimension_check = self.shape.index(max(self.shape))
        if dimension_check == 1:
            return self._dot_row(vector)
        else:
            return self._dot_column(vector)

    def _T_row_to_col(self):
        tmp = []
        for i in range(0, max(self.shape)):
            tmp.append([self.values[0][i]])
        return Vector(tmp)

    def _T_col_to_row(self):
        tmp = []
        for i in range(0, max(self.shape)):
            tmp.append(self.values[i][0])
        return Vector([tmp])

    def T(self):
        dimension_check = self.shape.index(max(self.shape))
        if (self.shape == (1, 1)):
            return self
        if dimension_check == 1:
            return self._T_row_to_col()
        else:
            return self._T_col_to_row()

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("only vector can add to each other")
        if (self.shape != other.shape):
            raise ValueError("only vector of same shape is allowed")
        dimension_check = self.shape.index(max(self.shape))
        tmp = []
        if dimension_check == 1:
            for i in range(0, max(self.shape)):
                tmp.append(self.values[0][i] + other.values[0][i])
            return Vector([tmp])
        else:
            for i in range(0, max(self.shape)):
                tmp.append([self.values[i][0] + other.values[i][0]])
            return Vector(tmp)

    def __radd__(self, other):
        return other + self

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("only vector can add to each other")
        if (self.shape != other.shape):
            raise ValueError("only vector of same shape is allowed")
        dimension_check = self.shape.index(max(self.shape))
        tmp = []
        if dimension_check == 1:
            for i in range(0, max(self.shape)):
                tmp.append(self.values[0][i] - other.values[0][i])
            return Vector([tmp])
        else:
            for i in range(0, max(self.shape)):
                tmp.append([self.values[i][0] - other.values[i][0]])
            return Vector(tmp)

    def __rsub__(self, other):
        return other - self

    def __row_loop(self, var, operator):
        tmp = []
        for i in range(0, max(self.shape)):
            tmp.append(ops[operator](self.values[0][i], var))
        return Vector([tmp])

    def __col_loop(self, var, operator):
        tmp = []
        for i in range(0, max(self.shape)):
            tmp.append([ops[operator](self.values[i][0], var)])
        return Vector(tmp)

    def col_loop(self, other, operator):
        tmp = []
        for i in range(0, max(self.shape)):
            tmp.append([ops[operator](self.values[0][i], other.values[0][i])])
        return Vector([tmp])

    def __truediv__(self, var):
        if isinstance(var, Vector):
            raise NotImplementedError(
                "Division of a Vector by a Vector is not implemented here.")
        if not any([isinstance(var, t) for t in [float, int, complex]]):
            raise ValueError("division only accepts scalar. (real number)")
        dimension_check = self.shape.index(max(self.shape))
        if dimension_check == 1:
            return self.__row_loop(var, "/")
        else:
            return self.__col_loop(var, "/")

    def __rtruediv__(self, var):
        raise NotImplementedError(
            "Division of a scalar by a Vector is not implemented here.")

    def __mul__(self, var):
        if isinstance(var, Vector):
            raise NotImplementedError(
                "Multiplication of a Vector by a Vector is not implemented here.")
        if not any([isinstance(var, t) for t in [float, int, complex]]):
            raise ValueError(
                "multiplication only accepts scalar. (real number)")
        dimension_check = self.shape.index(max(self.shape))
        if dimension_check == 1:
            return self.__row_loop(var, "*")
        else:
            return self.__col_loop(var, "*")

    def __rmul__(self, var):
        return self * var

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return str(self.values)
