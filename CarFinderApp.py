## AutoCountry Car Finder v0.3 ##
# This is a simple car finder application that allows users to search for cars based on various criteria.

# Declarations
AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
def display_menu():
    """Displays the AutoCountry Vehicle Finder menu."""
    print("********************************")
    print("AutoCountry Vehicle Finder v0.3")
    print("********************************")
    print("Please enter an option from the menu")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for an authorized vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. Exit")
    print("********************************")
    return ""

#create search function for Authorized Vehicle list
def searchVehicle(vehicle_name):
    #Searches for a vehicle in the authorized list
    if vehicle_name in AllowedVehiclesList:
        return f"'{vehicle_name}' is an authorized vehicle."
    #If the vehicle is not found, return a message indicating that it is not authorized.
    else:
        return f"'{vehicle_name}' is NOT an authorized vehicle."


#Display the menu options
print(display_menu())

#Execute the menu functions
while True:
    try:
        choice = int(input("Please select an option: "))
        #print the list of authorized vehicles
        if choice == 1:
            print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
            for item in AllowedVehiclesList:
                print(item)
            print(display_menu())

        #print the selected vehicle
        elif choice == 2:
            searchRequest = input("Please ENTER the full vehicle name: ")
            result = searchVehicle(searchRequest)
            print(result)
            print(display_menu())

        #add a new vehicle to the authorized list
        elif choice == 3:
            addVehicle = input("Please ENTER the full vehicle name you would like to add: ")
            AllowedVehiclesList.append(addVehicle)
            print(f"'{addVehicle}' has been added to the authorized vehicle list.")
            print(display_menu())

        #exit the while loop, ending the program.
        elif choice == 4:
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break

        #Error catching for invalid input
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")
    except ValueError:
        print("Invalid input. Please enter a number for your choice.")