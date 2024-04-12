#Task 1

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"},
    "Ticket003": {"Customer": "Steve", "Issue": "Connection Problem", "Status": "open"}
}

def open_new(tick_num, cust_name, issue, status, service):
    if tick_num in service:
        print("This ticket number already exists, try a different number.")
    else:
        service[tick_num] = {"Customer": cust_name, "Issue": issue, "Status": status }


def update_stat(tick_num, service):
    if tick_num in service:
        if input("Would you like to update the status of this ticket(y or n)? ") == "y":
            if service[tick_num]["Status"] == "open":
                service[tick_num].update({"Status": "closed"})
            else:
                service[tick_num].update({"Status": "open"})
    else:
        print("That ticket number does not exist.")

def ticket_display(service):
    choice = input("How would you like to display the tickets?\n(type 'all' or, for a filter type 'open' or 'closed')").lower()
    #if statements to determine which version to show
    if choice == "all":
        for tick_n, ticket_info in service.items():
            print(f"Ticket Number: {tick_n}\n\t Name: {ticket_info["Customer"]}\n\t Issue: {ticket_info["Issue"]}\n\t Status: {ticket_info["Status"]}")
    elif choice == "open":
        for tick_n, ticket_info in service.items():
            if ticket_info["Status"] == "open":
                print(f"Ticket Number: {tick_n}\n\t Name: {ticket_info["Customer"]}\n\t Issue: {ticket_info["Issue"]}\n\t Status: {ticket_info["Status"]}")
    elif choice == "closed":
        for tick_n, ticket_info in service.items():
            if ticket_info["Status"] == "closed":
                print(f"Ticket Number: {tick_n}\n\t Name: {ticket_info["Customer"]}\n\t Issue: {ticket_info["Issue"]}\n\t Status: {ticket_info["Status"]}")
    else:
        print("You typed an invalid choice. Please try again!")
    


open_new("Ticket004", "John", "Login Issue", "closed", service_tickets)
update_stat("Ticket002", service_tickets)

ticket_display(service_tickets)
