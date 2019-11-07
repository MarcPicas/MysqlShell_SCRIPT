#
# MySQL 8 Shell
#
# This example shows a simple X DevAPI script to work with relational data
#
from mysqlsh import mysqlx # needed in case you run the code outside of the shell
# SQL CREATE TABLE statement
CREATE_TBL = """
CREATE TABLE `supermercat`.`caixer` (
  `ID_CAIXER' INT not null auto_increment,
  `DNI_CLIENT` VARCHAR(9) NOT NULL,
  `NOM_CAIXER` VARCHAR(15) DEFAULT NULL,
  `COGNOM_CAIXER` VARCHAR(15) NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `NUM_TELF` INT DEFAULT NULL,
  PRIMARY KEY `ID_CAIXER` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
"""
# column list, user data structure
COLUMNS = ['Id_Caixer','DNI_Client','Nom_Caixer', 'Cognom_Caixer', 'Num_Telef']
user_info = {
  'host': 'localhost',
  'port': 33060,
  'user': 'root',
  'password': 'root',
}
print("Listing 4-6 Example - Python X DevAPI Demo with Relational Data.")
# Get a session (connection)
my_session = mysqlx.get_session(user_info)
# Precautionary drop schema
my_session.drop_schema('supermercat')
# Create the database (schema)
my_db = my_session.create_schema('supermercat')
# Execute the SQL statement to create the table
sql_res = my_session.sql(CREATE_TBL).execute()
# Get the table object
my_tbl = my_db.get_table('caixer')
# Insert some rows (data)
my_tbl.insert(COLUMNS).values(123,'12366677Z','Roser','Avellan',934524565).execute()
my_tbl.insert(COLUMNS).values(124,'14366677W','Fran','Catala',932457825).execute()
my_tbl.insert(COLUMNS).values(125,'11363547X','Pau','Barber',938742595).execute()
my_tbl.insert(COLUMNS).values(126,'12366677E','Lluc','Avellan',932541525).execute()
# Execute a simple select (SELECT ∗ FROM)
print("\nShowing results after inserting all rows.")
my_res = my_tbl.select(COLUMNS).execute()
# Display the results . Demonstrates how to work with results
# Print the column names followed by the rows
column_names = my_res.get_column_names()
column_count = my_res.get_column_count()
for i in range(0,column_count):
    if i < column_count - 1:
        print "{0}, ".format(column_names[i]),
    else:
        print "{0}".format(column_names[i]),
print
for row in my_res.fetch_all():
    for i in range(0,column_count):
        if i < column_count - 1:
            print "{0}, ".format(row[i]),
        else:
            print "{0}".format(row[i]),
    print
# Update a row
my_tbl.update().set('NUM_TELF', 935876433).where('ID_CAIXER LIKE 124').execute()
print("\nShowing results after updating row with ID_CAIXER LIKE 124.")
# Execute a simple select (SELECT ∗ FROM)
my_res = my_tbl.select(COLUMNS).execute()
# Display the results
for row in my_res.fetch_all():
    print row
# Delete some rows
my_tbl.delete().where('NUM_TELF > 30').execute()
# Execute a simple select (SELECT ∗ FROM)
print("\nShowing results after deleting rows with NUM_TELF > 30.")
my_res = my_tbl.select(COLUMNS).execute()
# Display the results
for row in my_res.fetch_all():
    print row
# Delete the database (schema)
my_session.drop_schema('supermercat')
