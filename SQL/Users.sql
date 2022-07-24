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





/*
Car: [CarID (autoincrement)], [Make], [Colour], [Seats], [Location], [Cost/hr]
User: [UserID (autoincrement)], [Name], [User], [Password], [Account Type], [Email] [Duration]
*/


