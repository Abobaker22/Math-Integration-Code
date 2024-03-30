import cmath
import math
from scipy.integrate import quad


def f(x):
    return cmath.cos(x) + 6j * cmath.sin(2*x)*cmath.exp(1j * w * x)
    # return cmath.sin(2*x)


def riemann_approximation(a, b, N):
    delta_x = (b - a) / N
    integral_sum = 0

    for i in range(1, N+1):
        x_i = a + (i - 1) * delta_x
        x_i_plus_one = a + (i) * delta_x
        x_midpoint = (x_i + x_i_plus_one) / 2
        integral_sum += f(x_midpoint) *delta_x

    return integral_sum


def integrate_using_build_in():
    # Compute the real part of the integral
    I_real, _ = quad(lambda x: f(x).real, a, b)

    # Compute the imaginary part of the integral
    I_imag, _ = quad(lambda x: f(x).imag, a, b)

    # Combine the real and imaginary parts to form the complex integral
    I_analytical = I_real + 1j * I_imag
    return I_analytical


def cartesian_to_polar(cartesian):
    real_part = cartesian.real
    imag_part = cartesian.imag

    # Calculate magnitude (r)
    magnitude = math.sqrt(real_part**2 + imag_part**2)

    # Calculate phase angle (θ)
    if real_part == 0:
        if imag_part > 0:
            phase_angle = math.pi / 2
        elif imag_part < 0:
            phase_angle = -math.pi / 2
        else:
            phase_angle = 0
    else:
        phase_angle = math.atan(imag_part / real_part)
        if real_part < 0:
            phase_angle += math.pi

    return magnitude, phase_angle


a = int(input('Enter the Lower limit: '))
b = int(input('Enter the Upper limit: '))
N = 1000
w = 1

result = riemann_approximation(a, b, N)
polar_result = cartesian_to_polar(result)
I_analytical = integrate_using_build_in()
absolute_difference = abs(I_analytical - result)

# Compare the results
print(f"Approximate integral value: {result:.6f}")
print(f"Analytical integral value: {I_analytical:.6f}")
# Calculate the absolute difference between analytical and numerical results
print(f"Absolute difference: {absolute_difference:.6f}")
print(
    f"Approximate integral value (Polar): {polar_result[0]:.6f} * e^({polar_result[1]:.6f}j)"
)

# Resource;
# https://www.khanacademy.org/math/ap-calculus-ab/ab-integration-new/ab-6-3/a/riemann-sums-with-summation-notation
