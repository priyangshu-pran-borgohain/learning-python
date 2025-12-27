DATA_FILE = "study_log.txt"

def add_entry():
    date = input("Date (DD-MM-YYYY): ")
    subject = input("Subject: ")
    hours = float(input("Study hours: "))
    focus = int(input("Focus level (1-5): "))

    with open(DATA_FILE, "a") as f:
        f.write(f"{date},{subject},{hours},{focus}\n")

    print("Entry saved.\n")

def analyze():
    try:
        with open(DATA_FILE, "r") as f:
            data = f.readlines()

        subject_hours = {}
        total_focus = 0
        entries = 0

        for line in data:
            _, subject, hours, focus = line.strip().split(",")
            hours = float(hours)
            focus = int(focus)

            subject_hours[subject] = subject_hours.get(subject, 0) + hours
            total_focus += focus
            entries += 1

        best_subject = max(subject_hours, key=subject_hours.get)
        avg_focus = total_focus / entries

        print("\n--- Productivity Report ---")
        print("Most studied subject:", best_subject)
        print("Average focus level:", round(avg_focus, 2))
        print("Total study entries:", entries)
        print()

    except FileNotFoundError:
        print("No data found.\n")

while True:
    print("1. Add study entry")
    print("2. Analyze productivity")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_entry()
    elif choice == "2":
        analyze()
    elif choice == "3":
        break
    else:
        print("Invalid choice\n")
