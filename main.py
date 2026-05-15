from datetime import datetime, timedelta
import csv
import os

file_name = "stocking_entries.csv"
fieldnames = ["date", "employee", "aisle", "cases", "start_time", "end_time", "minutes", "cases_per_hour"]
employees = ["Jose", "Alyssa", "Alex", "John"]
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

if not os.path.exists(file_name):
    with open(file_name, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames= fieldnames)
        writer.writeheader()

def create_entry(date, employee, aisle, cases, start, end):
    minutes = calculate_minutes(start, end)
    cases_per_hour = calculate_cases_per_hour(cases, minutes)
    
    entry = {
        "date": date,
        "employee": employee,
        "aisle": aisle,
        "cases": cases,
        "start_time": start.strftime("%H:%M"),
        "end_time": end.strftime("%H:%M"),
        "minutes": round(minutes, 2),
        "cases_per_hour": round(cases_per_hour, 2)
    }

    return entry

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

def calculate_minutes(start, end):
    if end < start:
        end += timedelta(days=1)
    return (end - start).total_seconds() / 60

def calculate_cases_per_hour(cases, minutes):
    if minutes > 0:
        return (cases / minutes) * 60
    else:
        return 0
    
def review_entry(entry):
    # Review entry
    print("\n--- Review Entry ---")
    print(f"Date: {entry['date']}")
    print(f"Employee: {entry['employee']}")
    print(f"Aisle: {entry['aisle']}")
    print(f"Cases: {entry['cases']}")
    print(f"Start Time: {entry['start_time']}")
    print(f"End Time: {entry['end_time']}")
    print(f"Minutes Worked: {entry['minutes']:.0f}")
    print(f"Cases/Hour: {entry['cases_per_hour']:.2f}")
    return

def confirm_save():
    while True:
        confirm = input("\nSave entry? (y/n): ").lower()
        if confirm in ["y", "n"]:
            return confirm == "y"
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def save_entry(entry, entries):
    entries.append(entry)
    with open(file_name, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(entry)
    print("Entry saved.")

def additional_entry():
    while True:
        additional = input("\nAdd another entry? (y/n): ").lower()
        if additional in ["y", "n"]:
            return additional == "y"
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def load_entries():
    entries = []

    if not os.path.exists(file_name):
        return entries

    with open(file_name, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['cases'] = int(row['cases'])
            row['minutes'] = float(row['minutes'])
            row['cases_per_hour'] = float(row['cases_per_hour'])
            entries.append(row)

    return entries

def add_entry(entries):
    print("\n--- New Entry ---")

    employee = get_valid_employees()
    date = get_valid_date()
    aisle = get_valid_aisle()
    cases = get_valid_cases()
    start = get_valid_time("Start time (HH:MM): ")
    end = get_valid_time("End time (HH:MM): ")
    
    entry = create_entry(date, employee, aisle, cases, start, end)
    review_entry(entry)

    if confirm_save():
        save_entry(entry, entries)
        if additional_entry():
            add_entry(entries)
    else:
        print("Entry discarded.")



def rewrite_csv(entries):
    with open(file_name, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for entry in entries:
            writer.writerow(entry)

def delete_last_entry(entries):
    if not entries:
        print("No entries to delete.")
        return

    last_entry = entries[-1]
    print("\n--- Last Entry ---")
    review_entry(last_entry)
    confirm = input("Delete this entry? (y/n): ").lower()
    if confirm == "y":
        entries.pop()
        rewrite_csv(entries)
        print("Last entry deleted.")
    elif confirm == "n":
        print("Entry not deleted.")
    else:
        print("Invalid input. Entry not deleted.")
        return

    print("Last entry deleted.")

def print_summary(entries):
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

def print_employee_averages(entries):
    employee_totals = {}

    for entry in entries:
        employee = entry['employee']

        if employee not in employee_totals:
            employee_totals[employee] = {
                "total_cases_per_hour": 0,
                "entry_count": 0
            }

        employee_totals[employee]["total_cases_per_hour"] += entry['cases_per_hour']
        employee_totals[employee]["entry_count"] += 1

    print("\n--- Employee Averages ---")

    for employee, data in employee_totals.items():
        average = data["total_cases_per_hour"] / data["entry_count"]
        print(f"{employee}: {average:.2f} cases/hour")

def display_menu():
    print("\n--- Stocking Efficiency Tracker ---")
    print("1. Add new entry")
    print("2. View summary")
    print("3. View employee averages")
    print("4. Delete last entry")
    print("5. Exit")

def main():
    # Load existing entries
    entries = load_entries()
    # Main loop
    while True:

        display_menu()

        choice = input("Select an option: ")

        if choice == "1":
            add_entry(entries)
        elif choice == "2":
            print_summary(entries)
        elif choice == "3":
            print_employee_averages(entries)
        elif choice == "4":
            delete_last_entry(entries)
        elif choice == "5":
            break
        else:
            print("Invalid Choice.")

if __name__ == "__main__":
    main()