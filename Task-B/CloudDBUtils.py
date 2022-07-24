import MySQLdb

class CloudDBUtils: 

    """
    CloudDBUtils is a Class that handles the connection betwen the Google Cloud SQL Server and the 
    CarShare Applications various IO Consoles throughout the IOT System.
    """
    HOST = "34.87.197.175"
    USER = "root"
    PASSWORD = "Hywr7lAqka8qjl7A"
    DATABASE = "CarShare"

    def __init__(self):
        """
        Initialises the connection to the Google Cloud SQL Server with credentials.

        Parameters: 
            connection: established connection to the cloud..
            host: Host Address assigned by Google Cloud Services.
            password: Key to the Database!
            db: Class Variable for Class Object Reference.
            cursor: mySQLdb connection handle.
        """
        connection = None
        if(connection == None):
            connection = MySQLdb.connect(CloudDBUtils.HOST, CloudDBUtils.USER,
                CloudDBUtils.PASSWORD, CloudDBUtils.DATABASE)
        self.connection = connection
        self.host = CloudDBUtils.HOST
        self.user = CloudDBUtils.USER
        self.password = CloudDBUtils.PASSWORD
        self.database = CloudDBUtils.DATABASE
        self.db = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password, db=self.database) 
        self.cursor = self.connection.cursor()

    def close(self):
        """Closes Connection"""
        self.connection.close()

    def __enter__(self):
        return self
    
    def printUsers(self):
        """
        Print all Users in the Database.
        """
        with CloudDBUtils() as db:
            for Users in db.getUsers():
                print(Users)


    def checkCredentials(self, user, password):
        """
        Checks if the User exists in the Database returns True if it does and False if it does not.

        Parameters:
            user: Username of the Login Attempt.
            password: Password of the Login Attempt.
        """
        with self.connection.cursor() as cursor:
            #print(cursor.execute("select * from Users where Username = 'JERRY1'"))
            #dbUSER = cursor.execute("SELECT Username as VALUE FROM Users WHERE Username = %s", [user])
            cursor.execute("SELECT Username as VALUE FROM Users WHERE Username=%s and Password=%s", [user, password])
            dbUSER = cursor.fetchone()
            #print(dbUSER)
            cursor.execute("SELECT Password as VALUE FROM Users WHERE Password=%s and Username=%s", [password, user])
            dbPASS = cursor.fetchone()
            #print(dbPASS)
            if (dbUSER == None) or (dbPASS == None):
                print("\n User is not in the Database or Password is Incorrect \n")
                return False
            else:
             return True

    def summonFirstName(self, user):
        """
        Returns FirstName of the User.

        Parameters:
            user: Username of current User.
        """
        with self.connection.cursor() as cursor:
         cursor.execute("SELECT Firstname as VALUE FROM Users WHERE Username=%s", [user])
         fNameText = cursor.fetchone()
         return fNameText[0]

    def summonLastName(self, user):
        """
        Returns LastName of the User.

        Parameters:
            user: Username of current User.
        """
        with self.connection.cursor() as cursor:
         cursor.execute("SELECT Lastname as VALUE FROM Users WHERE Username=%s", [user])
         lNameText = cursor.fetchone()
         return lNameText[0]


    def summonEmail(self, user):
        """
        Returns Email of the User.

        Parameters:
            user: Username of current User.
        """
        with self.connection.cursor() as cursor:
         cursor.execute("SELECT Email as VALUE FROM Users WHERE Username=%s", [user])
         eMailText = cursor.fetchone()
         return eMailText[0]


    def __exit__(self, type, value, traceback):
        self.close()
