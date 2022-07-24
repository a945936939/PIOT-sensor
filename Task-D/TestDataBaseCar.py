import unittest
import MySQLdb
from DatabaseUtils import DatabaseUtils

class TestDatabaseCar(unittest.TestCase):
    HOST = "34.87.197.175"
    USER = "root"
    PASSWORD = "Hywr7lAqka8qjl7A"
    DATABASE = "CarShare"

    def setUp(self):
        self.connection = MySQLdb.connect(TestDatabaseCar.HOST, TestDatabaseCar.USER,
            TestDatabaseCar.PASSWORD, TestDatabaseCar.DATABASE)
        
        with self.connection.cursor() as cursor:
            cursor.execute("drop table if exists Car")
            cursor.execute("""
                            CREATE TABLE Car(
                                CarID INT AUTO_INCREMENT NOT NULL, PRIMARY KEY(CarID),
                                Make VARCHAR(100) NOT NULL,
                                BodyType VARCHAR(100) NOT NULL,
                                Colour VARCHAR(100) NOT NULL,
                                Seats INT NOT NULL,
                                Location VARCHAR(100) NOT NULL,
                                CostperHr DECIMAL(15,2) NOT NULL,
                                ShareDate DATE NOT NULL 
                            )""")
            cursor.execute("INSERT INTO Car (Make, BodyType, Colour, Seats, Location, CostperHr, ShareDate) values ('test-make', 'sedan', 'black', 4, 'Melbourne', 12300, '2020-05-12');")

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
