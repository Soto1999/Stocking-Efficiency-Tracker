from datetime import datetime, timedelta

# Preset employees
employees = ["Jose", "Alyssa", "Alex", "John"]

# Preset aisles
aisles = [
    "1", "2",
    "3", "4",
    "5", "6",
    "7", "8",
    "9A", "9B",
    "10A", "10B",
    "11A", "11B",
    "12", "13",
    "14"
]

entries = []

while True:

    print("\n--- New Entry ---")

    # Employee validation
    while True:
        print("\nEmployees:", ", ".join(employees))

        employee = input("Employee name: ").title()

        if employee in employees:
            break
        else:
            print("Invalid employee.")

    # Aisle validation
    while True:
        print("\nAisles:", ", ".join(aisles))

        aisle = input("Aisle: ").upper()

        if aisle in aisles:
            break
        else:
            print("Invalid aisle.")

    # Cases
    cases = int(input("Cases stocked: "))

    # Time input
    start_time = input("Start time (HH:MM): ")
    end_time = input("End time (HH:MM): ")

    # Convert to datetime objects
    start = datetime.strptime(start_time, "%H:%M")
    end = datetime.strptime(end_time, "%H:%M")

    # Handle overnight shifts
    if end < start:
        end += timedelta(days=1)

    # Calculate minutes worked
    minutes = (end - start).total_seconds() / 60

    # Calculate cases per hour
    cases_per_hour = (cases / minutes) * 60

    # Create entry
    entry = {
        "employee": employee,
        "aisle": aisle,
        "cases": cases,
        "start_time": start_time,
        "end_time": end_time,
        "minutes": minutes,
        "cases_per_hour": cases_per_hour
    }

    # Review entry
    print("\n--- Review Entry ---")
    print(f"Employee: {employee}")
    print(f"Aisle: {aisle}")
    print(f"Cases: {cases}")
    print(f"Start Time: {start_time}")
    print(f"End Time: {end_time}")
    print(f"Minutes Worked: {minutes:.0f}")
    print(f"Cases/Hour: {cases_per_hour:.2f}")

    confirm = input("\nSave entry? (y/n): ").lower()

    if confirm == "y":
        entries.append(entry)
        print("Entry saved.")
    else:
        print("Entry discarded.")

    # Continue loop?
    cont = input("\nAdd another entry? (y/n): ").lower()

    if cont != "y":
        break

# Summary
print("\n--- Summary ---")

for e in entries:
    print(
        f"{e['employee']} | "
        f"{e['aisle']} | "
        f"{e['cases']} cases | "
        f"{e['minutes']:.0f} min | "
        f"{e['cases_per_hour']:.2f} cases/hour"
    )