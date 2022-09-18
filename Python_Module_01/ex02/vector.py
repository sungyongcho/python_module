
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
        # a list of a list of floats: Vector([[0.0, 1.0, 2.0, 3.0]]),
        # • a list of lists of single float: Vector([[0.0], [1.0], [2.0], [3.0]]),
        # • a size: Vector(3) -> the vector will have values = [[0.0], [1.0], [2.0]],
        # • a range: Vector((10,16)) -> the vector will have values = [[10.0], [11.0],
        #            [12.0], [13.0], [14.0], [15.0]]. in Vector((a,b)), if a > b, you must display accurate error message
        ##
        if (isinstance(values, int)):
            if (values < 0):
                raise ValueError(
                    "Vector must be initialized with appropriate data (int, negative)")
            self.values = []
            for i in range(values):
                self.values.append([float(i)])
        elif (isinstance(values, tuple)):
            if not (len(values) == 2):
                raise ValueError(
                    "Vector must be initialized with appropriate data (tuple, length)")
            if not (isinstance(values[0], int) and isinstance(values[1], int)):
                raise ValueError(
                    "Vector must be initialized with appropriate data (tuple, data type)")
            if not (values[0] < values[1]):
                raise ValueError(
                    "Vector must be initialized with appropriate data (tuple, range)")
            self.values = []
            for i in range(values[0], values[1]):
                self.values.append([float(i)])
        elif not (any(isinstance(i, list) for i in values) and isinstance(values, list)):
            raise TypeError("vector must be initialized with appropriate data")
        else:
            for list_inside in values:
                for j in list_inside:
                    if not (isinstance(j, float)):
                        raise TypeError("The element must be float type")

            self.values = values

        if len(self.values) == 1:
            # print(len(values[0]))
            self.shape = (1, len(self.values[0]))
        else:
            # print(len(values))
            self.shape = (len(self.values), 1)

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
