def haha() :
    print('Hello')
    return 
    print('Hola')
print('Bonjour')
haha()          

def plusTwo(x) :
    x = x + 2
    return x

y = 5
z = plusTwo(y)
print(z)
# predicted output is 7

# exercise 1 
def computepay(h, r):
    if h > 40 :
        pay = 40 * r + (h - 40) * r * 1.5
    else : 
        pay = h * r
        
    return pay

hrs = input("Enter Hours:")
hrs = float(hrs)

rate = input('Enter Rate:')
rate = float(rate)

p = computepay(hrs, rate)
print("Pay", p)