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


def vector_sum(*args): #TODO
    total = args[0]
    for vect in args[1:]:
        total = vector_add(total, vect)
        print(total)
    return total


    #return vector_add(args[0], vector_sum([x for x in args[1:] if shape_diff_exception(args[0], x)]))

    #return [vector_add(args[0],  x) for x in args[1:] if shape_diff_exception(args[0], args[x])]

    # if args = None:
    #     return total
    # else:
    #     return vector_add(vector_sum)

    # print(args)
    # print([shape(args[0]) for x in args])
    # print([shape(x) for x in args])
    # print([shape(args[0]) == shape(x) for x in args])
    # if False in [shape(args[0]) == shape(x) for x in args]:
    #     raise ShapeException("Vectors must be the same size")
    # return [sum([y[x] for y in args]) for x in range(len(args))]


    # if isinstance(args, zip):
    #     print("is zip")
    # if len(args) == 2:
    #     shape_diff_exception(args[0], args[1])
    #     return vector_add(args[0], args[1])
    # else:
    #     ret = args
    #     print(ret)
    #     return vector_add(args[0], vector_sum((x for x in args)))


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


def magnitude(vect):
    return math.sqrt(sum([x**2 for x in vect]))
