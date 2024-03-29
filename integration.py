import cmath


def f(x):
    # Define the function f(x) = cos(x) + 6i * sin(2x)
    functinos = [cmath.cos(x), cmath.sin(x), cmath.tan(x), cmath.exp(x), cmath.log(x), cmath.acos(x), cmath.asin(x)]
    return cmath.cos(x) + 6j * cmath.sin(2*x)

# Resource;
# https://www.khanacademy.org/math/ap-calculus-ab/ab-integration-new/ab-6-3/a/riemann-sums-with-summation-notation

def riemann_approximation(a, b, N):
    # Approximate the integral using N subintervals
    delta_x = (b - a) / N
    integral_sum = 0

    for i in range(N):
        x_i = a + i * delta_x
        integral_sum += f(x_i) * cmath.exp(1j * w * x_i) * delta_x

    return integral_sum

# User-provided values
a = int(input('Enter the Lower limit: '))  # Lower limit
b = int(input('Enter the Upper limit: '))  # Upper limit
N = 1000  # Number of subintervals
w = 1  # Value of the variable w

# Calculate the integral
result = riemann_approximation(a, b, N)

# Print the result
print(f"Approximate integral value: {result:.6f}")
# print(f"Analytical  integral value: ")