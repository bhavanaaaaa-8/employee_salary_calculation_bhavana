# Employee Salary Calculator

## Description
The Employee Salary Calculator is a Python program that calculates an employee's gross salary, total deductions, and net salary using configurable salary rules. It generates a formatted salary slip displaying the employee's salary details.

## Features
- Accepts employee name and basic salary.
- Calculates House Rent Allowance (HRA) and Dearness Allowance (DA).
- Calculates gross salary using separate functions.
- Calculates Provident Fund (PF) and tax deductions separately.
- Calculates total deductions and net salary.
- Validates numeric inputs and rejects negative salaries.
- Handles invalid inputs with clear error messages.
- Displays a neatly formatted salary slip.
- Allows salary rules to be configured easily.

## Salary Rules
The default salary percentages are:

- HRA: 20% of basic salary
- DA: 10% of basic salary
- PF: 5% of basic salary
- Tax: 5% of gross salary

These are sample values and can be modified in the program.

## Formulas
- **HRA** = Basic Salary × HRA Rate / 100
- **DA** = Basic Salary × DA Rate / 100
- **Gross Salary** = Basic Salary + HRA + DA
- **Total Deductions** = PF + Tax
- **Net Salary** = Gross Salary − Total Deductions

## Technologies Used
- Python 3
- Functions
- Conditional statements
- `try-except` exception handling
- Numeric input validation
- String formatting

## How to Run
1. Install Python 3.
2. Save the program as `employee_salary_calculator.py`.
3. Open a terminal in the folder containing the file.
4. Run the command:

   ```bash
   python employee_salary_calculator.py
   ```

5. Enter the employee's name and basic salary when prompted.

## Example
For a basic salary of ₹30,000:

| Component | Amount |
|---|---:|
| Basic Salary | ₹30,000.00 |
| HRA | ₹6,000.00 |
| DA | ₹3,000.00 |
| Gross Salary | ₹39,000.00 |
| PF Deduction | ₹1,500.00 |
| Tax Deduction | ₹1,950.00 |
| Total Deductions | ₹3,450.00 |
| **Net Salary** | **₹35,550.00** |

## Input Validation
- Rejects non-numeric salary inputs.
- Rejects negative salaries.
- Allows decimal salary values.
- Requests the salary again until valid input is provided.
- Rejects an empty employee name.

## Future Improvements
- Support multiple employees.
- Add employee ID and department.
- Save salary slips to a text file or PDF.
- Add configurable allowances and deductions.
- Support monthly and annual salary reports.

## Disclaimer
This project is intended for educational purposes. The salary percentages are illustrative and do not represent official payroll or tax rules.
