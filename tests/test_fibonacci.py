from pytest_benchmark.fixture import BenchmarkFixture
from kata_test_commit_revert.formulae import fibonacci


class TestFibonacci:
    def test_fibonacci(self):
        assert True

    def test_fibonacci_0(self):
        assert fibonacci(0) == 0

    def test_fibonacci_1(self):
        assert fibonacci(1) == 1

    def test_fibonacci_2(self):
        assert fibonacci(2) == 1

    def test_fibonacci_3(self):
        assert fibonacci(3) == 2

    def test_fibonacci_4(self):
        assert fibonacci(4) == 3

    def test_fibonacci_5(self):
        assert fibonacci(5) == 5

    def test_fibonacci_6(self):
        assert fibonacci(6) == 8

    def test_fibonacci_7(self):
        assert fibonacci(7) == 13

    def test_fibonacci_8(self):
        assert fibonacci(8) == 21

    def test_fibonacci_9(self):
        assert fibonacci(9) == 34

    def test_fibonacci_10(self):
        assert fibonacci(10) == 55

    def test_fibonacci_11(self):
        assert fibonacci(11) == 89

    def test_fibonacci_12(self):
        assert fibonacci(12) == 144

    def test_fibonacci_13(self):
        assert fibonacci(13) == 233

    def test_fibonacci_14(self):
        assert fibonacci(14) == 377

    def test_fibonacci_15(self):
        assert fibonacci(15) == 610

    def test_fibonacci_16(self):
        assert fibonacci(16) == 987

    def test_fibonacci_17(self):
        assert fibonacci(17) == 1597

    def test_fibonacci_18(self):
        assert fibonacci(18) == 2584

    def test_fibonacci_19(self):
        assert fibonacci(19) == 4181

    def test_fibonacci_20(self, benchmark: BenchmarkFixture):
        result = benchmark(fibonacci, 20)  # pyright: ignore[reportUnknownVariableType]
        assert result == 6765

    def test_fibonacci_30(self, benchmark: BenchmarkFixture):
        result = benchmark(fibonacci, 30)  # pyright: ignore[reportUnknownVariableType]
        assert result == 832040
