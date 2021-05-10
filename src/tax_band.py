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
    def __init__(self, salary: int, pension_rate: float):
        self.salary = salary * (1 - pension_rate)

    def _get_taxable_amount_in_band(self, band, next_band):
        if self.salary >= next_band:
            return next_band - band
        
        return self.salary - band

    def get_total_tax(self):
        total = 0

        for index, band in enumerate(GLASGOW_BANDS):
            if self.salary <= band:
                return total

            next_band =  GLASGOW_BANDS[index + 1]
            taxable_amount_in_band = self._get_taxable_amount_in_band(band, next_band)

            
            total += taxable_amount_in_band * GLASGOW_BAND_TAX_RATES[index]

        print(f"total: {total}")
        return total
