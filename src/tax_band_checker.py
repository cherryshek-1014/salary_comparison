from src.tax_band import GLASGOW_BANDS, TAX_BAND

class TaxBandChecker:
    def __init__(self, amount, band=GLASGOW_BANDS):
        self.amount = amount
        self.band = band

    def _is_amount_in(self, tier: TAX_BAND) -> bool:
        return self.amount > self.band[tier.value]

    def is_starter_rate(self) -> bool:
        return self._is_amount_in(TAX_BAND.STARTER)

    def is_basic_rate(self) -> bool:
        return self._is_amount_in(TAX_BAND.BASIC)

    def is_int_rate(self) -> bool:
        return self._is_amount_in(TAX_BAND.INTERMEDIATE)

    def is_higher_rate(self) -> bool:
        return self._is_amount_in(TAX_BAND.HIGHER)
