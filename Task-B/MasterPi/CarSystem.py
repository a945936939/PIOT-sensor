import MySQLdb
from CloudDBUtils import CloudDBUtils

"""
The CarSystem class. This class handles the function of unlock
and return of the car.
"""
class CarSystem:
    def __init__(self):
        self.cloud = CloudDBUtils()

    def fetchid(self, user):
        """
        Returns the UserID assigned to the Username passed as a Parameter.
        
        Parameters:
            user: Username.
        """
        cur = self.cloud.connection
        with cur.cursor() as cursor:
            cursor.execute("SELECT UserID as VALUE FROM Users WHERE Username=%s", [user])
            dbUserNametoID = cursor.fetchone()
            self.cloud.connection.commit()
        return dbUserNametoID

    def returnCar(self, user):
        """
        Changes the status of the Car from being Booked to being Available for another person to Book. 

        Parameters:
         user: Booked Car's Client.
        """
        cur = self.cloud.connection
        with cur.cursor() as cursor:
            cursor.execute("SELECT UserID as VALUE FROM Users WHERE Username=%s", [user])
            dbUserNametoID = cursor.fetchone()
            cursor.execute("UPDATE CarBooked SET Status = 'Available' WHERE UserID = %s", [dbUserNametoID[0]]) 
            self.cloud.connection.commit()
            print("Car Returned [STATUS SET TO AVAILABLE")

    def unreturnCar(self, user):
        """
        Function for debugging.
        """
        cur = self.cloud.connection
        with cur.cursor() as cursor:
            cursor.execute("SELECT UserID as VALUE FROM Users WHERE Username=%s", [user])
            dbUserNametoID = cursor.fetchone()
            #UPDATE CarBooked SET Status = 'Booked' WHERE UserID = 2
            cursor.execute("UPDATE CarBooked SET Status = 'Booked' WHERE UserID =%s", [dbUserNametoID[0]]) 
            self.cloud.connection.commit()
            print("Car Shared Out [STATUS SET TO BOOKED]")

    def checkLocked(self, user):
        """
        Checks if the Car is Locked and 'Locks' it if it is unlocked, conversely Unlocks it
        if the Car is Locked 

        Parameters:
            user: User who's Car is to be Locked/Unlocked
        """
        cur = self.cloud.connection
        uid= CarSystem().fetchid(user)
        with cur.cursor() as cursor:
           cursor.execute("SELECT Locked FROM CarBooked WHERE UserID=%s", [uid[0]])
           lockStatus = cursor.fetchone()
        if lockStatus[0] == "Unlocked":
           CarSystem().lockCar(user)
        else:
           CarSystem().unlockCar(user)


    def lockCar(self, user):
        """
        Locks User's Car.

        Parameters:
            user: Username.
        """
        cur = self.cloud.connection
        uid= CarSystem().fetchid(user)
        with cur.cursor() as cursor:
           cursor.execute("UPDATE CarBooked SET Locked = 'Locked' WHERE UserID =%s", [uid[0]])
           self.cloud.connection.commit()
        print("Car is now Locked")
        return True

    def unlockCar(self, user):
        """
        Unlocks User's Car.

        Parameters:
            user: Username.
        """
        cur = self.cloud.connection
        uid= CarSystem().fetchid(user)
        with cur.cursor() as cursor:
           cursor.execute("UPDATE CarBooked SET Locked = 'Unlocked' WHERE UserID =%s", [uid[0]])
           self.cloud.connection.commit()
        print("Car is now Unlocked")
        return True