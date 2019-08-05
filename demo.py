import datetime
from user import User

class Demo():
    def __init__(self):
        self.user_list = []

    def _get_user(self):
        access_user = input("\n Enter the user's email address to find them: ")
        users = [u for u in self.user_list if u.email == access_user]
        if len(users) != 1:
            return None
        return users[0]

    def create_user(self):
        emp_first = input("\n\n Enter employees first name: ")
        emp_last =  input("\n\n Enter employees last name: ")
        email = input("\n\n Enter employees email address: ")
        phone_number = int(input("\n\n Enter employees phone number: "))
        self.user_list.append(User(emp_first, emp_last, email, phone_number))

    def set_availability(self):
        user = self._get_user()
        if not user:
            return False

        mon_start = int(input("\nEnter a start time for mon: "))
        mon_end = int(input("\n Enter an end time for mon: "))
        tue_start = int(input("\n Enter a start time for tue: "))
        tue_end = int(input("\n Enter an end time for tue: "))
        wed_start = int(input("\n Enter a start time for wed: "))
        wed_end = int(input("\n Enter an end time for wed: "))
        thu_start = int(input("\n Enter a start time for thu: "))
        thu_end = int(input("\n Enter an end time for thu: "))
        fri_start = int(input("\n Enter a start time for fri: "))
        fri_end = int(input("\n Enter an end time for fri: "))
        sat_start = int(input("\n Enter a start time for sat: "))
        sat_end = int(input("\n Enter an end time for sat: "))
        sun_start = int(input("\n Enter a start time for sun: "))
        sun_end = int(input("\n Enter an end time for sun: "))

        user.create_availability(
            mon_start, mon_end,
            tue_start, tue_end,
            wed_start, wed_end,
            thu_start, thu_end,
            fri_start, fri_end,
            sat_start, sat_end,
            sun_start, sun_end
        )
        return True

    def show_users(self):
        for user in self.user_list:
            print(str(user))

    def view_availability(self):
        user = self._get_user()
        if not user:
            return False

        day = input("What day did you want to check?")
        time = int(input("What time did you want to check?"))

        rv = user.get_availability(day, time)
        print(f"\n{rv}")
        return rv

    def delete_user(self):
        user = self._get_user()
        if not user:
            return False

        self.user_list.remove(user)

        self.show_users()
        return True

    def menu(self):
        options = {
            1: self.create_user,
            2: self.set_availability,
            3: self.show_users,
            4: self.view_availability,
            5: self.delete_user
        }
        while True:
            print("""
                Select an option to begin:
                Enter 1 to create a new user
                Enter 2 to set availability
                Enter 3 to view all users
                Enter 4 to view availability
                Enter 5 to delete a user
                Enter 7 to exit""")

            option = int(input("What would you like to do?:"))
            if (option == 7):
                return

            if option in options:
                options[option]()


def main():
    demo = Demo()
    demo.menu()


if __name__== "__main__":
    main()
