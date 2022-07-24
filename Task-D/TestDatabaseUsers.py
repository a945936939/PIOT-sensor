import unittest
import MySQLdb
from DatabaseUtils import DatabaseUtils

class TestDatabaseUsers(unittest.TestCase):
    HOST = "34.87.197.175"
    USER = "root"
    PASSWORD = "Hywr7lAqka8qjl7A"
    DATABASE = "CarShare"


    def setUp(self):
        self.connection = MySQLdb.connect(TestDatabaseUsers.HOST, TestDatabaseUsers.USER,
            TestDatabaseUsers.PASSWORD, TestDatabaseUsers.DATABASE)
        
        with self.connection.cursor() as cursor:
            cursor.execute("drop table if exists Users")
            cursor.execute("""
                            CREATE TABLE Users(
                                UserID INT AUTO_INCREMENT NOT NULL, PRIMARY KEY(UserID),
                                    Username VARCHAR(100) NOT NULL,
                                    Password VARCHAR(100) NOT NULL,
                                    FirstName VARCHAR(100) NOT NULL,
                                    LastName VARCHAR(100) NOT NULL,
                                    Email VARCHAR(100) NOT NULL
                            )""")
            cursor.execute("INSERT INTO Users (Username, Password, FirstName, LastName, Email) VALUES ('u1', '123', 'test', 'user', 's122@student.email');")

        self.connection.commit()

    def tearDown(self):
        try:
            self.connection.close()
        except:
            pass
        finally:
            self.connection = None

    def count(self):
        with self.connection.cursor() as cursor:
            cursor.execute("select count(*) from Car")
            return cursor.fetchone()[0]

    def exists(self, CarID):
        with self.connection.cursor() as cursor:
            cursor.execute("select count(*) from Car where CarID = %s", (CarID))
            return cursor.fetchone()[0] == 1

    def test_insert(self):
        with DatabaseUtils(self.connection) as db:
            count = self.count()
            self.assertTrue(db.insertCar("5"))
            self.assertTrue(count + 1 == self.count())

    def test_get(self):
        with DatabaseUtils(self.connection) as db:
            self.assertTrue(self.count() == len(db.getcar()))

    def test_delete(self):
        with DatabaseUtils(self.connection) as db:
            count = self.count()
            cid = 1

            self.assertTrue(self.exists(cid))

            db.deleteCar(cid)

            self.assertFalse(self.exists(cid))
            self.assertTrue(count - 1 == self.count())

if __name__ == "__main__":
    unittest.main()
