"""Dummy test cases."""

from src.keep_it import add


def test_add(benchmark):
    """Test that ensure the add function does work well."""
    assert benchmark(add, 1, 2) == 3
