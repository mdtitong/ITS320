# Develop a Python application that incorporates using appropriate data types and provides program output in a logical manner.  Your program should prompt a user to enter a car brand, model, year, starting odometer reading, an ending odometer reading, and the estimated miles per gallon consumed by the vehicle. Store your data in a dictionary and print out the contents of the dictionary.

car_details = {}

car_details['Car Brand'] = str(input('enter brand of the car: '))
car_details['Model'] = str(input('enter model of the car: '))
car_details['Year'] = int(input('enter year of the car: '))
car_details['Starting Odometer Reading'] = int(
    input('enter starting odometer reading of the car: '))
car_details['Ending Odometer Reading'] = int(
    input('enter ending odometer reading of the car: '))
car_details['Estimated Miles per Gallon'] = float(
    input('enter estimated miles per gallon of the car: '))


print(car_details)
