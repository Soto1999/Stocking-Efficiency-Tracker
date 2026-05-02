
product = input("Product name: ")
cases = int(input("Cases stocked: "))
minutes = float(input("Minutes worked: "))

cases_per_hour = (cases / minutes) * 60

print(f"\n{product}")
print(f"Cases per hour: {cases_per_hour:.2f}")
