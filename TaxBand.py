from enum import Enum


class TAX_BAND(Enum):
    STARTER = 0
    BASIC = 1
    INTERMEDIATE = 2
    HIGHER = 3


class TaxCalculator:
    def __init__(self, salary: int):
        self.salary = salary

    def get_tax_for_band(self, band: TAX_BAND) -> int:
        if band == TAX_BAND.STARTER:
            if self.salary < 14667:
                return (self.salary - 12570) * 0.19

            return (14667 - 12570) * 0.19

        if band == TAX_BAND.BASIC:
            return (self.salary - 14667) * 0.2
        if band == TAX_BAND.INTERMEDIATE:
            return (self.salary - 25296) * 0.21
        if band == TAX_BAND.HIGHER:
            return (self.salary - 43662) * 0.41

        return 0