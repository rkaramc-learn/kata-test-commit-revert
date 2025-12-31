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
