import csv

def add_event():
    event_name = input("Enter event name: ")
    client_name = input("Enter client's name: ")
    date = input("Enter date (yyyy-mm-dd): ")
    venue = input("Enter venue name: ")
    status = "Planning"  

    with open("events.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([event_name, client_name, date, venue, status])

    print(f"✅ Event '{event_name}' added successfully!")


# add_event()

def view_events():
    # Open the CSV file in read mode
    with open("events.csv", mode="r") as file:
        reader = csv.reader(file)
        
        # Read all rows into a list
        events = list(reader)

        # Check if the file is empty (no events)
        if not events:
            print("No events found!")
            return  # Exit function
        
        # Print event details in a structured way
        print("\n📅 Saved Events:")
        for event in events:
            print(f"📌 {event[0]} | Client: {event[1]} | Date: {event[2]} | Venue: {event[3]} | Status: {event[4]}")

# view_events()import csv

def search_event():
    search_key = input("Enter event name, date (YYYY-MM-DD), or client name to search: ").strip()

    with open("events.csv", mode="r") as file:
        reader = csv.reader(file)
        events = list(reader)

        found = False
        print("\n🔍 Search Results:")
        for row in events:
            if search_key.lower() in [item.lower() for item in row]:  # Case-insensitive search
                print(f"📌 {row[0]} | Client: {row[1]} | Date: {row[2]} | Venue: {row[3]} | Status: {row[4]}")
                found = True

        if not found:
            print("❌ No event found.")

# ✅ Test the function
search_event()