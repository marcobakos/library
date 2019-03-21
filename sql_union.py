"""
SELECT *
FROM table1
UNION
SELECT *
FROM table2;

    Sometimes we just want to stack one dataset on top of the other.
    Well, the UNION operator allows us to do that.

    SQL has strict rules for appending data:

    - Tables must have the same number of columns.
    - The columns must have the same data types in the same order as the first table.


"""

