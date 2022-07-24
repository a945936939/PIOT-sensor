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
