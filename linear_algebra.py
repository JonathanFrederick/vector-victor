class ShapeException(Exception):
    pass

def shape(thing):
    try:
        return len(thing), len(thing[1])
    except:
        return (len(thing), )


def same_shape(a, b):
    return shape(a) == shape(b)


def vector_add(a, b):
    if same_shape(a,b):
        return [a[x]+b[x] for x in range(len(a))]
    else:
        raise ShapeException("Vectors must be the same size")

def vector_sub(a, b):
    if same_shape(a,b):
        return [a[x]-b[x] for x in range(len(a))]
    else:
        raise ShapeException("Vectors must be the same size")
