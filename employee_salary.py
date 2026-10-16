
# Configurable Salary Rules
HRA_RATE = 20
DA_RATE = 10
PF_RATE = 5
TAX_RATE = 5


def get_valid_salary():
    while True:
        try:
            salary = float(input("Enter basic salary: ₹"))

            if salary < 0:
                print("Salary cannot be negative. Try again.")
            else:
                return salary

        except ValueError:
            print("Invalid input! Enter a numeric salary.")


def calculate_hra(basic_salary):
    return basic_salary * HRA_RATE / 100


def calculate_da(basic_salary):
    return basic_salary * DA_RATE / 100


def calculate_gross_salary(basic_salary, hra, da):
    return basic_salary + hra + da


def calculate_pf(basic_salary):
    return basic_salary * PF_RATE / 100


def calculate_tax(gross_salary):
    return gross_salary * TAX_RATE / 100


def calculate_total_deductions(pf, tax):
    return pf + tax


def calculate_net_salary(gross_salary, deductions):
    return gross_salary - deductions


def display_salary_slip(name, basic_salary):
    hra = calculate_hra(basic_salary)
    da = calculate_da(basic_salary)

    gross = calculate_gross_salary(basic_salary, hra, da)

    pf = calculate_pf(basic_salary)
    tax = calculate_tax(gross)

    deductions = calculate_total_deductions(pf, tax)
    net = calculate_net_salary(gross, deductions)

    print("\n========== SALARY SLIP ==========")
    print(f"Employee Name    : {name}")
    print(f"Basic Salary     : ₹{basic_salary:,.2f}")
    print(f"HRA              : ₹{hra:,.2f}")
    print(f"DA               : ₹{da:,.2f}")
    print("---------------------------------")
    print(f"Gross Salary     : ₹{gross:,.2f}")
    print(f"PF Deduction     : ₹{pf:,.2f}")
    print(f"Tax Deduction    : ₹{tax:,.2f}")
    print(f"Total Deductions : ₹{deductions:,.2f}")
    print("---------------------------------")
    print(f"Net Salary       : ₹{net:,.2f}")
    print("=================================")


def main():
    name = input("Enter employee name: ").strip()

    if not name:
        print("Error: Employee name cannot be empty.")
        return

    basic_salary = get_valid_salary()
    display_salary_slip(name, basic_salary)


if __name__ == "__main__":
    main()
