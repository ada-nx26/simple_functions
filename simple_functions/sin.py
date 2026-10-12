from .functions1 import factorial

__all__ = ['sin']


def sin(x, n):
    """Taylor series for sin(x) using terms 0..n (x in radians)."""
    t = ((-1)**n * x**(2*n + 1)) / factorial(2*n + 1)
    return t + sin(x, n - 1) if n else t
