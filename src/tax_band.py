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
        self.salary = salary

    def get_total_tax(self):
        remainder = self.salary
        total = 0
        
        if self.salary <= TAX_FREE:
            return 0

        for index, band in enumerate(GLASGOW_BANDS):
            # skip first tax free
            if index == 0:
                remainder -= band
                continue
            
            if remainder <= 0:
                break

            if remainder - (band - GLASGOW_BANDS[index - 1]):
               taxable_amount_in_band = band - GLASGOW_BANDS[index - 1]
               remainder -= taxable_amount_in_band
            else:
                taxable_amount_in_band = remainder
                remainder = 0
                
            print(taxable_amount_in_band,
                  GLASGOW_BAND_TAX_RATES[index], taxable_amount_in_band * GLASGOW_BAND_TAX_RATES[index])
            total += taxable_amount_in_band * GLASGOW_BAND_TAX_RATES[index]

        print(total)
        return total
