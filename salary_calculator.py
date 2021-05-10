from TaxBand import TaxCalculator


class SalaryCalculator:
    def __init__(self, salary, location, pension_rate):
        self.salary = salary
        self.location = location
        self.pension_rate = pension_rate
        self.salary_after_pension = self.salary - \
            (self.salary * self.pension_rate)

    def glasgow_tax(self) -> int:
        tax_calc = TaxCalculator(self.salary_after_pension)

        return tax_calc.get_total_tax()

    def london_tax(self):
        if self.salary_after_pension <= 12570:
            return 0
        elif self.salary_after_pension <= 50270:
            return (self.salary_after_pension - 12570) * 0.2
        elif self.salary_after_pension <= 150000:
            first_band = (50270 - 12570) * 0.2
            second_band = (self.salary_after_pension - 50270) * 0.4
            return first_band + second_band

    def tax_deduction(self):
        if self.location == "G":
            return self.glasgow_tax()
        elif self.location == "L":
            return self.london_tax()
        else:
            return "Please specify a valid Location: 'G' or 'L'"

    def nic_deduction_weekly(self):
        weekly_gross = self.salary_after_pension / 52
        if weekly_gross < 184:
            return 0
        elif weekly_gross <= 967:
            return (weekly_gross - 184) * 0.12
        else:
            allowence = 184
            pct_12 = 967 - allowence
            pct_2 = weekly_gross - allowence - pct_12
            return (pct_12 * 0.12) + (pct_2 * 0.02)

    def student_loan_deduction(self):
        return (self.salary_after_pension - 25000) * 0.09

    def take_home(self):
        tax = self.tax_deduction()
        nic = self.nic_deduction_weekly() * 52
        student_loan = self.student_loan_deduction()
        return round(self.salary_after_pension - (tax + nic + student_loan), 2)


Salary_Calculator = SalaryCalculator(55000, 'G', 0.05)
print('Tax Deduction: £'+str(Salary_Calculator.tax_deduction()))
print('NI Deduction: £'+str(Salary_Calculator.nic_deduction_weekly()*52))
print('Student Loan Deduction: £'+str(Salary_Calculator.student_loan_deduction()))
print('Take Home: £'+str(Salary_Calculator.take_home()))
