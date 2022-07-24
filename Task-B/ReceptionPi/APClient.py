import socket, json, sqlite3, sys
sys.path.append("..")
import socketsUtils

from CloudDBUtils import CloudDBUtils


with open("config.json", "r") as file:
    data = json.load(file)
    
HOST = data["masterpi_ip"] # The server's hostname or IP address.
PORT = 63000               # The port used by the server.
ADDRESS = (HOST, PORT)


class APClient():

    def __init__(self):
        print("")
        print("====================================")
        print("CarShare IOT System - [Please Login]")
        print("====================================")
        print("1. Login with Username and Password")
        print("2. Login with Facial Recognition")
        print("3. Exit Program")
        print("====================================")
        print("")
        while (True):
            self.__option = input('Enter an Option: ')
            if (self.__option == "1"):
                self.login()
                break
            if (self.__option == "2"):
                print("")
                print("=== To Be Released ===")
                break
            if (self.__option == "3" or "exit" or "quit"):
                print("\n Thank you for using our CarShare Service - Goodbye! \n")
                exit()
            else:
                print("\n Select a Valid Option! [1,2,3] \n")
                break

    def login(self):
        """
        Function to Login User, checks Credentials against Database to ensure authenticity
        through the Google Cloud SQL Database.
        """
        self.__username = input("Enter Username: ")
        self.__password = input("Enter Password: ")
        with CloudDBUtils() as db:
            if db.checkCredentials(self.__username, self.__password):
                print(db.checkCredentials(self.__username, self.__password))
                print ("\n           ===== Login Successful! =====")
                print("\n ===== Connecting User: -" + self.__username +"- to the MasterPI =====")
                self.connectMaster(self.__username)
                
                

    def connectMaster(self, user):
        """
        Function to Connect Agent PI to MasterPI through Sockets.

        Parameters:
            user: Credential to be sent to the Master PI as a reference and as verification.
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("Connecting to {}...".format(ADDRESS))
            s.connect(ADDRESS)
            print("Connected.")

            print("Logging in as {}".format(self.__username))
            socketsUtils.sendJson(s, user)

            print("Waiting for Master Pi...")
            while(True):
                object = socketsUtils.recvJson(s)
                if("logout" in object):
                    print("Master Pi logged out.")
                    print()
                    break



class main():
    def __init__(self):
        while True:
            APClient()


# Main Function, encapusulates AgentPi Functionality
if __name__ == "__main__":
    main()
