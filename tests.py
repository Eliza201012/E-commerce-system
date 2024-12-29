class User:
	def __init__(self, id, name, role):
		self.__id = id
		self.__name = name
		self.__role = role

	def get_id(self):
		return self.__id
	
	def get_name(self):
		return self.__name
	
	def get_role(self):
		return self.__role


class Customer(User):
	def __init__(self, id, name, role):
		super().__init__(id, name, role)
		self.backet = []

	def add_to_cart(self, product):
		self.backet.append(product)
		return self.backet
	
	def checkout(self):
		print(f"Ваше ім'я: {self.get_name()}, Id: {self.get_id()}, Роль: {self.get_role()}")
		print(f"Ваші замовлення {self.backet}")
	

class Admin(User):
	def __init__(self, id, name, role):
		super().__init__(id, name, role)
		self.catalog = []

	def add_product(self, product):
		self.catalog.append(product)
		return self.catalog
	
	def remove_product(self, product):
		if product in self.catalog:
			self.catalog.remove(product)
			return self.catalog
		else:
			print("Такого товару не існує")

class Product:
	def __init__(self, id, name, price):
		self.__id = id
		self.__name = name
		self.__price = price


product_admin = Admin(id=4567, name="Alice", role="Admin")
product_customer = Customer(id=1234, name="Alice", role=None)

print(product_admin.add_product(product="Banana"))
print(product_admin.remove_product(product="Banana"))

product_customer.add_to_cart(product="Pineapple")
product_customer.checkout()