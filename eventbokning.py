from datetime import datetime

bookings = []

def book_event():
    event_name = input("Vad är evenemangets namn?")
    event_date_str = input("Ange datum för evenemanget (ÅÅÅÅ-MM-DD): ")
    event_date = datetime.strptime(event_date_str, "%Y-%m-%d")
    
    start_time_str = input("När ska evenemanget börja? (HH:MM)")
    end_time_str = input("När ska evenemanget sluta? (HH:MM)")
    
    start_time = datetime.strptime(start_time_str, "%H:%M")
    end_time = datetime.strptime(end_time_str, "%H:%M")
    
    if end_time <= start_time:
        print("Fel: Sluttiden kan inte vara tidigare än starttiden.")
        return
    
    for booking in bookings:
        if booking["event_date"] == event_date:
            if (start_time < booking["end_time"] and end_time > booking["start_time"]):
                print("Tyvärr, lokalen är redabn bokan under denna tid")
                return
            
    bookings.append({
        "event_name": event_name,
        "event_date": event_date,
        "start_time": start_time,
        "end_time": end_time
    })
    print(f"Evenemanget '{event_name}' är nu bokat {event_date_str} mellan {start_time_str} och {end_time_str}")
    with open ("bookings.txt", "a", encoding="UTF-8") as file:
            file.write(f"\nEvenemanget '{event_name}' är nu bokat {event_date_str} mellan {start_time_str} och {end_time_str}\n")
    
while True:
    book_event()
    cont = input("Vill du boka ett annat event? (j/n)")
    if cont.lower() != 'j':
        
        
            
        break