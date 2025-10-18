coeff = [4, 6, 8]
x = 2

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
        power = 1
        for j in range(i):
            power *= x
        res += coeff[i] * power
    return res

def fast_pow(x, n):
    """
    This is a function calculating number to the given power using recursion.
    :param x: number
    :param n: exponent
    :return: x to the power of n
    """
    if n == 0:
        return 1
    half = fast_pow(x, n // 2)
    if n % 2  == 0:
        return half * half
    else:
        return half * half * x

# 2. O(n log n)
def wiel_wart_rek(x, coeff):
    """
    *Same* but using recursion to calculate the values of x to the power of n.
    :param x:
    :param coeff:
    :return:
    """
    res = 0
    for i in range(len(coeff)):
        res += coeff[i] * fast_pow(x, i)
    return res

# 3. Horner
'''Aby obliczyć wartość wielomianu w postaci Hornera, 
należy wykonać n podstawień danej wartości w zamian za x oraz n - 1 mnożeń, co daje 2n - 1 operacji, 
gdzie stopień wielomianu jest większy lub równy n.'''

def wiel_wart_horner(x, coeff):
    """
    *Same* but using Horner's polynomial form.
    :param x:
    :param coeff:
    :return:
    """
    res = 0
    for a in reversed(coeff):
        res = res * x + a
    return res

print("O(n^2):", wiel_wart(x, coeff))
print("O(n log n):", wiel_wart_rek(x, coeff))
print("O(n) Horner:", wiel_wart_horner(x, coeff))
