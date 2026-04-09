# Data bases
today we will be learning about databases and SQL, we will be working with postgres and pqadmin

## SQL 

### what is it
sql is a query language commonly used to talk with databases 
### why 
its a easy way to structure how you get data form a database 
### commands 
Some of the most common are:

|command|desc|
|:---:|:---:|
|CREATE|Used when creating something|
|TABLE|Refers to a table of data|
|INSERT|Used to insert into something|
|TO|Points to what comes after|
|SELECT|Indicates what to pick|
|FROM|Points to where something is form|
|WHERE|Used with select to indicate something is something|
|AS|Saves the result as something else|
|AND|Adds something more|
|OR|Adds another condition|
|UNION|Combins the results|
|ROW|Refers to an entire row|
|COLOUMN|Refers to an entire coloumn|
|DPOP|Removes something|
|IF|A standard if statement|
|CASCADE|Used with drop to remove things that depends on it|

and theres lots more, syntax can also depend on the type of sql you are using with these being from postgres

## Keys
there 2 main types, Primary key and Foreign key

### Primary key 
A primary key is what other tables use to refer to it if they need some data form you, and its common practice that you only have one

### Foreign key 
A foreign key is refering to a key not assosiated with the table you are currently working in 

### Query
a query is a set of parameters that we use when reaching out to our database to get something from it an example could be:

SELECT * FROM users WHERE userrole = 'admin'

This query would take everything indicated by the * form the table users where the userrole coloumn value is admin and return
all the data assosiated with the entries that the query applis to so in this case all the users that are have the admin role

### Where to use it
Theres many ways to use a database but the one we will be using is with python which like many other programming languages
methods built in to the language to work with a database



