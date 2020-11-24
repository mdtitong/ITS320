# create an empty array

arr = []

# loop 5 times

for i in range(0, 5):

    x = float(input('Enter a number : '))

    # add x to arr

    arr.append(x)

sum = 0

# find the sum of all elements in arr

for x in arr:

    sum += x

# calculate average

average = sum / len(arr)

print('\n%15s %15s\n' % ('Original Value', 'Interest Value'))

for Original_value in arr:

    # calculate interesr value

    Interest_Value = Original_value * 0.2

    print('%10f %15f' % (Original_value, Interest_Value))

print('\nTotal :', sum)

print('Average :', average)

print('Maximum :', max(arr))

print('Minimum :', min(arr))
