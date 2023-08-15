#Question 1:- What is a database? Differentiate between SQL and NoSQl database.

"""Answer 1:-   A database is an organized collection of data, so that it can be easily
acessed and managed. You can organize data into tables, rows, columns, and index it to
make it easier to find relevant information. The main purpose of the database is to operate
a large amount of information by storing, retrieving, and managing data. There are many
database available like MySQL, Sybase, Oracle, MongoDB, Informix, PostgreSql, SQL Server etc.

difference between sql and Nosql 
1. Database are ctegorized as Reltional database management system(RDBMS). where as  Nosql 
   database are categorized as Non- reltional or distriuted database system.
2. Sql database have fixed  or static or predefined schema. Nosql database have dynamic schema.
3. Sql database display data in form of tables so it is known as table-based database.
   Nosql  database display data as collection of key-value pair, documents, graph database 
   or wide-columns stores.
4. Mysql, Oracle, Sqlite PostreSql and Ms-Sql etc. are the example of Sql database. MongoDB,
   Bigtable, Redis, RavenDB, Cassandra, Hbase, Neo4j, CouchDB etc. are example of nosql database"""

#Question 2:- What is DDL? Explain why CREATE, DROP, ALTER and TRUNCATE are used with an example.

"""Answer 2:- A data definition language (DDL) is a computer language used to create and 
modify the structure of database objects in a database. These database objects include
viws, schemas, table, indexes etc.

1. CREATE : This command is used to create a new table in Sql. The user has to give 
   information like table name, column names, and their datatypes.
Synatx --
       CREATE TABLE table_name(column_1 datatype,column_2 datatype, column_3 datatype,...);
       
2. DROP : This command is used to remove an existing table along with its structure from 
   the database.
Syntax --
    DROP TABLE table_name;
    
3. ALTER : This command is used to add, delete or change columns in the existing tables. 
   The user needs to know the existing tables name and can do add, delete or modify tasks
   easily.
Syntax --
    ALTER TABLE table_name
    ADD column_name datatypte;
    
4.TRUNCATE : This command is used to remove from the table, but the structure of the table
  still exists.
Syntax 
      TRUNCATE TABLE table_name;"""

#Question 3:- What is DML? Explain INSERT, UPDATE, and DELETE with an example.

"""Answer 3:- The SQL commands that deal with the manipulation of data present in the 
database belong to DML or Data Manipulation Language and this includes most of the SQL
 statements. It is the component of the SQL statement that controls access to data and 
 to the database. 
 
 1. INSERT: It is used to insert data into a table.
synrax:
    INSERT INTO TABLE(c1,c2,c3,....) VALUES(value1,value2,value3,....)
 2. UPDATE: It is used to update existing data within a table.
 syntax:
      UPDATE table_name SET [column_name1= value1,...column_nameN = valueN]  
 3. DELETE: It is used to delete records from a database table.
  syntax:
      DELETE FROM table_name [WHERE condition];   """

 #Question 4:- What is DQL? Explain SELECT with an example.

"""Answer 4:-DQL statements are used for performing queries on the data
  within schema objects. The purpose of the DQL Command is to get some
   schema relation based on the query passed to it. We can define DQL 
   as follows it is a component of SQL statement that allows getting data 
   from the database and imposing order upon it. It includes the SELECT statement.
   This command allows getting the data out of the database to perform operations
   with it. When a SELECT is fired against a table or tables the result is
   compiled into a further temporary table, which is displayed or perhaps received 
   by the program i.e. a front-end. 
   
   1. SELECT: It is used to retrieve data from the database."""

#Question 5:-  Explain Primary Key and Foreign Key.

"""Answer 5:- Primary key : A Primary Key is the minimal set of attributes of a table
that has the task to uniquely identify the rows, or we can say the tuples of the given
particular table.A primary key of a relation is one of the possible candidate keys
which the database designer thinks it's primary. It may be selected for 
convenience, performance and many other reasons. 

Foreign key: The FOREIGN KEY constraint is used to prevent actions that would 
destroy links between tables.
A FOREIGN KEY is a field (or collection of fields) in one table, that refers 
to the PRIMARY KEY in another table.
The table with the foreign key is called the child table, and the table 
with the primary key is called the referenced or parent table."""

#Question :- 6 Write a python code to connect MySQL to python. Explain the cursor() and execute() method.
#Answer 6:-

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE test")
mydb.close()
""" cursor() : Cursor is a Temporary Memory or Temporary Work Station. It is Allocated 
by Database Server at the Time of Performing DML(Data Manipulation Language) operations 
on the Table by the User. Cursors are used to store Database Tables.
 
 execute() : The Execute method executes a specified query, SQL statement, stored procedure, 
 or provider-specific text.
 """

 #Question 7:-Give the order of execution of SQL clauses in an SQL query.
"""Answer 7:-1. FROM: The FROM clause specifies the table or tables from which the data will be retrieved.
2.JOIN: The JOIN clause is used to combine data from two or more tables based on a common column.
3. WHERE: The WHERE clause is used to filter the data based on a specific condition.
4. GROUP BY: The GROUP BY clause is used to group the data by one or more columns and aggregate the results.
5. HAVING: The HAVING clause is used to filter the groups based on a specific condition.
6. SELECT: The SELECT clause is used to specify the columns to be retrieved from the tables.
7. DISTINCT: The DISTINCT keyword is used to eliminate duplicate rows from the results.
8. ORDER BY: The ORDER BY clause is used to sort the data based on one or more columns.
9. LIMIT: The LIMIT clause is used to limit the number of rows returned by the query."""