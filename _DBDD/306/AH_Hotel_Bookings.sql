/* the following CREATE statements use mySQL syntax */

CREATE TABLE Resort (
	resortID int NOT NULL PRIMARY KEY,
	resortName varchar(20) NOT NULL,
	resortType varchar(20) NOT NULL
);


CREATE TABLE Hotel (
	hotelRef varchar(4) NOT NULL PRIMARY KEY,
	hotelName varchar(20) NOT NULL,
	resortID int NOT NULL,
	starRating int NOT NULL,
	seasonStartDate date,
	mealPlan varchar(17) NOT NULL,
	checkInTime time NOT NULL,
	pricePersonNight float(6,2) NOT NULL,
	FOREIGN KEY (resortID) REFERENCES Resort(resortID)
);


CREATE TABLE Customer (
	customerNo int AUTO_INCREMENT PRIMARY KEY,
	firstname varchar(20) NOT NULL,
	surname varchar(20) NOT NULL,
	address varchar(40) NOT NULL,
	town varchar(20) NOT NULL,
	postcode varchar(8) NOT NULL
);


CREATE TABLE Booking (
	hotelRef varchar(4) NOT NULL,
	customerNo int NOT NULL,
	startDate date NOT NULL,
	numberNights int NOT NULL,
	numberInParty int NOT NULL,
	PRIMARY KEY (customerNo, hotelRef, startDate),
	FOREIGN KEY (customerNo) REFERENCES Customer(customerNo),
	FOREIGN KEY (hotelRef) REFERENCES Hotel(hotelRef)
);

/* the following INSERT statements use mySQL syntax */

INSERT INTO Resort VALUES (168, "Ayr", "coastal");
INSERT INTO Resort VALUES (212, "Fort William", "coastal");
INSERT INTO Resort VALUES (234, "Lochwinnoch", "country");
INSERT INTO Resort VALUES (347, "Portree", "island");
INSERT INTO Resort VALUES (406, "Glasgow", "city");

INSERT INTO Hotel (hotelRef, hotelName, resortID, starRating, mealPlan, checkInTime, pricePersonNight) VALUES ("AY19", "Glee Hotel", 168, 2, "Full Board","15:00:00", 85.50);
INSERT INTO Hotel VALUES ("AY72", "Lang Scots", 168, 3, "2019-04-27", "Half Board","14:30:00", 58.99);
INSERT INTO Hotel (hotelRef, hotelName, resortID, starRating, mealPlan, checkInTime, pricePersonNight) VALUES ("FW01", "The Fort", 212, 3, "Half Board","15:30:00", 125.37);
INSERT INTO Hotel (hotelRef, hotelName, resortID, starRating, mealPlan, checkInTime, pricePersonNight) VALUES ("FW02", "Willowbank", 212, 4, "Room Only","16:30:00", 69.95);
INSERT INTO Hotel VALUES ("FW03", "Nevis Hotel", 212, 3, "2019-02-02", "Half Board","15:30:00", 101.10);
INSERT INTO Hotel VALUES ("GL13", "Kelvin Park View", 406, 4, "2019-05-18", "Bed and Breakfast","15:30:00", 123.50);
INSERT INTO Hotel (hotelRef, hotelName, resortID, starRating, mealPlan, checkInTime, pricePersonNight) VALUES ("GL31", "Finnieston Wave", 406, 3, "Room Only","16:00:00", 87.45);
INSERT INTO Hotel VALUES ("PR04", "Bay View", 347, 5, "2019-05-03", "Bed and Breakfast", "16:00:00", 179.00);

INSERT INTO Customer VALUES (111, "Pam", "Shawfair", "7 Elmtree Way", "Paisley", "PA1 9GP");
INSERT INTO Customer VALUES (290, "Jim", "Thomson", "64 Main Road", "Hamilton", "ML11 1SW");
INSERT INTO Customer VALUES (315, "Edwina", "Jones", "121 Main Street", "Greenock", "PA16 1JK");
INSERT INTO Customer VALUES (426, "Omar", "Sharif", "31 Pike Place", "Perth", "PH31 3K");
INSERT INTO Customer VALUES (428, "Max", "Lowden", "5 Admiral Way", "Gourock", "PA19 1UX");
INSERT INTO Customer VALUES (457, "Pauline", "Sheriffhall", "34a Newton Road", "Dalkeith", "EH22 1FD");

INSERT INTO Booking VALUES ("FW02", 315, "2019-04-26", 2, 3);
INSERT INTO Booking VALUES ("AY72", 426, "2019-04-30", 7, 6);
INSERT INTO Booking VALUES ("AY19", 426, "2019-05-05", 7, 2);
INSERT INTO Booking VALUES ("PR04", 290, "2019-05-05", 2, 1);
INSERT INTO Booking VALUES ("PR04", 315, "2019-06-01", 3, 2);
INSERT INTO Booking VALUES ("AY72", 111, "2019-06-01", 5, 4);
INSERT INTO Booking VALUES ("PR04", 290, "2019-07-07", 7, 5);
INSERT INTO Booking VALUES ("GL31", 290, "2019-07-12", 1, 1);
INSERT INTO Booking VALUES ("AY19", 315, "2019-07-12", 4, 4);