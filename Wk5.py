x = input('Enter a number: ')
try : 
    x = int(x) 
except : 
    try : 
        x = float(x)
    except : 
        x = -1

if x == -1 :
    print('Input inapplicable')
elif x < 10 : 
    print('small')
elif x < 20 :
    print('medium')
else : 
    print('large')

# exercise 1
# all hours above 40 hours are paid with 1.5 times the originally hourly pay
hrs = input("Enter Hours:")
h = float(hrs)
rate = input('Enter rate: ')
r = float(rate)
if h > 40 :
	pay = 40 * r + (h - 40) * r * 1.5
else :
    pay = h * r
print(pay)

# exercise 2
inputScore = input("Enter Score: ")
score = float(inputScore)
if score >= 0 :
    if score <= 1 :
        if score >= 0.9 :
            print('A')
        elif score >= 0.8 :
            print('B')
        elif score >= 0.7 :
            print('C')
        elif score >= 0.6 :
            print('D')
        else :
            print('F')
    else :
        print('Error')
else :
    print('Error')
