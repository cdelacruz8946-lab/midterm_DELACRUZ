sales_file = open('sales_log.txt')

#SALES RECORD MANAGEMENT SYSTEM OPTIONS
def sales_record_management_system():

    print('='*30)
    print('SALES RECORD MANAGEMENT SYSTEM')
    print('='*30)
    print('1. Add Sale Record')
    print('2. View All Records')
    print('3. Clear All Records')
    print('4. Exit System')
    print('='*30)

myloop = True

while myloop:
    print(sales_record_management_system())

    user_options = input("Choose an option from 1-4:")

def errorEmptyInput():
    print("Input must not be empty!")

#OPTION 1

def exit_system():
    if user_options == "4":
        print('Thank you for using the Sales Record Management System!')
        exit()

if user_options == '':
    print(errorEmptyInput())

def add_sales_record():
    if user_options == "1":
        try:
            item_name = input('Item name: ')
            quantity_sold = input("Quantity sold: ")
            price_per_unit = input("Price per unit: ")

        except ValueError:
            if item_name == '':
                print(errorEmptyInput())
                return
            if quantity_sold == '':
                print(errorEmptyInput())
            if price_per_unit == '':
                print(errorEmptyInput())