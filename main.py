import cmath
import numpy as np

class BigInt:
    def __init__(self, value=0):
        if isinstance(value, int):
            self.value = str(value)
        elif isinstance(value, str):
            self.value = value
        else:
            raise TypeError("BigInt supports only int or str initialization")

    def __str__(self):
        return self.value

    def __int__(self):
        return int(self.value)

    # Comparison operators
    def __lt__(self, other):
        return self.value < str(other)

    def __le__(self, other):
        return self.value <= str(other)

    def __gt__(self, other):
        return self.value > str(other)

    def __ge__(self, other):
        return self.value >= str(other)

    def __eq__(self, other):
        return self.value == str(other)

    # Arithmetic operators
    def __add__(self, other):
        return BigInt(int(self) + int(other))

    def __sub__(self, other):
        return BigInt(int(self) - int(other))

    def __mul__(self, other):
        return BigInt(int(self) * int(other))

    def __floordiv__(self, other):
        return BigInt(int(self) // int(other))

    def __mod__(self, other):
        return BigInt(int(self) % int(other))

    def __pow__(self, power, modulo=None):
        return BigInt(int(self) ** int(power))

    # Conversion methods
    @staticmethod
    def from_string(string):
        return BigInt(string)

    @staticmethod
    def from_int(integer):
        return BigInt(integer)

    def to_string(self):
        return str(self)

    def to_int(self):
        return int(self)



def karatsuba_multiply(x, y):
    x = str(x)
    y = str(y)

    if len(x) == 0 or len(y) == 0:
        return 0
    if len(x) == 1 or len(y) == 1:
        return int(x) * int(y)

    max_len = max(len(x), len(y))
    n = (max_len + 1) // 2

    a, b = x[:-n], x[-n:]
    c, d = y[:-n], y[-n:]

    # Handle case where a or b is empty
    if not a:
        a = '0'
    if not b:
        b = '0'
    if not c:
        c = '0'
    if not d:
        d = '0'

    ac = karatsuba_multiply(a, c)
    bd = karatsuba_multiply(b, d)
    ad_plus_bc = karatsuba_multiply(str(int(a) + int(b)), str(int(c) + int(d))) - ac - bd

    result = ac * 10**(2*n) + (ad_plus_bc * 10**n) + bd

    return result


def fft_multiply(x, y):
    x_str = str(x)
    y_str = str(y)

    n = len(x_str) + len(y_str) - 1
    fft_size = 1
    while fft_size < n:
        fft_size *= 2

    # Convert numbers to polynomials
    x_poly = [int(digit) for digit in reversed(x_str)]
    y_poly = [int(digit) for digit in reversed(y_str)]

    # Apply FFT
    x_fft = np.fft.fft(x_poly, fft_size)
    y_fft = np.fft.fft(y_poly, fft_size)

    # Perform multiplication in frequency domain
    result_fft = x_fft * y_fft

    # Apply inverse FFT to obtain result in time domain
    result_time_domain = np.fft.ifft(result_fft).real  # Take the real part since we're dealing with integers

    # Convert result from polynomial representation to integer
    result = 0
    for i in range(n):
        result += round(result_time_domain[i]) * (10 ** i)

    return result





a = BigInt(9876543234121124123412341234123412341234341234123411098765432109876543210)
b = BigInt("1234123412341234123412341234123412341234123412341234123412341234123412341234")

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

bigint1 = BigInt(num1)
bigint2 = BigInt(num2)

result_fft = fft_multiply(bigint1, bigint2)
print("Result of FFT multiplication:", result_fft)

result_karatsuba = karatsuba_multiply(bigint1, bigint2)
print("Result of Karatsuba multiplication:", result_karatsuba)

