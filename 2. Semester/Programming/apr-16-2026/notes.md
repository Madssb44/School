# psycopg2
psycopg2 is a tool that allows you to make querys to a database from python

# how to use it?

make a get connection function 

def get_conn():
    return psycopg2.connect(
    dbname="name of the dbname"
    user="your user"
    password="your password"
    host="the host of the db"
    port="the port its listening on"
    )

    
remember to open and close everytime you need it!

conn = get_conn()      # sets the conn variable
curr = conn.cursor()   # makes a cursor
curr.execute()         # runs the sql command written within the ()
conn.commit()          # commits it to the db 
curr.close()           # closes the cursor 
conn.close()           # closes the connection 


its a good idea to make a insert command in your python progarm you use to make a variable you are sending

so a simple flow would look like this

conn = get_conn()
curr = conn.cursor()
sql = "INSERT INTO contact (email, phone) VALUES (%s, %s)"
curr.execute(sql, ("email@example.com", 12341234))
curr.commit()
curr.close()
conn.close()


placeholders are a very good idea to reduce the chance for injections
this is what a place holder looks like (%s)

you can also create a table which would look like this:

curr.execute("""CREATE TABLE IF NOT EXISTS tabelname (
id INT PRIMARY KEY
name VARCHAR(255)
age INT
);
"""))



## fetching
when fetching you are getting data from your db, therefore you dont need to have a commit when using it

There are different ways to fetch from a db, heres a example of one:

@app.route("/data")
def data():
    conn = get_conn()
    curr = conn.cursor()
    curr.execute("SELECT id, email, phone FROM contact ORDER BY id;")
    rows = curr.fetchall()
    curr.close()
    conn.close()
    return rows

this will return everything from the execute command as a tuble 

the different types are: 

|name|discription|
|:---:|:---:|
|fetchone|fetches 1 thing|
|fetchmany|fetches many things, as many as you tell it to|
|fetchall|fetches everything|

fetchone, fetchmany and fetch all 

with fetch one and a loop you then need to tell the program how many rows you have or else it will be an infinate loop!


