# ft_vaccine
sql injector based on python

With academical purpose, this project aims to perform both simple sqli: Error-based SQLi and Union-based SQLi

The goal of the sql injector are:
    - To modify the content of the databases
    - To perform different queries that are not allowed by the application

There are two types of sql injection:
    - In-band SQL injection (Simple sqli)
    - Inferential SQL injection (Blind sqli)

In-band SQL Injection:
    - Error-based technique relies on error message thrown by the database server to obtain information about the structure of the database.
    - Union-based SQL injection is a technique that leverages the UNION SQL operator to combine the results of two or more SELECT statements into a single result, which is then returned as part of the HTTP response.