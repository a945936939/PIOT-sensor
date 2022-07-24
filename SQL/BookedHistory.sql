CREATE TABLE BookedHistory(
    BHistoryID INT AUTO_INCREMENT NOT NULL, Primary KEY(BHistoryID),
    UserID INT NOT NULL,
    CarID INT NOT NULL,
    constraint FKbhUserID FOREIGN KEY (UserID) references Users (UserID),
    constraint FKbhCarID FOREIGN KEY (CarID) references Car (CarID)
);

INSERT INTO BookedHistory (UserID, CarID)
values (2, 1);