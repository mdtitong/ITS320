# Read two integers and print two lines. The first line should contain integer division, //, the second line
# should contain float division, /, and the third line should contain modulo division, %. You do not need to
# perform any rounding or formatting operations.
num1 = int(input("First number: "))
num2 = int(input("Second number: "))

divide = num1 // num2
fdivide = num1 / num2
modulo = num1 % num2
print(divide)
print(fdivide)
print(modulo)
