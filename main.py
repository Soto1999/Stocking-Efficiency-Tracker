
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