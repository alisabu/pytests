import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_multiply_calculate_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 10, 5) == 2

    def test_division_calculate_failed(self):
        assert self.calc.division(self, 8, 4) == 3

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 20, 5) == 15

    def test_subtraction_calculate_failed(self):
        assert self.calc.subtraction(self, 8, 4) == 3

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 20, 5) == 25

    def test_adding_calculate_failed(self):
        assert self.calc.adding(self, 4, 4) == 9
