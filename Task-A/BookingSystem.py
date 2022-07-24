from DatabaseUtils import DatabaseUtils

class BookingSystem:
    """
    The BookingSystem class. This class handles the Booking system
    """

    def __init__(self, user):
        self.cloud = DatabaseUtils()
        self.user = user
        print("User is: " + self.user)
        print("************************************************")
        print("CarShare Booking System - [Welcome Car Sharer!]")
        print("************************************************")
        print("1. View the History of My Booked Cars")
        print("2. Show all Available Cars")
        print("3. Search a Car")
        print("4. Book a Car")
        print("5. Cancel a Booking")
        print("6. Logout")
        print("************************************************")
        print("")
        while (True):
            self.__option = input('Enter an Option: ')
            if (self.__option == "1"):
                print("View the History of My Booked Cars")
                BookingSystem().viewBookingHistory(user)
                break
            if (self.__option == "2"):
                print("")
                print("Show all Available Cars")
                BookingSystem().showAvailableCars(user)
                break
            if (self.__option == "3"):
                print("")
                print("Search a Car")
                BookingSystem().searchCars(user)
                break
            if (self.__option == "4"):
                print("")
                print("Book a Car")
                BookingSystem().bookCar(user)
                break
            if (self.__option == "5"):
                print("")
                print("Cancel a Booking")
                BookingSystem().canelBooking(user)
                break
            if (self.__option == "6" or "exit" or "quit"):
                print("\n Thank you for using our CarShare Service - Goodbye! \n")
                exit()
            else:
                print("\n Select a Valid Option! [1,2,3] \n")
                BookingSystem()


    def viewBookingHistory(self,user):
        """
        Prints a list of cars that the user has booked
        """
        return

    def showAvailableCars(self,user):
        """
        Prints a list of all available cars
        """
        return

    def searchCars(self,user):
        """
        Searches database to print fields of car properties in the console
        """
        return
    



    def bookCar(self,user):
        """
        Books a car that gets added into Google Calendar
        """
        return 

    def canelBooking(self,user):
        """
        Removes event from Google Calendar 
        """
        return 
