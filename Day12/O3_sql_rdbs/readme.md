# Day 12: SQL RDBMS — Module 01: Conditional Aggregation (`CASE WHEN`)

> **W3Schools-Aligned Syllabus & Master Architecture Guide**  
> **Course:** C-DAC PGCP-AI Data Analytics | **Module:** Relational Database Management Systems (SQL RDBMS)  
> **Topics Covered:** The SQL `CASE` Statement, Aggregate Functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`), `GROUP BY`, `HAVING`, and Advanced Conditional Aggregation

---

## 📑 Table of Contents (W3Schools Foundation to Advanced Enterprise)

### Part I: W3Schools Core SQL Building Blocks
1. [The SQL `CASE` Statement Syntax & Fundamentals](#1-the-sql-case-statement-syntax--fundamentals)
   - 1.1 What is the `CASE` Expression? (If-Then-Else logic)
   - 1.2 Searched `CASE` (`WHEN condition THEN result`)
   - 1.3 Simple `CASE` (`CASE expression WHEN value THEN result`)
   - 1.4 The `ELSE` Clause & Default `NULL` Behavior
   - 1.5 Short-Circuit Execution Order (Top-to-Bottom)
2. [SQL Aggregate Functions & The NULL Handling Rule](#2-sql-aggregate-functions--the-null-handling-rule)
   - 2.1 The `COUNT()` Function: `COUNT(*)`, `COUNT(column)`, `COUNT(DISTINCT column)`
   - 2.2 The `SUM()` Function & Null Ignoring
   - 2.3 The `AVG()` Function: Calculating Means and the Denominator Shrink
   - 2.4 The `MIN()` & `MAX()` Functions
   - 2.5 Null-Handling Scalar Functions (`COALESCE()`, `IFNULL()`)
3. [The `GROUP BY` Statement & Aggregation Workflows](#3-the-group-by-statement--aggregation-workflows)
   - 3.1 Grouping Rows by Categorical Columns
   - 3.2 SQL Clause Execution Order (`FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT`)
4. [The `HAVING` Clause](#4-the-having-clause)
   - 4.1 Why `HAVING` was added (Filtering aggregates where `WHERE` cannot be used)
   - 4.2 Combining `WHERE`, `GROUP BY`, and `HAVING`

---

### Part II: Intermediate & Advanced Conditional Aggregation
5. [The Power Pattern: Combining `CASE WHEN` with Aggregate Functions](#5-the-power-pattern-combining-case-when-with-aggregate-functions)
   - 5.1 Why Conditional Aggregation? Single-Scan ($\mathcal{O}(N)$) vs Multiple Queries / Joins
   - 5.2 Conditional Counting (`COUNT(CASE WHEN ... THEN 1 END)`)
   - 5.3 The Deadliest SQL Trap: Why `COUNT(CASE WHEN ... THEN 1 ELSE 0 END)` Counts Everything!
   - 5.4 Conditional Summation (`SUM(CASE WHEN ... THEN amount ELSE 0 END)`)
   - 5.5 Conditional Averages (`AVG(CASE WHEN ... THEN score END)`)
6. [Dynamic Cross-Tabulation & Matrix Pivoting (Rows to Columns)](#6-dynamic-cross-tabulation--matrix-pivoting-rows-to-columns)
   - 6.1 Creating Pivot Tables using `SUM(CASE WHEN ...)` / `MAX(CASE WHEN ...)`
   - 6.2 Cross-Database ANSI SQL Portability (Eliminating Vendor `PIVOT`)
7. [Multi-Condition Grouping & Custom Binning](#7-multi-condition-grouping--custom-binning)
   - 7.1 Using `CASE` inside `GROUP BY` for On-the-Fly Category Bucketing
   - 7.2 Complex Boolean Logic (`AND`, `OR`, `BETWEEN`, `IN`, `LIKE`)
8. [Filtering Aggregated Groups with Conditional `HAVING`](#8-filtering-aggregated-groups-with-conditional-having)
   - 8.1 Filtering Cohorts by Threshold Rates (e.g. Return Rate > 20%)
9. [Modern ANSI Standard: `FILTER (WHERE ...)` vs `CASE WHEN`](#9-modern-ansi-standard-filter-where--vs-case-when)
   - 9.1 The SQL:2003 `FILTER` Clause (PostgreSQL, SQLite 3.30+, DuckDB)
   - 9.2 Syntactic Comparison & Performance Equivalence
10. [The SQL-to-Pandas Rosetta Stone](#10-the-sql-to-pandas-rosetta-stone)
    - 10.1 `CASE WHEN` ➔ `np.where()` / `pd.cut()`
    - 10.2 Conditional Aggregation ➔ `df.groupby().agg()` / Named Aggregation
    - 10.3 SQL Pivot ➔ `pd.pivot_table()` / `pd.crosstab()`
11. [Hands-On Enterprise Case Studies (SQLite Lab)](#11-hands-on-enterprise-case-studies-sqlite-lab)
    - 11.1 E-Commerce Transaction Profit & Loss (Gross vs Net Revenue)
    - 11.2 Banking Credit Risk & Non-Performing Loan (NPL) Ratios
    - 11.3 SaaS Subscription MRR Movement Waterfall (New, Expansion, Churn)
12. [W3Schools Exercises, Viva Traps & Technical Interview Questions](#12-w3schools-exercises-viva-traps--technical-interview-questions)

---

## 1. The SQL `CASE` Statement Syntax & Fundamentals

According to standard W3Schools documentation, the SQL `CASE` statement goes through conditions and returns a value when the first condition is met (like an `if-then-else` statement). Once a condition is true, it stops reading and returns the result. If no conditions are true, it returns the value in the `ELSE` clause (or `NULL` if no `ELSE` is present).

### 1.1 Searched `CASE` Syntax
Used when evaluating complex conditions (`<`, `>`, `BETWEEN`, `AND`, `OR`):
```sql
SELECT OrderID, Quantity,
    CASE 
        WHEN Quantity > 30 THEN 'High Volume'
        WHEN Quantity = 30 THEN 'Target Volume'
        ELSE 'Under Target'
    END AS QuantityStatus
