#!/usr/bin/env python3
#sudo netstat -ap | grep 31416 [unix command to re-open socket]
import socket, json, sys
sys.path.append("..")
import socketsUtils

from CloudDBUtils import CloudDBUtils
from CarSystem import CarSystem
from LocationGMAPI import LocationGMAPI

HOST = ""    # Empty string means to listen on all IP's on the machine, also works with IPv6.
             # Note "0.0.0.0" also works but only with IPv4.
PORT = 63000 # Port to listen on (non-privileged ports are > 1023).
ADDRESS = (HOST, PORT)

def main():
    """
    Listens to incoming Connection on the Open Ports designated in the Config JSON file.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(ADDRESS)
        s.listen()

        print("Listening on {}...".format(ADDRESS))
        while True:
            print("Waiting for Reception Pi...")
            conn, addr = s.accept()
            with conn:
                print("Connected to {}".format(addr))
                print()

                user = socketsUtils.recvJson(conn)
                menu(user)

                socketsUtils.sendJson(conn, { "logout": True })

def menu(user):

    while(True):
        print("Welcome {}".format(user))
        print("1. Unlock/Lock Car")
        print("2. Return Car")
        print("3. Show Location")
        print("4. Display user details")
        print("5. Logout")
        print()

        text = input("Select an option: ")
        print()
        if (text == "1"):
            print("\n Unlock\Lock Car \n")
            CarSystem().checkLocked(user)
        elif (text == "2"):
            print("\n Return Car \n")
            CarSystem().returnCar(user)
            #CarSystem().unreturnCar(user)
        elif (text == "3"):
            print("\n Show Location \n")
            LocationGMAPI().geoCode(user)
            print("\n")
        elif(text == "4"):
            print("\n ======== Your Details ========")
            print("Username  : {}".format(user))
            print("First Name: {}".format(CloudDBUtils().summonFirstName(user)))
            print("Last Name : {}".format(CloudDBUtils().summonLastName(user)))
            print("Email Address : {}".format(CloudDBUtils().summonEmail(user)))
            print("=================================== \n")
        elif(text == "5"):
            print("Goodbye.")
            print()
            break
        else:
            print("Invalid input, try again.")
            print()

# Execute program.
if __name__ == "__main__":
    main()
