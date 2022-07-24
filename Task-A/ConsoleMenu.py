from DatabaseUtils import DatabaseUtils
from BookingSystem import BookingSystem

ConsoleUser = ""

"""
The ConsoleMenu class. This class handles the menu for a user
"""
class ConsoleMenu:

    def __init__(self):
        self.cloud = DatabaseUtils()
        self.consoleuser = ConsoleUser
        print("")
        print("====================================")
        print("CarShare IOT System - [Console Menu System]")
        print("====================================")
        print("1. Register as a NEW USER")
        print("2. Login")
        print("3. Exit Program")
        print("====================================")
        print("")
        while (True):
            self.__option = input('Enter an Option: ')
            if (self.__option == "1"):
                print("Register System")
                self.regUser()
                break
            if (self.__option == "2"):
                print("")
                print("Login System")
                if self.login() == False:
                    break
                else:
                    #textUser = self.login()
                    BookingSystem(self.consoleuser)
                    break
            if (self.__option == "3" or "exit" or "quit"):
                print("\n Thank you for using our CarShare Service - Goodbye! \n")
                exit()
            else:
                print("\n Select a Valid Option! [1,2,3] \n")
                break

    def regUser(self):
        """Contains complete registration process.

        Prompts user for registration information and
        stores user input into database after the 
        attributes are validated.

        Attributes
        ----------
        __username : str
            Takes user input as their username
        __password : str
            Takes user input as their password
        __firstname : str
            Takes user input as their first name
        __lastname : str
            Takes user input as their last name
        __email : str 
            Takes user input as their email address
        """

        self.__username = input("Enter Username: ")
        self.__password = input("Enter Password: ")
        self.__firstname = input("Enter First Name: ")
        self.__lastname = input("Enter Last Name: ")
        self.__email = input("Enter Email: ")
        cur = self.cloud.connection
        with cur.cursor() as cursor:
            sql = "INSERT INTO Users (Username, Password, FirstName, LastName, Email) VALUES (%s,%s,%s,%s,%s)"
            val = (self.__username, self.__password, self.__firstname, self.__lastname,self.__email)
            cursor.execute(sql, val)
            self.cloud.connection.commit()
            print("User Added %s", self.__username + " Welcome" + self.__firstname)
                                
    def login(self):
        """Prompts user with username and password

        Prompts the user for username and password and if
        successful user establishes connection with server.

        Attributes
        ----------
        __username : str
            The string the user inputs as their username
        __password : str
            The string the user inputs as their password
        """

        self.__username = input("Enter Username: ")
        self.__password = input("Enter Password: ")
        with DatabaseUtils() as db:
            if (db.checkCredentials(self.__username, self.__password) == True):
                print(db.checkCredentials(self.__username, self.__password))
                print ("\n    ===== Login Successful! =====")
                self.consoleuser = self.__username
                print("\n ===== Connecting User: -" + self.consoleuser +" ========")
                return 
            else: 
                return False


class main():
    def __init__(self):
        while True:
            ConsoleMenu()


# Main Function, encapusulates AgentPi Functionality
if __name__ == "__main__":
    main()
