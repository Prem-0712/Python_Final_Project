events = []  

def add_event():
    event_name = input("Enter event name: ")
    client_name = input("Enter client's name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    venue = input("Enter venue name: ")
    status = "Planning"  

    event = {
        "name": event_name,
        "client": client_name,
        "date": date,
        "venue": venue,
        "status": status
    }

    events.append(event)
    print("\n✅Event added successfully !!\n")

add_event()
print(events)

def view_event():
    if not events:
        print("\n❌ No events found.\n")
        return
    
    print("\n📅 All Events:\n")
    for idx, event in enumerate(events, start=1):
         print(f"{idx}. {event['name']} | Client: {event['client']} | Date: {event['date']} | Venue: {event['venue']} | Status: {event['status']}")
    print("\n")

view_event()