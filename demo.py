import datetime
from User import User




#Variables and lists needed for program. 

user_list = []

#Need to make sure to add DOB 
def create_user():

	global user_list

	active_create_account  = False

	emp_first = input("\n\n Enter employees first name: ")

	emp_last =  input("\n\n Enter employees last name: ")

	email = input("\n\n Enter employees email address: ")

	phone_number = int(input("\n\n Enter employees phone number: "))


	user_list.append(User(emp_first,emp_last,email,phone_number))

	for i in user_list:
		print(i.to_string())



#Now that you can access it, work on setting availabilty 
def set_availability():




	access_user = input("\n Enter the user's email address to find them: ") 

	for i in user_list:

		if access_user ==  i._User__email:
			print("\nfill in the employees available start and end times")
			start_mon = int(input("\nEnter a start time for mon: "))
			end_mon = int(input("\n Enter an end time for mon: "))
			start_tue = int(input("\n Enter a start time for tue: "))
			end_tue = int(input("\n Enter an end time for tue: "))
			start_wed = int(input("\n Enter a start time for wed: "))
			end_wed = int(input("\n Enter an end time for wed: "))
			start_thu = int(input("\n Enter a start time for thu: "))
			end_thu = int(input("\n Enter an end time for thu: "))
			start_fri = int(input("\n Enter a start time for fri: "))
			end_fri = int(input("\n Enter an end time for fri: "))
			start_sat = int(input("\n Enter a start time for sat: "))
			end_sat = int(input("\n Enter an end time for sat: "))
			start_sun = int(input("\n Enter a start time for sun: "))
			end_sun = int(input("\n Enter an end time for sun: "))

			i.set_availability(start_mon,end_mon,start_tue,end_tue,start_wed,end_wed,start_thu,end_thu,start_fri,end_fri,start_sat,end_sat,start_sun,end_sun)
			


def show_users():

	global user_list

	for i in user_list:
			print(i.to_string())



def view_availability():


	access_user = input("\n Enter the user's email address to view availabilty: ") 

	for i in user_list:

		if access_user == i._User__email:

			day = input("What day did you want to check?")
			time = int(input("What time did you want to check?"))

			print("\n",i.get_availability(day,time))


def delete_user():

	delete_user = input("\n Enter the user's email address to delete them: ")

	for i in user_list:

		if delete_user == i._User__email:

			user_list.remove(i)

			for i in user_list:
				print(i.to_string())



#main program
def main():

	active_create_account = True

	main_console = ("\nSelect an option to begin:")
	main_console += ("\n\nEnter 1 to create a new user")
	main_console += ("\nEnter 2 to set availability")
	main_console += ("\nEnter 3 to view all users")
	main_console += ("\nEnter 4 to view availability")
	main_console += ("\nEnter 5 to delete a user")
	main_console += ('\nEnter 7 to exit')
	main_console += ('\n\nWhat would you like to do?:')









	while True:

		user_option = int(input(main_console))

	

		#Switch statement
		switcher = {

	
			
			1:

				create_user,


			2:


				set_availability,

			3:

				show_users,


			4:

				view_availability,

			5:

				delete_user,
				

			7:

				exit

			}

		switcher.get(user_option,None)()
							





	


if __name__== "__main__":
	main()
















'''

print("hello world")

cong = User("Cong","Do","congdoe@gmail.com","7036094480")

print(cong.to_string())

cong.set_dob(datetime.date(1992,10,12))

print(cong.get_dob().strftime("%B %d, %Y"))

cong.set_availability(900,1700,900,500,900,500,900,500,900,500,900,500,900,500)

print(cong.get_availability().is_available('monday',1000))
'''





