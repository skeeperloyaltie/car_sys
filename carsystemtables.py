import sqlite3


conn = sqlite3.connect("CarSales.db")
c = conn.cursor()
def tablecreate():
	table1 = """
	CREATE TABLE IF NOT EXISTS Employee (
	Name text NOT NULL, 
	ID_number integer PRIMARY KEY, 
	Department text NOT NULL,
	job_title text NOT NULL,
	Basic_salary integer
);
	"""
	table2 =  """
	CREATE TABLE IF NOT EXISTS Cars (
	Name text NOT NULL, 
	ID_number text NOT NULL PRIMARY KEY,
	Price integer, 
	Type text NOT NULL
);
	"""
	table3 =  """
	CREATE TABLE IF NOT EXISTS Sales (
	ID_number integer NOT NULL, 
	Name text NOT NULL, 
	Car_sold integer, 
	Price integer,  
	FOREIGN KEY (ID_number) REFERENCES Employee(ID_number )
);

	"""
	c.execute(table1)
	c.execute(table2)
	c.execute(table3)
	conn.commit()
	conn.close()
	
tablecreate()
