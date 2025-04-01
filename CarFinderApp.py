## AutoCountry Car Finder v0.1 ##
# This is a simple car finder application that allows users to search for cars based on various criteria.

# Declarations
AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
def display_menu():
    """Displays the AutoCountry Vehicle Finder menu."""
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please enter an option from the menu")
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")

#Display the menu options
def main():
    """Main function to handle program execution."""
    display_menu()

#Execute the menu functions
    while True: 
        try:
            choice = int(input("Please select an option: "))

            # print the list of authorized vehicles
            if choice == 1:
                print("Printing all Authorized Vehicles...")
                print(AllowedVehiclesList) 
                
            # exit the while loop, ending the program.
            elif choice == 2:
                print("Exiting...")
                break 
            
            else:
                print("Invalid choice. Please enter 1 or 2.")

        except ValueError:
            print("Invalid input. Please do as told.")