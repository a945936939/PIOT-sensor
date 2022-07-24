/*Car Table*/

CREATE TABLE Car(
CarID INT AUTO_INCREMENT NOT NULL, PRIMARY KEY(CarID),
    Make VARCHAR(100) NOT NULL,
    BodyType VARCHAR(100) NOT NULL,
    Colour VARCHAR(100) NOT NULL,
    Seats INT NOT NULL,
    Location VARCHAR(100) NOT NULL,
    CostperHr DECIMAL(15,2) NOT NULL,
    ShareDate DATE NOT NULL /*Subject to change with Google Calendar Implementation*/
);

INSERT INTO Car (Make, BodyType, Colour, Seats, Location, CostperHr, ShareDate)
VALUES ('test-make', 'sedan', 'black', 4, 'Melbourne', 12300, '2020-05-12');