FROM OrderDetails;
```

### 1.2 Simple `CASE` Syntax
Used when comparing a single expression against fixed literal values:
```sql
SELECT CustomerName, Country,
    CASE Country
        WHEN 'USA' THEN 'North America'
        WHEN 'Canada' THEN 'North America'
        WHEN 'Germany' THEN 'Europe'
        ELSE 'Rest of World'
    END AS ContinentRegion
FROM Customers;
```

### 1.3 `CASE` in `ORDER BY`
W3Schools highlights using `CASE` in `ORDER BY` for priority sorting:
```sql
SELECT CustomerName, City, Country
FROM Customers
ORDER BY 
    CASE 
        WHEN Country = 'Germany' THEN 1
        WHEN Country = 'USA' THEN 2
        ELSE 3
    END, 
    CustomerName;
```

---

## 2. SQL Aggregate Functions & The NULL Handling Rule

W3Schools defines aggregate functions as functions that perform calculations on a set of values and return a single summary value.

| Function | W3Schools Definition | Treatment of `NULL` Values |
| :--- | :--- | :--- |
| `COUNT(*)` | Returns the total count of rows in the table. | **Includes** rows with `NULL`s. |
| `COUNT(column)` | Returns the number of values in the column. | **Ignores** `NULL`s. |
| `COUNT(DISTINCT col)` | Returns the number of unique non-null values. | **Ignores** `NULL`s. |
| `SUM(column)` | Calculates the sum of a numeric column. | **Ignores** `NULL`s. |
| `AVG(column)` | Calculates the average value of a numeric column. | **Ignores** `NULL`s (denominator is count of non-nulls!). |
| `MIN()` / `MAX()` | Returns minimum / maximum value. | **Ignores** `NULL`s. |

### The `COALESCE()` / `IFNULL()` Helper
If `NULL`s must be converted into zeroes before aggregation:
```sql
SELECT AVG(COALESCE(Price, 0)) FROM Products;
```

---

## 3. The `GROUP BY` Statement & Aggregation Workflows

W3Schools notes that `GROUP BY` groups rows that have the same values into summary rows (e.g. "find the number of customers in each country").
```sql
SELECT Country, COUNT(CustomerID) AS NumberOfCustomers
FROM Customers
GROUP BY Country
ORDER BY NumberOfCustomers DESC;
```

---

## 4. The `HAVING` Clause

W3Schools explains: *The `HAVING` clause was added to SQL because the `WHERE` keyword cannot be used with aggregate functions.*

```sql
SELECT Country, COUNT(CustomerID) AS CustomerCount
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5;
```

---

## 5. The Power Pattern: Combining `CASE WHEN` with Aggregate Functions

When `CASE WHEN` is nested inside `COUNT()`, `SUM()`, or `AVG()`, we perform **Conditional Aggregation**.

### 5.1 Conditional Counting
Count specific categories without writing multiple queries:
```sql
SELECT 
    Country,
    COUNT(CASE WHEN City = 'London' THEN 1 END) AS LondonCustomers,
    COUNT(CASE WHEN City = 'Berlin' THEN 1 END) AS BerlinCustomers
FROM Customers
GROUP BY Country;
```

### 5.2 The Deadliest SQL Trap: Why `COUNT(... 1 ELSE 0 END)` Fails
```sql
-- ❌ BUG: 0 is non-null, so COUNT tallies EVERY single row!
COUNT(CASE WHEN status = 'Refunded' THEN 1 ELSE 0 END)

-- ✅ CORRECT: Omit ELSE (yields NULL)
COUNT(CASE WHEN status = 'Refunded' THEN 1 END)

-- ✅ OR USE SUM:
SUM(CASE WHEN status = 'Refunded' THEN 1 ELSE 0 END)
```

### 5.3 Conditional Summation (P&L Financials)
```sql
SELECT 
    department,
    SUM(CASE WHEN status = 'Completed' THEN amount ELSE 0 END) AS gross_revenue,
    SUM(CASE WHEN status = 'Refunded'  THEN amount ELSE 0 END) AS refund_losses,
    SUM(CASE WHEN status = 'Completed' THEN amount ELSE 0 END) -
    SUM(CASE WHEN status = 'Refunded'  THEN amount ELSE 0 END) AS net_revenue
