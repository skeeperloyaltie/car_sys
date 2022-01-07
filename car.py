
	
class EmployeeDetails:
	def __init__(self,  name,  id , department,  title,  salary):
		self.name = name
		self.id = id
		self.department = department
		self.title = title
		self.salary = salary
		
		def set(self):
			pass

class Employees(EmployeeDetails):
	def __init__(self,name = None,  id = None , department = None,  title = None,  salary = None,  db = None):
		EmployeeDetails.__init__(self,  name,  id , department,  title,  salary)
		self.conn= connect(db)
		self.curr = self.conn.cursor()
		
	def get_id(self,  id):
		
		self.curr.execute()
		return self.curr.fetchall()
		
	def get_all(self):
			self.curr.execute("")
			return self.curr.fetchall()
		
	def set(self):
		self.curr.execute()
		self.conn.commit()
		
	def delete(self, id):
		sql = ''
		self.curr.execute(sql,  (id, ))
		
		
class Car:
			def __init__(self, name= None,  id = None,  price = None,  type = None,  db = None):
				self.name = name
				self.id = id
				self.price = price
				self.type = type
				self.conn= connect(db)
				self.curr = self.conn.cursor()
			
			def get_id(self,  id):
				self.curr.execute()
				return self.curr.fetchall()
				
			def get_all(self):
				self.curr.execute()
				return self.curr.fetchall()
			
			def set(self):
				self.curr.execute()
				self.conn.commit()
			
			def delete(self, id):
				sql = ''
				self.curr.execute(sql,  (id, ))

class Sales:
	def __init__(self,  userid = None,  name = None,  carid= None, sale = None,  db = None):
		self.name = name
		self.cid = carid
		self.uid = userid
		self.sale = sale
		self.conn = connect(db)
		self.curr = self.conn.cursor()
		
	def set(self):
			self.curr.execute()
			self.conn.commit()
			
	def get_id(self,  id):
			self.curr.execute()
			return self.curr.fetchall()
	def get_all(self):
			self.curr.execute()
			return self.curr.fetchall()
	def delete(self, id):
				sql = ''
				self.curr.execute(sql,  (id, ))
				
	def get_salary(self):
		sales = self.curr.execute().fetchall()
		manager = self.curr.execute().fetchall()
		salesp = self.curr.execute().fetchall()
		result = []
		for i in salesp:
			u = i
			usdet = self.curr.execute().fetchall()
			profit = 0
			for j in sales:
				
				if j[0] == i[0]:
					
					carprice = self.curr.execute().fetchall()
					profit  += j[2] - carprice[0][0]
			#print(usdet)
			salary = (profit * 6.5) + usdet[0][1]
			mansal = (profit * 3.5) +manager[0][1]
			result.append((u[1], salary))
			result.append((manager[0][0],   mansal))
		return result
			
	


def fill_sale_data():
	salesdata = [["Joy Rogers", "ZX3",155000], ["Joy Rogers", "VX3", 57800],["Joy Rogers", "VX3", 55000], ["Joy Rogers","SX3", 89000], ["Joy Rogers","SX3", 93000],["Mark Jones", "VX3", 58000], ["Mark Jones","VX3", 58000], ["Mark Jones", "VX3", 158000],["Mark Jones", "VX3", 158000], ["Mark Jones", "VX3", 158000]]
	cur = connect("").cursor()
	for i in salesdata:
		userid = cur.execute("Select ID_number from Employee where Name = ?", (i[0], )).fetchall()
		c= Sales(userid[0][0],  i[0],  i[1], i[2],  db="")
		c.set()


def fill_emp_data():
    employeedata = [["Susan Meyers",47899, "Accounting","Manager", 37500],  ["Mark Jones", 39119, "IT", "Salesperson", 26000], ["Joy Rogers", 81774, "Manufacturing", "Salesperson", 24000]]
    for i in employeedata:
      	c = Employees(i[0], i[1], i[2], i[3], i[4],  "")
      	c.set()


def fill_car_data():
	car_data=[["Jazz", "VX3", 55000,  "Hatch"], ["Mark3", "SX3", 84000, "Sedan"], ["Wagoner", "ZX3", 125000, "SUV"]]
	for i in car_data:
	     	c = Car(i[0], i[1], i[2], i[3],  "")
	     	c.set()


def print_menu():
	print("")	
	
def few_db_fillers_and_actions():
	print("\n\n")
	fill_emp_data()#fill employee tabme
	c = Employees(db = "")
	#c.delete(81774)
	print(c.get_id(81774))
	
	print("\n\n")
	fill_car_data()#fill car table
	c = Car(db = "")
	print(c.get_id("VX3"))
	print("\n\n")
	fill_sale_data()# fill sale table with data
	c = Sales(db = "")
	#print(c.get_id(81774))
	print(c.get_salary())

#few_db_fillers_and_actions()

if __name__ == "__main__":
	print_menu()
	ch = print("")
	if ch == 1:
		few_db_fillers_and_actions()
	elif ch == 2:
		c = Employees(db = "")
		l = c.get_all()
		print("Name     |  ID Number | Department | Job | Basic Salary")
		for i in l:
			for c in i:
				print(c,  end="   ")
			print()
		
