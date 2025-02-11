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

def search_event():
    if not events:
        print("\n❌ No events to search.\n")
        return

    search_key = input("Enter event name, client name, or date (YYYY-MM-DD) to search: ").strip().lower()

    found_events = [event for event in events if search_key in event["name"].lower() or 
                    search_key in event["client"].lower() or search_key in event["date"]]

    if not found_events:
        print("\n❌ No matching events found.\n")
        return

    print("\n🔍 Search Results:\n")
    for idx, event in enumerate(found_events, start=1):
        print(f"{idx}. {event['name']} | Client: {event['client']} | Date: {event['date']} | Venue: {event['venue']} | Status: {event['status']}")
    print("\n")

search_event()