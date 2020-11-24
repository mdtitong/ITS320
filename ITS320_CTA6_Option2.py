# imported itertools to solve cartesian product using product() function
import itertools
print('====== LIST COMPUTATION ======\n')

# user input number of required elements not more than 10 numbers
num = int(input("Enter number of elements containing not more than 10 numbers: "))
while num > 10:
    print('list must contain not greater than 10 items!')
    num = int(input("Enter the right number of elements: "))

# user input the numbers to be stored in the List
A = list(map(int, input("\nA: Enter the numbers : ").strip().split()))[:num]
B = list(map(int, input("B: Enter the numbers : ").strip().split()))[:num]
print("\nA = ", A)
print("B = ", B)

# prints out the Cartesian Product in the list provided by the user
print('\n====== CARTESIAN PRODUCT ======\n')
print('AxB = ', end=' ')
for item in itertools.product(A, B):
    print(item, end=' ')
print('\n\n===============================\n')
