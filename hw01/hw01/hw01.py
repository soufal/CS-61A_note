from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    # if b < 0:
    #     f = add(a, -b)
    # else:
    #     f = add(a, b)
    #office answer
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

def a_plus_abs_b_syntax_check():
    """Check that you didn't change the return statement of a_plus_abs_b.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    # You don't need to edit this function. It's just here to check your work.


def two_of_three(i, j, k):
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    # min_v = min(i, j, k)
    # max_v = max(i, j, k)
    # medim_v = sub(sub(add(add(i, j), k), min_v), max_v)
    # result = add(min_v*min_v, medim_v*medim_v)
    # return min(i*i+j*j, i*i+k*k, j*j+k*k)
    # other solution
    return i**2+j**2+k**2 - max(i,j,k)**2

def two_of_three_syntax_check():
    """Check that your two_of_three code consists of nothing but a return statement.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    # You don't need to edit this function. It's just here to check your work.


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    max_factor = 1
    for i in range(1, n):
        if n % i == 0:
            max_factor=max(max_factor, i)
    return max_factor



def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5~
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    #选择一个正整数 n 作为开始。 如果 n 是偶数，则将其除以 2。 如果n是奇数，则乘以3并加1。 继续这个过程直到n为1。
    hailstone_len = 1
    print(n)

    while n != 1:
        if(n % 2 == 0):
            n = n // 2
            print(n)
            hailstone_len += 1
        else:
            n = n * 3 + 1
            print(n)
            hailstone_len += 1


    return hailstone_len
