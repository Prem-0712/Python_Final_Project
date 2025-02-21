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

# search_event()

def update_event():
    if not events:
        print("\n❌ No events available to update.\n")
        return
    
    search_key = input("Enter event name or client name to find the event: ").strip().lower()
    
    event_to_update = None
    for event in events:
        if search_key in event["name"].lower() or search_key in event["client"].lower():
            event_to_update = event
            break  # Stop after finding the first matching event
    
    if event_to_update is None:
        print("\n❌ No matching events found.\n")
        return

    print("\n🔍 Event Found:\n")
    print(f"{event_to_update['name']} | Client: {event_to_update['client']} | Date: {event_to_update['date']} | Venue: {event_to_update['venue']} | Status: {event_to_update['status']}")
    
    update_status_only = input("\nDo you want to update only the status? (yes/no): ").strip().lower()
    
    if update_status_only == "yes":
        new_status = input("Enter new status (Planning/Confirmed/Completed): ").strip().capitalize()
        if new_status:
            event_to_update["status"] = new_status
        print("\n✅ Event status updated successfully!\n")
    
    else:
        new_name = input(f"Enter new event name ({event_to_update['name']}): ").strip()
        if new_name:
            event_to_update["name"] = new_name
        
        new_client = input(f"Enter new client name ({event_to_update['client']}): ").strip()
        if new_client:
            event_to_update["client"] = new_client
        
        new_date = input(f"Enter new date ({event_to_update['date']}): ").strip()
        if new_date:
            event_to_update["date"] = new_date
        
        new_venue = input(f"Enter new venue ({event_to_update['venue']}): ").strip()
        if new_venue:
            event_to_update["venue"] = new_venue
        
        new_status = input(f"Enter new status ({event_to_update['status']}): ").strip().capitalize()
        if new_status:
            event_to_update["status"] = new_status
        
        print("\n✅ Event updated successfully!\n")

update_event()

def delete_event():
    if not events:
        print("\n❌ No events available to delete.\n")
        return

    search_key = input("Enter event name or client name to find the event: ").strip().lower()
    
    found_events = [event for event in events if search_key in event["name"].lower() or search_key in event["client"].lower()]

    if not found_events:
        print("\n❌ No matching events found.\n")
        return

    print("\n🗑️ Matching Events:\n")
    for idx, event in enumerate(found_events, start=1):
        print(f"{idx}. {event['name']} | Client: {event['client']} | Date: {event['date']} | Venue: {event['venue']} | Status: {event['status']}")
    
    try:
        choice = int(input("\nEnter the number of the event you want to delete: "))
        event_to_delete = found_events[choice - 1]
    except (ValueError, IndexError):
        print("\n❌ Invalid choice.\n")
        return

    confirm = input(f"Are you sure you want to delete '{event_to_delete['name']}'? (yes/no): ").strip().lower()
    if confirm == "yes":
        events.remove(event_to_delete)
        print("\n✅ Event deleted successfully!\n")
    else:
        print("\n❌ Deletion canceled.\n")

delete_event()