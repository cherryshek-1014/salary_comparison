from src.salary_calculator import SalaryCalculator
import pandas as pd

output = pd.DataFrame(
    columns=['annual_salary', 'glasgow_takehome', 'london_takehome'])
Pension_Contribution = 0.05
salary_range = list(range(30000, 105000, 5000))

for ind, value in enumerate(salary_range):
    glasgow_takehome = SalaryCalculator(
        value, "G", Pension_Contribution
    ).take_home()

    london_takehome = SalaryCalculator(
        value, "L", Pension_Contribution
    ).take_home()

    output_row = [int(value), glasgow_takehome, london_takehome]
    output.loc[ind] = output_row

output.to_csv("Glasgow_Londond_Takehome_Comparison.csv", index=False)
