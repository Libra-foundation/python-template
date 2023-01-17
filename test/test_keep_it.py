from src.keep_it import add


def test_add(benchmark):
    assert benchmark(add, 1, 2) == 3
