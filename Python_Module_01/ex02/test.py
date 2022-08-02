from re import I
from vector import Vector

# row vector
print(Vector([[1., 2.]]).shape)

# column vector
print(Vector([[1.], [2.], [3.]]).shape)


# dot product

# row
print(Vector([[1., 2.0]]).dot(Vector([[5., 2.0]])))

# column
print(Vector([[2.0], [3.0]]).dot(Vector([[2.0], [3.0]])))


print(Vector([[3.0]]).dot(Vector([[4.0]])))

print(Vector([[12.0, 34.0]]).T().values)

print(Vector([[56.0], [78.0]]).T().values)
