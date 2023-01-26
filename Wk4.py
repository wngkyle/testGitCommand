# exercise 1
inputFloor = input('Which floor do you want to go: ')
val = int(inputFloor)
print('The elevator is going to', val, 'floor')

# exercise 2
hrs = input('Enter hours: ')
rt = input('Enter rate: ')
pay = float(hrs) * float(rt)
print('Pay : $' + str(pay)) #need to cast variable pay from float to string first so it can be concatenate 