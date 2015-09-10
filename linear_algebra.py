import math

class ShapeException(Exception):
    pass

def shape(thing):
    try:
        return len(thing), len(thing[1])
    except:
        return (len(thing), )


def shape_diff_exception(a, b):
    if shape(a) != shape(b):
        raise ShapeException("Vectors must be the same size")
    else:
        return True

def vector_add(a, b):
    shape_diff_exception(a,b)
    return [a[x]+b[x] for x in range(len(a))]


def vector_sub(a, b):
    shape_diff_exception(a,b)
    return [a[x]-b[x] for x in range(len(a))]


def vector_sum(*args):
    # total = args[0]
    # for vect in args[1:]:
    #     total = vector_add(total, vect)
    #     print(total)
    # return total

    if False in [shape(args[0]) == shape(x) for x in args]:
        raise ShapeException("Vectors must be the same size")
    return [sum(x) for x in zip(*args)]

    # if len(args) == 2:
    #     return vector_add(args[0], args[1])
    # else:
    #     return vector_add(args[0], vector_sum(*args[1:]))


def dot(a, b):
    shape_diff_exception(a,b)
    return sum([a[x]*b[x] for x in range(len(a))])


def vector_multiply(vect, scal):
    print(vect, scal)
    return [x*scal for x in vect]


def vector_mean(*args):
    total = args[0]
    for vect in args[1:]:
        total = vector_add(total, vect)
    return [x/len(args) for x in total]

#
def magnitude(vect):
    return math.sqrt(sum([x**2 for x in vect]))


def matrix_row(matr, row):
    return matr[row]


def matrix_col(matr, col):
    return [row[col] for row in matr]


def matrix_scalar_multiply(matr, scal):
    return [vector_multiply(vect, scal) for vect in matr]


def matrix_vector_multiply(matr, vect):
    return [dot(x, vect) for x in matr]
