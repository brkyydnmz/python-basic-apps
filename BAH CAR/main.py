from rent import CarRent, BikeRent, Customer

bike = BikeRent(75)
car = CarRent(50)
customer = Customer()

main_menu = True

while True:
    
    if main_menu:
        print("""
              ***** BAH Vehicle Rental Shop *****
              A. Bike Menu
              B. Car Menu
              Q. Exit
              """)
        main_menu = False
        
        choice = input("Enter choice: ")
        
    if choice == "A" or choice == "a":
        
        print("""
              ****** BAH BIKE MENU *****
              1. Display available bikes
              2. Request a bike on hourly basis $ 2
              3. Request a bike on daily basis $ 15
              4. Return a bike
              5. Main Menu
              6. Exit
              """)
        choice = input("Enter choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("It is not integer")
            continue
        
        if choice == 1:
            bike.displayStock()
            choice = "A"
        elif choice == 2:
            customer.rentalTime_b = bike.rentHourly(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 1
            main_menu = True
            print("----------------")
        elif choice == 3:
            customer.rentalTime_b = bike.rentDaily(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 2
            main_menu = True
            print("----------------")
        elif choice == 4:
            customer.bill = bike.returnVehicle(customer.returnVehicle("bike"),"bike")
            customer.rentalBasis_b, customer.rentalTime_b, customer.bikes = 0,0,0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice ==6:
            break
        else:
            print("Invalid input. Please enter a number between 1-6 ")
            main_menu = True
        
    elif choice == "B" or choice == "b":
        
        print("""
              ****** BAH CAR MENU *****
              1. Display available cars
              2. Request a car on hourly basis $ 15
              3. Request a car on daily basis $ 100
              4. Return a car
              5. Main Menu
              6. Exit
              """)
        choice = input("Enter choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("It is not integer")
            continue
        
        if choice == 1:
            car.displayStock()
            choice = "B"
        elif choice == 2:
            customer.rentalTime_c = car.rentHourly(customer.requestVehicle("car"))
            customer.rentalBasis_c = 1
            main_menu = True
            print("----------------")
        elif choice == 3:
            customer.rentalTime_c = car.rentDaily(customer.requestVehicle("car"))
            customer.rentalBasis_c = 2
            main_menu = True
            print("----------------")
        elif choice == 4:
            customer.bill = car.returnVehicle(customer.returnVehicle("car"),"car")
            customer.rentalBasis_c, customer.rentalTime_c, customer.cars = 0,0,0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice ==6:
            break
        else:
            print("Invalid input. Please enter a number between 1-6 ")
            main_menu = True
        
    elif choice == "Q" or choice == "q":  
        break
    
    else:
        print("Invalid Input. Please Enter A-B-Q")
        main_menu = True
    
    print("Thank you for using the BAH Vehicle Rental Shop")
    
    input("Please Write a Feedback: ")
    
    print("Thank you for using the Feedback interface.Please choose someone.")
    
    
    
    print("""
    1-Send feedback to support center.
    2-Continue.
    """)
        
    
    
    return_menu = True
    while True:
        
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            print("Sent your feedback please wait 30-60 seconds for support.")
        
        elif choice == 2:
            break
        
        else:
            print("Invalid Input. Please Enter 1-2")
            continue
            return_menu = True
    




        
        
        
        
        
