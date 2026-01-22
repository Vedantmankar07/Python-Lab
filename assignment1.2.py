vendor_name = input("Enter Vendor Name: ")
assoc_year = input("Enter Year of Association: ")
phone = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

total_purchase = 0

for i in range(1, 13):
    monthly_val = float(input(f"Enter purchase for month {i}: "))
    total_purchase += monthly_val

print("\n--- ANNUAL PURCHASE REPORT ---")
print("Vendor:", vendor_name)
print("Year:", assoc_year)
print("Contact:", phone)
print("Email:", email)
print("------------------------------")
print("Total Annual Billing: ", total_purchase)
print("Average Monthly Spend:", total_purchase / 12)
print("------------------------------")