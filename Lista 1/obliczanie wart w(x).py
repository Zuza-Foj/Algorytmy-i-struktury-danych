coeff = [4, 6, 8]
# 1. O(n^2)
def wiel_wart(x, coeff):
    """
    This is a function calculating the value of a polynomial for given value of x and list of coefficients.
    :param x: int variable
    :param coeff: list of numbers
    :return: int result p(a) where 'a' is a given x
    """
    res = coeff[0]
    for i in range(1, len(coeff)):
        res += coeff[i] * x ** i
    return res

print(wiel_wart(2, coeff))

# 2. O(n logn)
def wiel_wart_rek(x, coeff):
    """
    *Same* but using recursion to calculate the values of x to the power of n.
    :param x:
    :param coeff:
    :return:
    """
    res = coeff[0]
    for i in range(1,len(coeff)):
        if i // 2 == 0:
            half = x ** (1 // 2)
            res += coeff[i] * half * half
        else:
            res += coeff[i] * half * half * x
    return res

print(wiel_wart(2, coeff))

# 3. Horner
'''Aby obliczyć wartość wielomianu w postaci Hornera, 
należy wykonać n podstawień danej wartości w zamian za x oraz n - 1 mnożeń, co daje 2n - 1 operacji, 
gdzie stopień wielomianu jest większy lub równy n.'''