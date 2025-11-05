-- database: c:\Users\thefa\OneDrive\Documents\VSCode\SQA_AH_Computing_Science\_DBDD\301\AH_Dishes.db
-- A.
SELECT course, MAX(price) AS 'most expensive item'
FROM Dishes
WHERE portions >= 2
GROUP BY course;

-- B.
-- database: c:\Users\thefa\OneDrive\Documents\VSCode\SQA_AH_Computing_Science\_DBDD\301\AH_Dishes.db

SELECT Course, COUNT(*) AS 'Number of courses'
FROM Dishes
GROUP BY Course;

-- C.
-- database: ./AH_Dishes.db

SELECT dishName, price
FROM Dishes
WHERE course = "Starter"
ORDER BY price DESC;

-- D.
DELETE FROM Dishes
WHERE dishName = "Panacotta";

-- 3.
SELECT Title FROM Movies
WHERE Rating = (SELECT MAX(Rating) FROM Movies);

-- 4.
SELECT Name, Postcode
FROM Resort
WHERE Resort_ID = (
    SELECT Resort_ID
    FROM Instructor
    GROUP BY Resort_ID
    ORDER BY COUNT(*) DESC
    LIMIT 1
);
-- I've taken this question out - it's way beyond Higher level.

-- 4a. (NEW)
SELECT Firstname, Surname
FROM Instructor
WHERE Resort_ID = (
    SELECT Resort_ID
    FROM Resort
    WHERE Name = 'Glenshee'
);

-- 4b. (NEW)
SELECT Firstname, Surname
FROM Instructor
WHERE Resort_ID = (
    SELECT Resort_ID
    FROM Resort
    WHERE Lifts = (
        SELECT MAX(Lifts)
        FROM Resort
    )
);