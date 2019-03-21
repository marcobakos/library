# Examples of SELECT
"""
SELECT * FROM movies;

SELECT name, genre, year FROM movies;


SELECT imdb_rating AS 'IMDB' FROM movies;

    AS is a keyword in SQL that allows you to rename a column or table using an alias.

SELECT DISTINCT year FROM movies;

    DISTINCT is used to return unique values in the output.
    It filters out all duplicate values in the specified column(s).

SELECT * FROM movies WHERE year > 2014 ;

    Comparison operators used with the WHERE clause are:

    = equal to
    != not equal to
    > greater than
    < less than
    >= greater than or equal to
    <= less than or equal to


SELECT * FROM movies WHERE name LIKE 'Se_en';


    LIKE is a special operator used with the WHERE clause to search for a specific pattern in a column.

    name LIKE 'Se_en' is a condition evaluating the name column for a specific pattern.

    Se_en represents a pattern with a wildcard character.

    The _ means you can substitute any individual character here without breaking the pattern.
    The names Seven and Se7en both match this pattern.


SELECT * FROM movies WHERE name LIKE 'The %';

    % is a wildcard character that matches zero or more missing letters in the pattern. For example:

    A% matches all movies with names that begin with letter ‘A’
    %a matches all movies that end with ‘a’

    We can also use % both before and after a pattern


SELECT name FROM movies WHERE imdb_rating IS NULL;

    It is not possible to test for NULL values with comparison operators, such as = and !=.

    Instead, we will have to use these operators:

    - IS NULL
    - IS NOT NULL


SELECT * FROM movies WHERE year BETWEEN 1970 and 1979;

    In this statement, the BETWEEN operator is being used to filter the result set to only include
    movies with years between 1990 up to, and including 1999.

SELECT * FROM movies WHERE year < 1985 AND genre = 'horror' ;

    With AND, both conditions must be true for the row to be included in the result.


SELECT * FROM movies WHERE genre = 'romance' OR genre = 'comedy';

    With OR, if any of the conditions are true, then the row is added to the result.


SELECT name, year, imdb_rating FROM movies
     ORDER BY imdb_rating DESC;


    ORDER BY is a clause that indicates you want to sort the result set by a particular column.
    name is the specified column.

    - DESC is a keyword used in ORDER BY to sort the results in descending order (high to low or Z-A).

    - ASC is a keyword used in ORDER BY to sort the results in ascending order (low to high or A-Z).


SELECT * FROM movies
ORDER BY imdb_rating DESC
LIMIT 3;

    LIMIT is a clause that lets you specify the maximum number of rows the result set will have.


SELECT name,
 CASE
  WHEN imdb_rating > 8 THEN 'Fantastic'
  WHEN imdb_rating > 6 THEN 'Poorly Received'
  ELSE 'Avoid at All Costs'
 END
FROM movies;

    A CASE statement allows us to create different outputs (usually in the SELECT statement).
    It is SQL’s way of handling if-then logic.

    Each WHEN tests a condition and the following THEN gives us the string if the condition is true.
    The ELSE gives us the string if all the above conditions are false.
    The CASE statement must end with END.

###########################################
Let’s summarize:

    SELECT is the clause we use every time we want to query information from a database.
    AS renames a column or table.
    DISTINCT return unique values.
    WHERE is a popular command that lets you filter the results of the query based on conditions that you specify.
    LIKE and BETWEEN are special operators.
    AND and OR combines multiple conditions.
    ORDER BY sorts the result.
    LIMIT specifies the maximum number of rows that the query will return.
    CASE creates different outputs.
###########################################

Aggregate Functions:

Here is a quick preview of some important aggregates that we will cover in the next five exercises:

    - COUNT(): count the number of rows
    - SUM(): the sum of the values in a column
    - MAX()/MIN(): the largest/smallest value
    - AVG(): the average of the values in a column
    - ROUND(): round the values in the column


SELECT COUNT(*) FROM fake_apps WHERE price = 0;

    Here, we want to count every row, so we pass * as an argument inside the parenthesis.

SELECT SUM(downloads) FROM fake_apps;

    SUM() is a function that takes the name of a column as an argument and returns
    the sum of all the values in that column.

SELECT MAX(price) FROM fake_apps;

    The MAX() and MIN() functions return the highest and lowest values in a column, respectively.
    - MAX() takes the name of a column as an argument and returns the largest value in that column.
      Here, we returned the largest value in the downloads column.
    - MIN() works the same way but it does the exact opposite; it returns the smallest value.

SELECT AVG(price) FROM fake_apps;

    The AVG() function works by taking a column name as an argument and returns the average value for that column.


SELECT ROUND(AVG(price),2) FROM fake_apps;

    ROUND() function takes two arguments inside the parenthesis:

    - a column name
    - an integer (may be zero)

    It rounds the values in the column to the number of decimal places specified by the integer.


SELECT year, AVG(imdb_rating)
 FROM movies
 GROUP BY year
 ORDER BY year;

    GROUP BY is a clause in SQL that is used with aggregate functions.
    It is used in collaboration with the SELECT statement to arrange identical data into groups.
    The GROUP BY statement comes after any WHERE statements, but before ORDER BY or LIMIT.

SELECT category, price, AVG(downloads)
  FROM fake_apps
  GROUP BY 1, 2;

    SQL lets us use column reference(s) in our GROUP BY that will make our lives easier.

    - 1 is the first column selected
    - 2 is the second column selected
    - 3 is the third column selected


SELECT price, ROUND(AVG(downloads)), COUNT(*)
  FROM fake_apps
  GROUP BY price
  HAVING COUNT(*) > 10;

    - When we want to limit the results of a query based on values of the individual rows, use WHERE.
    - When we want to limit the results of a query based on an aggregate property, use HAVING.
    HAVING statement always comes after GROUP BY, but before ORDER BY and LIMIT.


########## Review

You just learned how to use aggregate functions to perform calculations on your data. What can we generalize so far?

    - COUNT(): count the number of rows
    - SUM(): the sum of the values in a column
    - MAX()/MIN(): the largest/smallest value
    - AVG(): the average of the values in a column
    - ROUND(): round the values in the column

Aggregate functions combine multiple rows together to form a single value of more meaningful information.

    - GROUP BY is a clause used with aggregate functions to combine data from one or more columns.
    - HAVING limit the results of a query based on an aggregate property.














"""
