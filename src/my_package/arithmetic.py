"""
This is arithmetic package.
"""

def fibonacci_iterative(n):
    """
    Fibbonachi. Returns the n-th element of the Fibbonachi sequence
    starting from 1.
    :type n: int
    :param n: n - the number of element in the sequence
    :rtype: int
    
    """
    if isinstance(n-1, int) and n > 0:
        a, b = 1, 1
        for i in xrange(n-1):  # @UnusedVariable
            a, b = b, a + b
        return a
    else:
        raise Exception("n is natural")

def fibonacci_recursive(n):
    """
    Fibbonachi recursive
    :type n: int
    :param n: n - the number of element in the sequence
    
    """
    if isinstance(n, int) and n > 0:
        if n in [1, 2]:
            return 1
        else: 
            return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    else:
        raise Exception("n should be natural")
       
if __name__ == "__main__":
    for i in xrange(1,10):
        print fibonacci_recursive(i)
#     print fibonacci_recursive(4)
#     for i in xrange(10):
#         print fibonacci_recursive(i)
     