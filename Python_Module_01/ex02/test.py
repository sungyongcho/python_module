from re import I
from vector import Vector

# todo:
# clean up tester

# row vector
print("# row vector")
print("")
print(Vector([[1., 2.]]).shape)
print(Vector([[1., 2.]]).values)
print()
print("#column vector")
print()
print(Vector([[1.], [2.], [3.]]).shape)
print(Vector([[1.], [2.], [3.]]).values)
print()


print("# dot product")
print("# row")
print()
print(Vector([[1., 2.0]]).dot(Vector([[5., 2.0]])))
print()
print("#column")
print()
print(Vector([[2.0], [3.0]]).dot(Vector([[2.0], [3.0]])))
print()
print(Vector([[3.0]]).dot(Vector([[4.0]])))
print()
print("# T")
print()
print(Vector([[12.0, 34.0]]).T().values)
print(Vector([[56.0], [78.0]]).T().values)

print()
print("# add, radd")
print()
a = Vector([[1., 2., 3.]]) + Vector([[4., 5., 6.]])
print(a.values)
aa = Vector([[1.], [2.], [3.]]) + Vector([[4.], [5.], [6.]])
print(aa.values)

# a = Vector([[1., 2., 3.]]) + 4
# print(a.values)

b = Vector([[4., 5., 6.]])

c = Vector([[7., 8., 9.]]) + b
print(c.values)

d = b + Vector([[7., 8., 9.]])
print(d.values)

# sub, rsub

e = Vector([[1., 2., 3.]]) - Vector([[4., 5., 6.]])
print(d.values)

ee = Vector([[1.], [2.], [3.]]) - Vector([[4.], [5.], [6.]])
print(ee.values)

f = Vector([[4., 5., 6.]])

g = Vector([[7., 8., 9.]]) - f
print(g.values)

h = f - Vector([[7., 8., 9.]])
print(h.values)

# truediv

i = Vector([[1., 2., 3.]]) / 3

j = Vector([[4.], [5.], [6.]]) / 3

# truediv with NotImplementedError (uncomment to test)

# ii =  Vector([[1., 2., 3.]]) / Vector([[1., 2., 3.]])

print(i.values)
print(j.values)

# rtruediv (uncomment to test)

# k =  3 / Vector([[1., 2., 3.]])

# l = 3 / Vector([[4.], [5.], [6.]])


# mul, rmul

m = Vector([[1., 2., 3.]]) * 3

n = Vector([[4.], [5.], [6.]]) * 3

# mul with NotImplementedError (uncomment to test)

# mm = Vector([[1., 2., 3.]]) * Vector([[1., 2., 3.]])

print(m.values)
print(n.values)


mm = 3 * Vector([[7., 8., 9.]])

nn = 3 * Vector([[10.], [11.], [12.]])

print(mm.values)
print(nn.values)

# str, repr
# must be identical, i.e we expect that print(vector) and vector within python interpretor behave the same, see correspond

v1 = Vector([[0.0], [1.0], [2.0], [3.0]])

print(v1)
print(repr(v1))
