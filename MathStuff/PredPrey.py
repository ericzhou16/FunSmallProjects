import matplotlib.pyplot as plt


def dxdt(x, y):
    return 2 * x - x * y


def dydt(x, y):
    return x * y - 3 * y


# y(0) = 2, x(0) = 80
def double_euler(t, x, y, h, tn):
    xs = []
    ys = []
    ts = []
    while t < tn:
        # yprime = dydt(x, y)
        # xprime = dxdt(x, y)
        # y = y + h * yprime
        # x = x + h * xprime
        x = x + h * dxdt(x, y)
        y = y + h * dydt(x, y)
        t += h
        # print(f"({x}, {y})")
        xs.append(x)
        ys.append(y)
        ts.append(t)
    print("Approximation: x: " + str(x) + ", y: " + str(y))
    return xs, ys, ts


xs, ys, ts = double_euler(0, 80, 2, 0.001, 100)
plt.plot(ts, xs)
plt.plot(ts, ys)
plt.show()
