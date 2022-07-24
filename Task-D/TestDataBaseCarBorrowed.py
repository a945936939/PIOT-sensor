import unittest
import MySQLdb
from DatabaseUtils import DatabaseUtils

class TestDatabaseCarBooked(unittest.TestCase):
    HOST = "34.87.197.175"
    USER = "root"
    PASSWORD = "Hywr7lAqka8qjl7A"
    DATABASE = "CarShare"


    def setUp(self):
        self.connection = MySQLdb.connect(TestDatabaseCarBooked.HOST, TestDatabaseCarBooked.USER,
            TestDatabaseCarBooked.PASSWORD, TestDatabaseCarBooked.DATABASE)
        
        with self.connection.cursor() as cursor:
            cursor.execute("drop table if exists CarBooked")
            cursor.execute("""
                            CREATE TABLE CarBooked(
                                BookedID INT AUTO_INCREMENT NOT NULL, Primary KEY(BookedID),
                                UserID INT NOT NULL,
                                CarID INT NOT NULL,
                                Status enum ('Available', 'Booked'),
                                BorrowedDate DATE NOT NULL,
                                ReturnedDate DATE NOT NULL,
                                Locked enum ('Locked', 'Unlocked'),
                                constraint FKUserID FOREIGN KEY (UserID) references Users (UserID),
                                constraint FKCarID FOREIGN KEY (CarID) references Car (CarID)
                            )""")
            cursor.execute("INSERT INTO CarBooked (UserID, CarID, Status, BorrowedDate, ReturnedDate, Locked) values ('2', '1', 'Booked', '2020-05-24', '2020-05-24', 'Unlocked')")

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
