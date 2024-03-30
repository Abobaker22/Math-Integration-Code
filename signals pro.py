import cmath
from scipy.integrate import quad

def f(x):
    functions = [cmath.cos(x), cmath.sin(x), cmath.tan(x), cmath.exp(x), cmath.acos(x), cmath.asin(x)]
    return cmath.cos(x) + 6j * cmath.sin(2*x)*cmath.exp(1j * w * x)


def integral(a, b, N):
    delta_x = (b - a) / N
    integral_sum = 0

    for i in range(1, N+1):
        x_i = a + (i-1) * delta_x
        integral_sum += f(x_i) *delta_x

    return integral_sum

a = float(input('Enter the Lower limit: '))
b = float(input('Enter the Upper limit: '))
N = 1000
w = 1

result = integral(a, b, N)

print(f"Approximate integral value: {result:.6f}")


############################################CHECKER###############################################
real_integral, imag_integral = quad(lambda x: f(x).real, a, b)[0], quad(lambda x: f(x).imag, a, b)[0]

# Combine the real and imaginary parts to get the complex integral
complex_integral = real_integral + 1j * imag_integral

print(f"Complex integral checker: {complex_integral:.6f}")
