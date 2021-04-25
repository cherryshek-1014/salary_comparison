from enum import Enum

TAX_FREE = 12570
GLASGOW_BANDS = [12570, 14667, 25296, 43662, 150000]
GLASGOW_BAND_TAX_RATES = [0.19, 0.20, 0.21, 0.41, 0.46]
LONDON_BANDS = [12570, 14667, 25296, 43662, 150000]


class TAX_BAND(Enum):
    STARTER = 0
    BASIC = 1
    INTERMEDIATE = 2
    HIGHER = 3


class TaxCalculator:
    def __init__(self, salary: int):
        self.salary = salary

    def get_total_tax(self):
        total = 0
        if self.salary <= TAX_FREE:
            return 0

        for index, value in enumerate(GLASGOW_BANDS):
            if index >= len(GLASGOW_BANDS) - 1:
                break
            if self.salary > GLASGOW_BANDS[index + 1]:
                taxable_amount_in_band = (GLASGOW_BANDS[index + 1] - value)
            else:
                taxable_amount_in_band = (self.salary - value)

            total += taxable_amount_in_band * GLASGOW_BAND_TAX_RATES[index]

        return total
