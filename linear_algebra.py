class ShapeException(Exception):
    pass

def shape(thing):
    try:
        return len(thing), len(thing[1])
    except:
        return (len(thing), )
