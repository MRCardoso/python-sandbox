import sys

params = sys.argv[1:]
value = 12
try:
    value = int(params[0])
except:
    pass

def fromRecursion(value, result = 0):
    """
    Sum the accumulator (result), with next decrement (value - 1)
    each handshake decrease 1
    ex:(3) 2 + 1
    ex:(4) 3 + 2 + 1
    ex:(12) 11 + 10 + 9 + 8 + 7 + 6 + 5+ 4 + 3 + 2 + 1
    etc...
    """
    nextValue = value - 1
    result += nextValue
    if nextValue > 1:
        result = fromRecursion(nextValue, result)
    return result

def fromMath(value):
    """
    each person greets 12 times
    multiplying the total of peoples x the total of each person handshake
    (value - 1), you have all possibilities of handshake
    Now just divide the result by the quantity of handshake by person (2)
    """
    return (value * (value -1)) / 2

print(
    "Result from Recursion: %d, result from Math: %d" %
    (fromRecursion(value), fromMath(value))
)