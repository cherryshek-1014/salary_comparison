from src.salary_calculator import SalaryCalculator

Salary_Calculator = SalaryCalculator(55000, 'G', 0.05)
print('Tax Deduction: £'+str(Salary_Calculator.tax_deduction()))
print('NI Deduction: £'+str(Salary_Calculator.nic_deduction_weekly()*52))
print('Student Loan Deduction: £'+str(Salary_Calculator.student_loan_deduction()))
print('Take Home: £'+str(Salary_Calculator.take_home()))
