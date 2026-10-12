import pytest
import numpy as np

from simple_functions import my_sum


class TestSimpleFunctions:
    """Tests for the functions in functions1.py."""

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4),
    ])
    def test_my_sum(self, iterable, expected):
        """my_sum adds up the items of lists and tuples."""
        assert my_sum(iterable) == expected

    def test_sin(self, x):
        """sin's Taylor series matches numpy's sin."""
        assert sin(x, 20) == pytest.approx(np.sin(x), abs=1e-12)