import pytest
import numpy as np

from simple_functions import my_sum, sin


class TestSimpleFunctions:
    """Tests for the functions in the simple_functions package."""

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4),
    ])
    def test_my_sum(self, iterable, expected):
        """my_sum adds up the items of lists and tuples."""
        assert my_sum(iterable) == expected

    @pytest.mark.parametrize('x', [
        0.0, 0.5, 1.0, -1.0, np.pi / 2, 10.0, 100.0, -50.0,
    ])
    def test_sin(self, x):
        """sin's Taylor series matches numpy's sin, including large x."""
        assert sin(x) == pytest.approx(np.sin(x), abs=1e-12)
