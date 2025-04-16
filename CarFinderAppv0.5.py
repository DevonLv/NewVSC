## AutoCountry Car Finder v1.0 ##
# This is a simple car finder application that allows users to search for cars based on various criteria.

#Declarations

#display menu setup
def display_menu():
    #Displays the AutoCountry Vehicle Finder menu
    print("********************************")
    print("AutoCountry Vehicle Finder v1.0")
    print("********************************")
    print("Please enter an option from the menu")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for an authorized vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
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

#save the list to a file
def save_to_file(vehicle_list):
    #Saves the list of vehicles to a file."""
    with open("AuthorizedVehiclesList.txt", "w") as file:
        for vehicle in vehicle_list:
            file.write(f"{vehicle}\n")

#load the list from a file
def load_from_file():
    #Loads the list of vehicles from a file."""
    try:
        with open("AuthorizedVehiclesList.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("AuthorizedVehiclesList.txt not found. Starting with an empty list.")
        return []

#Initialize the AllowedVehiclesList
default_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'Ram 1500']
AllowedVehiclesList = load_from_file()

#Create the file with default vehicles if it doesn't exist or is empty
if not AllowedVehiclesList:
    AllowedVehiclesList = default_vehicles
    save_to_file(AllowedVehiclesList)
    
#File name for storing the allowed vehicles
file_name = "AuthorizedVehiclesList.txt"

#Load the list from the file initially
AllowedVehiclesList = load_from_file()

#Display the menu options
print(display_menu())

#display AuthorizedVehicleList function
def displayVehicles():
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for item in AllowedVehiclesList:
        print(item)
    # Save to file whenever the list is accessed
    save_to_file(AllowedVehiclesList)  
    print(display_menu())

#search for a vehicle function
def searchVehicle():
    searchRequest = input("Please ENTER the full vehicle name: ")
    if searchRequest in AllowedVehiclesList:
        print(f"'{searchRequest}' is an authorized vehicle.")
    else:
        print(f"'{searchRequest}' is NOT an authorized vehicle.")
    print(display_menu())

#add vehicle function
def addVehicle():
    addVehicle = input("Please ENTER the full vehicle name you would like to add: ")
    AllowedVehiclesList.append(addVehicle)
    save_to_file(AllowedVehiclesList)  
    print(f"You have added '{addVehicle}' as an authorized vehicle.")
    print(display_menu())
            
#delete vehicle function
def removeVehicle():
    removeVehicle = input("Please ENTER the full vehicle name you would like to remove: ")
    if removeVehicle in AllowedVehiclesList:
        removeConfirm = input(f"Are you sure you want to remove '{removeVehicle}' from the authorized vehicles list? (yes/no): ").lower()
        if removeConfirm == "yes":
            AllowedVehiclesList.remove(removeVehicle)
            # Save to file after removing a vehicle
            save_to_file(AllowedVehiclesList)  
            print(f"You have REMOVED '{removeVehicle}' from the authorized vehicles list.")
        elif removeConfirm == "no":
            print(f"You have NOT removed '{removeVehicle}' from the authorized vehicles list.")
    else:
        print(f"'{removeVehicle}' is not a vehicle on the authorized vehicles list.")
    print(display_menu())

#exit the program
def exitProgram():
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
    exit()   
    
#Execute the menu functions
while True:
    try:
        choice = int(input("Please select an option: "))
        #print the list of authorized vehicles
        if choice == 1:
            displayVehicles()
        #search for a vehicle
        elif choice == 2:
            searchVehicle()
        #add a new vehicle to the authorized list
        elif choice == 3:
            addVehicle()
        #remove a vehicle from the authorized list
        elif choice == 4:
            removeVehicle()
        #exit the program
        elif choice == 5:
            exitProgram()
        
        #Error catching for invalid input
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")
    except ValueError:
        print("Invalid input. Please enter a number for your choice.")