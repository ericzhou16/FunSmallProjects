import math


# Differential Equation
def dydx(x, y):
    return pow(x, 3) * math.exp(-2 * x) - 2 * y


# Runge Kutta
def runge_kutta(x, y, h, xn):
    track = [(x, y)]
    # Looping
    while x < xn:
        # Calculating k values
        k1 = dydx(x, y)
        k2 = dydx(x + h / 2, y + h / 2 * k1)
        k3 = dydx(x + h / 2, y + h / 2 * k2)
        k4 = dydx(x + h, y + h * k3)
        # Rounding
        y = round(y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4), 9)
        x = round(x + h, 2)
        track.append((x, y))
    print(f"Approximation: ({xn}, {y})")
    return track


# Running functions and showing results
track1 = runge_kutta(0, 1, 0.1, 1)
track2 = runge_kutta(0, 1, 0.05, 1)
print(track1)
print([track2[i] for i in range(0, len(track2), 2)])  # printing every other
