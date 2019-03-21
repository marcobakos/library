"""
SELECT *
FROM orders
JOIN subscriptions
ON orders.subscription_id =
   subscriptions.subscription_id;


SELECT *
FROM orders
JOIN subscriptions
ON orders.subscription_id =
   subscriptions.subscription_id
WHERE description = "Fashion Magazine";


SELECT *
FROM orders
JOIN customers
  ON orders.customer_id = customers.customer_id;

    - The first line selects all columns from our combined table. If we only want to select certain columns, we can specify which ones we want.
    - The second line specifies the first table that we want to look in, orders
    - The third line uses JOIN to say that we want to combine information from orders with customers.
    - The fourth line tells us how to combine the two tables. We want to match orders table’s customer_id column with customers table’s customer_id column.

    When we perform a simple JOIN (often called an inner join) our result
        only includes rows that match our ON condition.



SELECT *
FROM newspaper
LEFT JOIN online
ON newspaper.id = online.id;


SELECT *
FROM newspaper
LEFT JOIN online
ON newspaper.id = online.id
WHERE online.id IS NULL;

    A left join will keep all rows from the first table, regardless of whether there is a matching row in the second table.


#################
  Cross Join

SELECT *
FROM newspaper
CROSS JOIN months;

SELECT *
FROM newspaper
CROSS JOIN months
WHERE start_month <= month and
      end_month >= month;

SELECT month, COUNT(*)
FROM newspaper
CROSS JOIN months
WHERE start_month <= month and
      end_month >= month
GROUP BY month;

    So far, we’ve focused on matching rows that have some information in common.
    Sometimes, we just want to combine all rows of one table with all rows of another table.
    For instance, if we had a table of shirts and a table of pants,
      we might want to know all the possible combinations to create different outfits.
    Our code might look like this:

    SELECT shirts.shirt_color,
        pants.pants_color
        FROM shirts
        CROSS JOIN pants;


"""

