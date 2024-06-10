import math
import matplotlib.pyplot as plt
import numpy as np


def h(t):
    """Causal Heaviside function.
    """
    if t >= 0.0:
    return 1.0
return 0.0


"""Vectorize function shorthand
"""
vv = np.vectorize


def r(t):
    """Ramp function.
    """
    return t * h(t)


# y = np.vectorize(r)(x)
# plt.plot(x, y)
# plt.title("R function")
# plt.show()


def delay(t0, f):
    """Delays the given function by t0.
    """

  return lambda t: f(t-t0)


# d = 0.5
# y = np.vectorize(delay(d, h))(x)
# plt.plot(x, y)
# plt.title("Heaviside function, but delayed by {}".format(d))
# plt.show()


# Exp(t) that starts from zero.
def expt(a):
  return lambda t: math.exp(a* t) * h(t)


# y = vv(expt(-1.))(x)
# y2 = vv(expt(1.))(x)
# plt.plot(x, y)
# plt.plot(x, y2)
# plt.title("Here's how exponential function works")
# plt.show()


# Returns a function that is a sum of two functions.
def sumfn(f1, f2):
  return lambda t: f1(t) + f2(t)


# # Tests sumfn by summing up two exponentials, of which one is delayed by 0.5
# def twofn():
  # return lambda t: sumfn(delay(0.5, expt(-1.0)), expt(-1.0))(t)


# y = np.vectorize(twofn())(x)
# plt.plot(x, y)
# plt.show()


# d = 0.5
# y = np.vectorize(delay(d, h))(x)
# plt.plot(x, y)
# plt.title("Heaviside function, but delayed by {}".format(d))
# plt.show()


from functools import reduce

# Returns a function that is a reduction of the supplied fns by fn.
def reducef(fn, *fns):
  return reduce(fn, fns)

# y = np.vectorize(reducef(sumfn,h,delay(0.5, r)))(x)
# plt.plot(x, y)
# plt.show()


def mulf(f1, f2):
  return lambda t: f1(t) * f2(t)

# y = np.vectorize(reducef(mulf, r, r))(x)
# plt.plot(x, y)
# plt.show()
