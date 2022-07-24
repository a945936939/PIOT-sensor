#Used for connecting to the python MySQLdb and creating Tables & Fields.class DatabaseUtils:
import MySQLdb

class DatabaseUtils: 
    HOST = "34.87.197.175"
    USER = "root"
    PASSWORD = "Hywr7lAqka8qjl7A"
    DATABASE = "CarShare"


    def __init__(self):
        connection = None
        if(connection == None):
            connection = MySQLdb.connect(DatabaseUtils.HOST, DatabaseUtils.USER,
                DatabaseUtils.PASSWORD, DatabaseUtils.DATABASE)
        self.connection = connection
        self.host = DatabaseUtils.HOST
        self.user = DatabaseUtils.USER
        self.password = DatabaseUtils.PASSWORD
        self.database = DatabaseUtils.DATABASE
        self.db = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password, db=self.database) 
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self
    
    def login(self):
        with DatabaseUtils() as db:
            for Users in db.getUsers():
                print(Users)


    def checkCredentials(self, user, password):
        with self.connection.cursor() as cursor:
            #print(cursor.execute("select * from Users where Username = 'JERRY1'"))
            #dbUSER = cursor.execute("SELECT Username as VALUE FROM Users WHERE Username = %s", [user])
            cursor.execute("SELECT Username as VALUE FROM Users WHERE Username=%s and Password=%s", [user, password])
            dbUSER = cursor.fetchone()
            print(dbUSER)
            cursor.execute("SELECT Password as VALUE FROM Users WHERE Password=%s and Username=%s", [password, user])
            dbPASS = cursor.fetchone()
            print(dbPASS)
            if (dbUSER == None) or (dbPASS == None):
                print("\n User is not in the Database or Password is Incorrect \n")
                return False
            else:
             return True

    def summonFirstName(self, user):
        with self.connection.cursor() as cursor:
         cursor.execute("SELECT Firstname as VALUE FROM Users WHERE Username=%s", [user])
         fNameText = cursor.fetchone()
         return fNameText[0]

    def summonLastName(self, user):
        with self.connection.cursor() as cursor:
         cursor.execute("SELECT Lastname as VALUE FROM Users WHERE Username=%s", [user])
         lNameText = cursor.fetchone()
         return lNameText[0]


    def summonEmail(self, user):
        with self.connection.cursor() as cursor:
         cursor.execute("SELECT Email as VALUE FROM Users WHERE Username=%s", [user])
         eMailText = cursor.fetchone()
         return eMailText[0]


    def __exit__(self, type, value, traceback):
        self.close()
