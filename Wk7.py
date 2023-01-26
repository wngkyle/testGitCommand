x = 'hola dumbdumb'
y = x[4]
print(y, '\n')

x = 4
y = x
c = 4
print(y is x)
print(x is y)



# while loop
print('while loop: ')
n = 5
while n >= 0 :
    print(n) 
    n = n - 1
print('blastoff\n')

#for loop
print('for loop: ')
count = [5, 4, 3, 2, 1, 0]
for i in count :
    print(i)
print('blastoff\n')

# Finding the largest 
print('Finding the largest: ')
numberList = [74, 84, 92, 102, 12, 13, 47]
largestSoFar = numberList[0]
print('Before', largestSoFar)
for num in numberList :
    if num > largestSoFar :
        largestSoFar = num
print('After', largestSoFar, '\n')

# Counting in a loop
print('Counting in a loop')
count1 = 0
print('Before', count1)
for num in numberList :
    count1 = count1 + 1    
print('After', count1, '\n')

# Summing in a loop
print('Summing in a loop')
total = 0
print('Before', total)
for num in numberList :
    total = total + num
print('After', total, '\n')

# Finding the average 
print('Finding the average in a loop')
total = 0
count2 = 0
average = 0
print('Before', average)
for num in numberList :
    total = total + num
    count2 = count2 + 1
average = round(total / count2, 2)
print('After', average, '\n')

# filtering in a loop
print('Filtering in a loop')
for num in numberList :
    if num > 80 :
        print('Larger than 80:', num)       

# exercise 1
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try :
        num = int(num)
    except : 
        print('Invalid input')
        continue
    if largest is None :
        largest = num
        smallest = num
    elif largest < num :
        largest = num
    elif smallest > num :
        smallest = num
    else :
	    continue
print("Maximum is", largest)
print("Minimum is", smallest)