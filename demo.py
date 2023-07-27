                                     # ASSIGNMENT: PYTHON+SQL




 #  Q1. What is a database? Differentiate between SQL and NoSQL databases?

 
 """Database is basically the name of structered or unstructred data, which is stored in computer system.
 and if we talk about diffrence between sql and nosql then firstly we need to clear the meaning of both.
 
 SQL= Sturctured query Language
 
 we are using the Sql Database for storing the structred data like excel, there are the columns and rows
 for sake of convinence ...MySql, MSSQL and oracle..etc 
 
 In NoSql, we can store the data, which is unstructred. As we need to store the images, videos and some 
 formats of data then we use NoSql. MongoDB,Influx...etc..and cassands are the example of such type of 
 database""" 

                                 
                                  



#Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example

""" 

DDL= Data Definaton Language

As it is clear by the fullform, DDL is a package of commands in sql. These commands ie...CREAT,DROP,
ALTER and TRUNCATE explain below:

CREAT
This command is used to create a new table in SQL.

DROP
This command is used to remove an existing table along with its structure from the Database.

ALTER
This command is used to add, delete or change columns in the existing table.

TRUNCATE
This command is used to remove all rows from the table, but the structure of the table still exists.

"""





#Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example?

"""
DML=Data Manipulation Language
DML is also a package of commands which are used in manipulation data or information. Such type of 
commands ...ie..INSERT, UPDATE, and DELETE explained below:

INSERT
This command is used to enter the information of the row of a existing table.

UPDATE
This command is used to modify the data which is allready exist in a existing table.

DELETE
This command is used to erase some or all of the previous table records.
"""






#Q4. What is DQL? Explain SELECT with an example?
"""
DQL= Data Query Language

In DQL, the commands are giving the instruction to the system for opreate the data. The SELECT statement
is used in the DQL command. With the SELECT command, we can get the data from the database and manipulate 
it as we want.
"""





# Q5. Explain Primary Key and Foreign Key?
"""

Primary key
-it is used when data is unique in the table.
-Two or more rows can't have same primary key.
-it cannot accept Null values

Foreign Key
-it is used to combine(only characterstic) the table.
-There can same key for two or more table
-It can accept null values also
"""




#Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method?

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
#here cursor is used for access the mydb connector so that we can access the SQL properties
#  by the python
mycursor.execute("SHOW DATABASES")
# and execute is used for calling the mycursor for running






#Q7. Give the order of execution of SQL clauses in an SQL query
""" 

FROM
ON
JOIN
WHERE
GROUP BY
WITH CUBE or WITH ROLLUP
HAVING
SELECT
DISTINCT
ORDER BY
TOP
"""