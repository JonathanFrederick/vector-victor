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


def vector_add(a, b):
    shape_diff_exception(a,b)
    return [a[x]+b[x] for x in range(len(a))]


def vector_sub(a, b):
    shape_diff_exception(a,b)
    return [a[x]-b[x] for x in range(len(a))]


# def vector_sum(total, *args = None): #TODO
#     if args = None:
#         return total
#     else:
#         return vector_add(vector_sum)

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
    #     return vector_add(args[0], vector_sum(zip(args)))


def dot(a, b):
    shape_diff_exception(a,b)
    return sum([a[x]*b[x] for x in range(len(a))])