FROM transactions
GROUP BY department;
```

---

## 6. Dynamic Cross-Tabulation & Matrix Pivoting

Pivot categorical rows into columns across all SQL engines:
```sql
SELECT 
    department,
    SUM(CASE WHEN payment_method = 'Credit Card' THEN amount ELSE 0 END) AS credit_card_sales,
    SUM(CASE WHEN payment_method = 'Debit Card'  THEN amount ELSE 0 END) AS debit_card_sales,
    SUM(CASE WHEN payment_method = 'PayPal'      THEN amount ELSE 0 END) AS paypal_sales
FROM transactions
WHERE status = 'Completed'
GROUP BY department;
```

---

## 7. Using `CASE` inside `GROUP BY` for On-the-Fly Bucketing

W3Schools highlights that you can use `CASE` inside `GROUP BY` to dynamically categorize and group records:
```sql
SELECT 
    CASE 
        WHEN Price > 100 THEN 'Expensive'
        WHEN Price BETWEEN 20 AND 100 THEN 'Moderate'
        ELSE 'Budget'
    END AS PriceCategory,
    COUNT(*) AS ProductCount,
    AVG(Price) AS AveragePrice
FROM Products
GROUP BY 
    CASE 
        WHEN Price > 100 THEN 'Expensive'
        WHEN Price BETWEEN 20 AND 100 THEN 'Moderate'
        ELSE 'Budget'
    END;
```

---

## 8. Filtering Aggregated Groups with Conditional `HAVING`
Filter groups based on conditional metrics:
```sql
SELECT department,
       COUNT(*) AS total_orders,
       SUM(CASE WHEN status = 'Refunded' THEN 1 ELSE 0 END) AS refunds
FROM transactions
GROUP BY department
HAVING 100.0 * SUM(CASE WHEN status = 'Refunded' THEN 1 ELSE 0 END) / COUNT(*) > 20.0;
```

---

## 9. Modern ANSI Standard: `FILTER (WHERE ...)` vs `CASE WHEN`
In PostgreSQL, SQLite 3.30+, DuckDB:
```sql
SELECT 
    department,
    COUNT(*) AS total_orders,
    COUNT(*) FILTER (WHERE status = 'Completed') AS completed_orders,
    SUM(amount) FILTER (WHERE status = 'Completed') AS gross_sales
FROM transactions
GROUP BY department;
```

---

## 10. The SQL-to-Pandas Rosetta Stone

| Data Analytics Task | SQL Expression (W3Schools Pattern) | Python Pandas Equivalent |
| :--- | :--- | :--- |
| **Row Flagging** | `CASE WHEN price > 100 THEN 'High' ELSE 'Low' END` | `np.where(df['price'] > 100, 'High', 'Low')` |
| **Conditional Count** | `COUNT(CASE WHEN st='Active' THEN 1 END)` | `(df['st'] == 'Active').sum()` |
| **Conditional Sum** | `SUM(CASE WHEN st='A' THEN amt ELSE 0 END)` | `df.loc[df['st'] == 'A', 'amt'].sum()` |
| **Dynamic Pivot** | `SUM(CASE WHEN type='Card' THEN amt ELSE 0 END)` | `df.pivot_table(index='dept', columns='type', values='amt', aggfunc='sum')` |
| **On-the-fly Grouping** | `GROUP BY CASE WHEN ...` | `df.groupby(pd.cut(df['price'], bins=[0,20,100,np.inf]))` |

---

## 11. Hands-On Enterprise Case Studies (SQLite Lab)

The accompanying notebook [Day12/O3_sql_rdbs/O1_aggregation_condition.ipynb](file:///d:/PGCPAI/Data_Analytics/CDAC-Data-Analytics/Day12/O3_sql_rdbs/O1_aggregation_condition.ipynb) contains three interactive labs:
1. **E-Commerce Order P&L:** Net revenue, cancelled demand, and customer rating analysis.
2. **Commercial Banking Loan Risk:** Prime vs Subprime exposure and Non-Performing Loan (NPL) ratios.
3. **SaaS Subscription MRR Waterfall:** Net MRR changes across New, Expansion, Contraction, and Churn events.

---

## 12. Critical Viva Traps & Technical Interview Questions

1. **Why does `COUNT(CASE WHEN x > 10 THEN 0 END)` count every matching row?**  
   *Answer:* `COUNT()` checks for **non-null** values. Since `0` is a valid non-null literal, SQL counts it! To avoid counting, omit `ELSE` so unmatched rows evaluate to `NULL`.
2. **Why is conditional aggregation faster than multiple subqueries or joins?**  
   *Answer:* It executes in a **single table scan ($\mathcal{O}(N)$)** in CPU cache, avoiding intermediate Cartesian tables and disk I/O.
3. **What is the difference between `WHERE` and `HAVING` with `CASE WHEN`?**  
   *Answer:* `WHERE` filters raw individual rows *before* grouping occurs. `HAVING` filters aggregated group metrics *after* `GROUP BY` reduction.
