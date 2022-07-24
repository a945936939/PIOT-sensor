import unittest
import MySQLdb
from DatabaseUtils import DatabaseUtils

class TestDatabaseBookedHistory(unittest.TestCase):
    HOST = "34.87.197.175"
    USER = "root"
    PASSWORD = "Hywr7lAqka8qjl7A"
    DATABASE = "CarShare"

    def setUp(self):
        self.connection = MySQLdb.connect(TestDatabaseBookedHistory.HOST, TestDatabaseBookedHistory.USER,
            TestDatabaseBookedHistory.PASSWORD, TestDatabaseBookedHistory.DATABASE)
        
        with self.connection.cursor() as cursor:
            cursor.execute("drop table if exists BookedHistory")
            cursor.execute("""
                    CREATE TABLE if not exists BookedHistory(
                        BHistoryID INT AUTO_INCREMENT NOT NULL, Primary KEY(BHistoryID),
                        UserID INT NOT NULL,
                        CarID INT NOT NULL,
                        constraint FKbhUserID FOREIGN KEY (UserID) references Users (UserID),
                        constraint FKbhCarID FOREIGN KEY (CarID) references Car (CarID)
                    )""")
            cursor.execute("insert into BookedHistory (UserID, CarID) values (2, 1);")
            cursor.execute("insert into BookedHistory (UserID, CarID) values (1, 2);")
            cursor.execute("insert into BookedHistory (UserID, CarID) values (3, 3);")
        self.connection.commit()

    def tearDown(self):
        try:
            self.connection.close()
        except:
            pass
        finally:
            self.connection = None

    def countBookedHistory(self):
        with self.connection.cursor() as cursor:
            cursor.execute("select count(*) from BookedHistory")
            return cursor.fetchone()[0]

    def bkHistoryExists(self, bkID):
        with self.connection.cursor() as cursor:
            cursor.execute("select count(*) from BookedHistory where bkID = %s", (bkID,))
            return cursor.fetchone()[0] == 1

    def test_insertbkhistory(self):
        with DatabaseUtils(self.connection) as db:
            count = self.countBookedHistory()
            self.assertTrue(db.insertbkHistory("5, 5"))
            self.assertTrue(count + 1 == self.countBookedHistory())

    def test_get(self):
        with DatabaseUtils(self.connection) as db:
            self.assertTrue(self.countBookedHistory() == len(db.get()))

    def test_deletebkhistory(self):
        with DatabaseUtils(self.connection) as db:
            count = self.countBookedHistory()
            bkID = 1

            self.assertTrue(self.bkHistoryExists(bkID))

            db.deletebkhistory(bkID)

            self.assertFalse(self.bkHistoryExists(bkID))
            self.assertTrue(count - 1 == self.countBookedHistory())

if __name__ == "__main__":
    unittest.main()
