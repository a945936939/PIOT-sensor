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
