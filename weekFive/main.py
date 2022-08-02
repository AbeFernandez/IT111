import csv
from _csv import writer
from datetime import date

today = date.today()


def read_csv():
    with open('employee.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        print("\nThe Data")
        print("_" * 58)
        for row in csv_reader:
            print("%-20s | %-20s | %10s |" % (row[0], row[1], row[2]))
            line_count += 1


def years_working(user_name):
    with open('employee.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        print("\n" + "_" * 44)
        for row in csv_reader:
            if row[0] == user_name:
                print(row[0] + " have", (today.year - int(row[2])), "years in the company")

            else:
                print("Name is not found in this row.")


def append_list_as_row(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)


def main():


    loop_control = True

    while loop_control:
        print("\nPress '1' to take a look at the list")
        print("Press '2' to append to the list")
        print("Press '3' to find out how many years have an employee in the company")
        print("Press '4' to 'EXIT'\n")
        menu = int(input("Enter a number: "))
        if menu == 1:
            read_csv()

        if menu == 2:
            control = True
            while control:
                user_name = input("Enter employee full name: ")
                if not user_name:
                    print("can't be empty!")
                else:
                    control = False
            control = True
            while control:
                user_department = input("Enter employee department: ")
                if not user_department:
                    print("can't be empty!")
                else:
                    control = False

            control = True
            while control:
                try:
                    user_year = int(input("Enter employee start year (1999): "))
                except ValueError:
                    print("Only numbers and can not be empty")
                else:
                    control = False
            employee = [user_name, user_department, user_year]
            append_list_as_row("employee.csv", employee)

        if menu == 3:
            find_employee = input("Enter the employee full name: ")
            years_working(find_employee)

        if menu == 4:
            print("\nThank you for using our platform!")
            loop_control = False


main()
