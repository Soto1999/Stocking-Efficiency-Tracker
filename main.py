
entries =[]

while True:
    print("\nNew Entry")
    employee = input("Employee name: ")
    aisle = input("Aisle: ")
    cases = int(input("Cases stocked: "))
    minutes = float(input("Minutes worked: "))

    cases_per_hour = (cases / minutes) * 60

    entry = {
        "employee": employee,
        "aisle": aisle,
        "cases_per_hour": cases_per_hour
    }

    entries.append(entry)

    print(f"\nRecorded: {employee} - {cases_per_hour:.2f} cases/hour")
    
    cont = input("Add another entry? (y/n): ").lower()
    if cont != 'y':
        break

#Summary
print("\nSummary")
for e in entries:
    print(f"{e['employee']} - {e['aisle']} - {e['cases_per_hour']:.2f} cases/hour")

print("\n Employee Averages")

employee_totals = {}

for e in entries:
    employee = e['employee']
    if employee not in employee_totals:
        employee_totals[employee] = {
            "total_cases_per_hour": 0,
            "entry_count": 0
        }

    employee_totals[employee]["total_cases_per_hour"] += e['cases_per_hour']
    employee_totals[employee]["entry_count"] += 1

for employee, data in employee_totals.items():
    average = data["total_cases_per_hour"] / data["entry_count"] if data["entry_count"] > 0 else 0
    print(f"{employee} - {average:.2f} cases/hour")