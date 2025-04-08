## AutoCountry Car Finder v0.1 ##
# This is a simple car finder application that allows users to search for cars based on various criteria.

# Declarations
AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
def display_menu():
    """Displays the AutoCountry Vehicle Finder menu."""
    print("********************************")
    print("AutoCountry Vehicle Finder v0.2")
    print("********************************")
    print("Please enter an option from the menu")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for an authorized vehicle")
    print("3. Exit")
    print("********************************")
    return ""

#create search function for Authorized Vehicle list
def searchVehicle(vehicle_name):
    #Searches for a vehicle in the authorized list
    if vehicle_name in AllowedVehiclesList:
        return f"'{vehicle_name}' is an authorized vehicle."
        print(display_menu()) 
    #If the vehicle is not found, return a message indicating that it is not authorized.
    else:
        return f"'{vehicle_name}' is NOT an authorized vehicle."
        print(display_menu())

#Display the menu options
print(display_menu())

#Execute the menu functions
while True:
    try:
        choice = int(input("Please select an option:"))
            #print the list of authorized vehicles
        if choice == 1:
                print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
                for item in AllowedVehiclesList:
                    print(item)
                print(display_menu())
                choice = int(input("Please select an option:"))
                
            #print the selected vehicle
        elif choice == 2:
                searchRequest = input("Please ENTER the full vehicle name: ")
                result = searchVehicle(searchRequest)
                print(result)
                print(display_menu())
            
            #exit the while loop, ending the program.
        elif choice == 3:
                print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
                break 
            #Error catching for invalid input
    except ValueError:
        print("Invalid choice. Please enter 1, 2 or 3.")