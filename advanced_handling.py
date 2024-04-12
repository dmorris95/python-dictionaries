#Task 1

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"},
    "103": {"status": "available", "customer": ""},
    "104": {"status": "booked", "customer": "John Smith"}
}

def book_room(rooms, num, cust_name): #mark as booked and add name
    if num not in rooms:
        print("This room number does not exist.")
    else:
        rooms[num] = {"status": "booked", "customer" : cust_name}
        print("Room successfully booked.")

def checkout(room, num): #remove as available and remove customer
    if num not in room:
        print("Room number does not exist")
    else:
        room[num] = {"status" : "available", "customer": ""}
        print("Customer has been checked out!")

def display_status(room):
    for num, room_info in room.items():
        print(f"Room Number: {num}")
        stat = room_info["status"]
        cust = room_info["customer"]
        if cust == "":
            print(f"Status of room: {stat}\n")
        else:
            print(f"Status of room: {stat}\nCustomer Name: {cust}\n")

book_room(hotel_rooms, "103", "Larry Bird")
checkout(hotel_rooms, "102")

display_status(hotel_rooms)



#Task 2
#handle cases where no matches are found, uses a case-insen


products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20},
    "3": {"name": "Computer", "category": "Electronics", "price": 350},
    "4": {"name": "laptop", "category": "Electronics", "price": 650}
}

def search_products(products, prod_name):
    count = 0
    try:
        for n, product_info in products.items():
            if prod_name.lower() in product_info["name"].lower():
                count += 1
                print(f"Product found: {n}: {product_info["name"]}----{product_info["category"]}----{product_info["price"]}}}")
        if count == 0:
            print(f"No products were found matching '{prod_name}'")
    except ValueError:
        print("An invalid product was searched for.")
search_products(products, "comp")
