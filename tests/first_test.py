from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    # Позитивный тест на умножение
    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    # Позитивный тест на деление
    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 4, 2) == 2

    # Позитивный тест на сложение
    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 5, 2) == 7

    # Позитивный тест на вычитание
    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 8, 2) == 6




