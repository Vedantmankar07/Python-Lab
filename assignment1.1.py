name = input("Enter Name: ")
emp_id = input("Enter Employee ID: ")
dept = input("Enter Department: ")
basic_salary = float(input("Enter Basic Salary: "))

da = 0.92 * basic_salary
hra = 0.58 * basic_salary
ta = 0.30 * basic_salary
lic = 500

gross_salary = basic_salary + da + hra + ta
net_salary = gross_salary - lic

print("\n--- Employee Pay Slip ---")
print("Name:", name)
print("ID:", emp_id)
print("Department:", dept)
print("Basic Salary:", basic_salary)
print("DA:", da)
print("HRA:", hra)
print("TA:", ta)
print("LIC Deduction:", lic)
print("-------------------------")
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)