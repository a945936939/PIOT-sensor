/*Car Table*/
CREATE TABLE Car(
CarID INT AUTO_INCREMENT NOT NULL, PRIMARY KEY(CarID),
    Make VARCHAR(100) NOT NULL,
    BodyType VARCHAR(100) NOT NULL,
    Colour VARCHAR(100) NOT NULL,
    Seats INT NOT NULL,
    Location VARCHAR(100) NOT NULL,
    CostperHr DECIMAL(15,2) NOT NULL,
    ShareDate DATE NOT NULL 
);

INSERT INTO Car (Make, BodyType, Colour, Seats, Location, CostperHr, ShareDate)
VALUES ('test-make', 'sedan', 'black', 4, 'Melbourne', 12300, '2020-05-12');



/*Staff Table*/
CREATE TABLE Staff(
UserID INT AUTO_INCREMENT NOT NULL, PRIMARY KEY(UserID),
    Username VARCHAR(100) NOT NULL,
    Password VARCHAR(100) NOT NULL,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    UserType SET('Manager', 'Engineer', 'SysAdmin')
);

INSERT INTO Staff (Username, Password, FirstName, LastName, Email, UserType)
VALUES ('JERRY1', '123', 'Jeremy', 'Chung', 's1234@student.email', 'Engineer');



/*Users Table*/
CREATE TABLE Users(
UserID INT AUTO_INCREMENT NOT NULL, PRIMARY KEY(UserID),
    Username VARCHAR(100) NOT NULL,
    Password VARCHAR(100) NOT NULL,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL
);

INSERT INTO Users (Username, Password, FirstName, LastName, Email)
VALUES ('JERRY1', '123', 'Jeremy', 'Chung', 's1234@student.email');

INSERT INTO Users (Username, Password, FirstName, LastName, Email)
VALUES ('u1', '123', 'test', 'user', 's122@student.email');


/*Car Borrowed*/
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
);

/* U1 has Borrowed Car: 1 on A2 Submission Date*/
INSERT INTO CarBooked (UserID, CarID, Status, BorrowedDate, ReturnedDate, Locked)
values ('2', '1', 'Booked', '2020-05-24', '2020-05-24', 'Unlocked');

CREATE TABLE BookedHistory(
    BHistoryID INT AUTO_INCREMENT NOT NULL, Primary KEY(BHistoryID),
    UserID INT NOT NULL,
    CarID INT NOT NULL,
    constraint FKbhUserID FOREIGN KEY (UserID) references Users (UserID),
    constraint FKbhCarID FOREIGN KEY (CarID) references Car (CarID)
);

INSERT INTO BookedHistory (UserID, CarID)
values (2, 1);
/* REMEMBER TO UPDATE ALL TABLES */
UNIQUE (UserID)


/*Alters*/

ALTER TABLE CarBooked
ADD Locked enum('Locked', 'Unlocked');
