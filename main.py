from datetime import datetime, timedelta
import csv
import os

file_name = "stocking_entries.csv"
fieldnames = ["date", "employee", "aisle", "cases", "start_time", "end_time", "minutes", "cases_per_hour"]
employees = ["Jose", "Alyssa", "Alex", "John"]
entries = []
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


def get_valid_employees():
    while True:
        print("\nEmployees:", ", ".join(employees))

        employee = input("Employee name: ").title()
        if employee in employees:
            return employee 
        else:
            print("Invalid employee.")

def get_valid_date():
    while True:
        date = input("Date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format.")

def get_valid_aisle():
    while True:
        print("\nAisles:", ", ".join(aisles))

        aisle = input("Aisle: ").upper()

        if aisle in aisles:
            return aisle
        else:
            print("Invalid aisle.")

def get_valid_cases():
    while True:
        try:
            cases = int(input("Cases stocked: "))
            if cases >= 0:
                return cases
            else:
                print("Cases cannot be negative.")
        except ValueError:
            print("Invalid number of cases.")

def get_valid_time(prompt):
    while True:
        time_str = input(prompt)
        try:
            return datetime.strptime(time_str, "%H:%M")
        except ValueError:
            print("Invalid time format. Please enter in HH:MM format.")

if not os.path.exists(file_name):
    with open(file_name, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames= fieldnames)
        writer.writeheader()

# Main loop
while True:

    print("\n--- New Entry ---")

    # Employee validation
    employee = get_valid_employees()
    date = get_valid_date()
    aisle = get_valid_aisle()
    cases = get_valid_cases()

    # Time input
    start = get_valid_time("Start time (HH:MM): ")
    end = get_valid_time("End time (HH:MM): ")


    # Handle overnight shifts
    if end < start:
        end += timedelta(days=1)

    # Calculate minutes worked
    minutes = (end - start).total_seconds() / 60

    # Calculate cases per hour
    cases_per_hour = (cases / minutes) * 60

    # Create entry
    entry = {
        "date": date,
        "employee": employee,
        "aisle": aisle,
        "cases": cases,
        "start_time": start.strftime("%H:%M"),
        "end_time": end.strftime("%H:%M"),
        "minutes": minutes,
        "cases_per_hour": cases_per_hour
    }

    # Review entry
    print("\n--- Review Entry ---")
    print(f"Date: {date}")
    print(f"Employee: {employee}")
    print(f"Aisle: {aisle}")
    print(f"Cases: {cases}")
    print(f"Start Time: {start.strftime('%H:%M')}")
    print(f"End Time: {end.strftime('%H:%M')}")
    print(f"Minutes Worked: {minutes:.0f}")
    print(f"Cases/Hour: {cases_per_hour:.2f}")

    confirm = input("\nSave entry? (y/n): ").lower()

    # Asking for user confirmation before saving
    if confirm == "y":
        entries.append(entry)
        # If user confirms, save to CSV
        with open(file_name, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(entry)

        print("Entry saved.")
    else:
        print("Entry discarded.")

    # Ask if user wants to add another entry
    cont = input("\nAdd another entry? (y/n): ").lower()

    if cont != "y":
        break

# Summary
print("\n--- Summary ---")

for e in entries:
    print(
        f"{e['date']} | "
        f"{e['employee']} | "
        f"{e['aisle']} | "
        f"{e['cases']} cases | "
        f"{e['minutes']:.0f} min | "
        f"{e['cases_per_hour']:.2f} cases/hour"
    )