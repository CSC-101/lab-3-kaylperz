more = [x + 1 for x in [1,2,3,4]]     # List, in order, the values that x takes at each step. x=1, x=2, x=3, x=4
print()                               # What is the value of more at this point? [2,3,4,5]

def square(n:int) -> int:
    return n * n                           # Record, in order of the calls, each value of n and
                                           # the corresponding return value. n=1 return 1, n=2 return 4, n=3 return 9, n=4 return 16


squares = [square(x) for x in [1,2,3,4]]   # What is the value of squares and how does this relate to the
print()                                    # values recorded above? squares = [1,4,9,16] this is the corresponding return values

def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value. n=1 return false, n=2 return false, n=3 return true, n=4 return true


answer = [x for x in range(5) if check(x)]   # What is the value of answer? [3,4]
print()

def inc(m:int) -> int:
    return m + 1                             # Record, in order of the calls, each value of m and
                                             # the corresponding return value. m = 3 return 4, m = 4 return 5


def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value. n = 0 return false, n = 1 return false, n = 2 return false, n = 3 return true, n = 4 return true


answer = [inc(x) for x in range(5) if check(x)]   # What is the value of answer? [3,4]
print()