import math

from .functions1 import factorial

__all__ = ['sin']


def _taylor(x, n):
    """Sum of the Taylor series terms 0..n for sin(x)."""
    t = (-1)**n * x**(2*n + 1) / factorial(2*n + 1)
    return t + _taylor(x, n - 1) if n else t


def sin(x, n=20):
    """Taylor series for sin(x) (radians), using terms 0..n."""
    if not isinstance(x, complex):
        x = math.remainder(x, 2 * math.pi)  # shift into [-pi, pi]
    return _taylor(x, n)
