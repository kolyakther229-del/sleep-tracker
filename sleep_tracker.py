from datetime import datetime, timedelta

# Function to calculate sleep duration 
def calculate_sleep(sleep_time, wake_time):
    fmt = "%H:%M"
    sleep = datetime. strptime(sleep_time, fmt)
    waka = datetime. strtime(wake_time, fmt)

    #Handle overnight sleep
    if wake < sleep:
        wake += timedelta(days=1)

    duration = wake - sleep
    hours = duration.total_seconds() / 3600
    return round(hours, 2)
# Function to check sleep quality
def sleep_quality(hours): 
    if hours < 5:
        return "Poor ❌","Try sleeping earlier and avoid mobile at night."
    elif 5 <= hours < 7:
        return"Average ⚠️", "You need a bit more rest."
    elif 7 <= hours <=9:
        return"Healthy ✅", "Great job! Keep this routine."
    else:
        return"Oversleep 😴", "Try to maintain a balanced schedule"

#Function to save history
def save_history(date, sleep_time, wake_time, hours, quality):
    with open("sleep_history.txt", "a") as file:
        file.write(f"{date} | Sleep: {sleep_time} | Wake: {wake_time} | {hours} hrs | {quality}\n")

# Function to view history
def view_history():
    try:
        with open("sleep_history.txt", "r") as file:
            data = file.readlines()
            if not data:
                print("\nNo history found.\n")
            else:
                print("\n📅 Sleep History (Last 5 Records):")
                for line in data[-5:]:
                    print(line.strip())
    except FileNotFoundError:
        print("\nNo history file found yet.\n")

# Main program
while True:
    print("\n🌙 Sleep Tracker Menu")
    print("1. Add Sleep Record")
    print("2. View History")
    print("3. Exit")

    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        sleep_time = input("Enter sleep time (HH:MM): ")
        wake_time = input("Enter wake time (HH:MM): ")

        try:
            hours = calculate_sleep(sleep_time, wake_time)
            quality, suggestion = sleep_quality(hours)

            print(f"\n🛌 You slept: {hours} hours")
            print(f"📊 Sleep Quality: {quality}")
            print(f"💡 Suggestion: {suggestion}")

            today = datetime.now().strftime("%Y-%m-%d")
            save_history(today, sleep_time, wake_time, hours, quality)

        except:
            print("\n❌ Invalid time format! Please use HH:MM (e.g., 23:00)\n")

    elif choice == "2":
        view_history()

    elif choice == "3":
        print("Goodbye! 😴")
        break

    else:
        print("Invalid choice! Try again.")