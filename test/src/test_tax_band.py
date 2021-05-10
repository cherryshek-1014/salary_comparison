from src.tax_band import TaxCalculator
import pytest

testdata = [
    (38000, 0.05, 4793.07),
    (55000, 0.05, 9902.17)
]

class TestTaxCalculator:
    @pytest.mark.parametrize("salary,pension, expected_tax", testdata)
    def test_returns_expected(self, salary, pension, expected_tax):
        tax_calculator = TaxCalculator(salary, pension)
        assert tax_calculator.get_total_tax() == expected_tax 
