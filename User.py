import datetime
from Availability import Availability

class User():


	def __init__(self,first_name,last_name,email,phone_number):

			self.__first_name = first_name
			self.__last_name = last_name
			self.__email = email
			self.__phone_number = phone_number
			self.dob = None
			self.__availability = Availability()



	def get_name(self):
		return f'{self.__first_name} {self.__last_name}'

	def set_first_name(self,new_name):
		self.__first_name = new_name


	def set_last_name(self,new_name):
		self.__last_name = new_name

	def get_email(self):
		return self.__email

	def set_email(self,new_email):
		self.__email = new_email

	def get_phone(self):
		return self.__phone_number

	def set_phone_number(self,new_number):
		self.__phone_number = new_number

	def get_dob(self):
		return self.__dob

	def set_dob(self,dob_date):
		self.__dob = dob_date

	def get_availability(self,day,time):
		return self.__availability.is_available(day,time)

	def set_availability(self,start_mon,end_mon,start_tue,end_tue,start_wed,end_wed,start_thu,end_thu,start_fri,end_fri,start_sat,end_sat,start_sun,end_sun):

		#use Availability class implementation
		self.__availability.set_mon(start_mon,end_mon)
		self.__availability.set_tue(start_tue,end_tue)
		self.__availability.set_wed(start_wed,start_wed)
		self.__availability.set_thu(start_thu,start_thu)
		self.__availability.set_fri(start_fri,start_fri)
		self.__availability.set_sat(start_sat,start_sat)
		self.__availability.set_sun(start_sun,start_sun)



	def to_string(self):
		return f'Name: {self.get_name()}, Email: {self.get_email()}, Phone Number: {self.get_phone()}'



#TODO: Add Manager and Employee class that INHERIRITS from User class
#Employee should inherit from User.
#Manager should inherit from Employee.

class Employee(User):
	def __init__(self,first_name,last_name,email,phone_number,store,emp_type):
		User.__init__(self,first_name,last_name,email,phone_number)
		self.__store = store
		self.__type = emp_type



print("hello world")

cong = User("Cong","Do","congdoe@gmail.com","7036094480")

print(cong.to_string())

cong.set_dob(datetime.date(1992,10,12))

print(cong.get_dob().strftime("%B %d, %Y"))

cong.set_availability(900,1700,900,500,900,500,900,500,900,500,900,500,900,500)

print(cong.get_availability('monday',1000))







