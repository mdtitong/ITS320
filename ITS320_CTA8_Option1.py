car_details = {}
inventory = [
    {'Make': 'Subaru', 'Model': 'Crosstrek',
        'color': 'white', 'Year': 2018, 'Miles': 15000}

]


class car_info:

    def __init__(self, make, model, color, year, miles):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.miles = miles

    def make(self):
        return self.make

    def model(self):
        return self.model

    def color(self):
        return self.color

    def year(self):
        return self.year

    def miles(self):
        return self.miles


def main():
    while True:
        try:
            menu()
            choice = int(input('Choose by Entering the Number (1-6): '))
            print('----------------------------------------')

            if choice == 1:
                add()
            elif choice == 2:
                remove()
            elif choice == 3:
                update()
            elif choice == 4:
                view()
            elif choice == 5:
                print_txt()
            elif choice == 6:
                print('Thank You!')
                quit()
            else:
                print('INVALID INPUT! Please Enter the Correct Number (1-6): ')
        except ValueError:
            print('INVALID INPUT! You Can Only Enter Numbers from 1-6!')


def header():
    print('======     ---< ABC AUTO >---     ======')


def menu():
    header()
    print('========================================')
    print('1. Add')
    print('2. Remove')
    print('3. Update')
    print('4. View')
    print('5. Print')
    print('6. Exit')
    print('========================================')


def add():
    header()
    print('----- ADD A CAR TO THE INVENTORY -------')

    while True:
        try:
            car_details = {}

            car_details['Make'] = str(input('enter brand of the car: '))
            car_details['Model'] = str(input('enter model of the car: '))
            car_details['color'] = str(input('enter color of the car: '))
            car_details['Year'] = int(input('enter year of the car: '))
            car_details['Miles'] = int(input('enter Mileage of the car: '))
            inventory.append(car_details)
            print('>>>>> Car details have been added to the inventory!')
            break
        except Exception:
            print('INVALID INPUT! PLEASE TRY AGAIN')


def remove():
    header()
    print('---- REMOVE A CAR FROM THE INVENTORY -----')
    view()
    while True:
        try:
            del_item = int(
                input('Choose the car you want to remove (use number correspondence): '))

            del inventory[del_item-1]
            print('>>>>> You have deleted a car in the inventory!')
            break
        except Exception:
            print('INVALID INPUT! PLEASE TRY AGAIN!')


def update():
    header()
    print('----- UPDATE A CAR TO THE INVENTORY ----')
    view()
    while True:
        try:
            del_item = int(
                input('Choose the car you want to update (use number correspondence): '))
            del inventory[del_item-1]
            car_details = {}
            car_details['Make'] = str(input('enter brand of the car: '))
            car_details['Model'] = str(input('enter model of the car: '))
            car_details['color'] = str(input('enter color of the car: '))
            car_details['Year'] = int(input('enter year of the car: '))
            car_details['Miles'] = int(input('enter Mileage of the car: '))
            inventory.insert(del_item-1, car_details)
            print('>>>>> Car has been updated!')
            break
        except Exception:
            print('INVALID INPUT! PLEASE TRY AGAIN')


def view():
    header()
    print('----- ABC AUTO INVENTORY -----------')
    for i, car_details in enumerate(inventory):
        print(i+1, car_details)
    print('----------------------------------------')


def print_txt():
    txt_file = open('InventoryTextFile', 'w')
    txt_file.write(str(inventory))
    txt_file.close()
    print('>>>>> A Text File has been created containing the inventory of ABC AUTO (InventoryTextFile.txt)')


main()
