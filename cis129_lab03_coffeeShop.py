'''coffeShop'''

# Variable holds price of items and number of items
cofPrice = 5
mufPrice = 4
numCof = 0
numMuf = 0
totalCof = 0
totalMuf = 0
tax = 0.06
totalTax = 0 
total = 0

# Get's imput from user and assigns it to variables
numCof = int(input('How many coffees would you like? '))
numMuf = int(input('How many muffins would you like? '))

# Assigns appropriate values to remaining variables
totalCof = float(numCof * cofPrice)
totalMuf = float(numMuf * mufPrice)
totalTax = (totalCof + totalMuf) * tax
total = totalCof + totalMuf + totalTax

# Prints the reciept
print('*' * 20)
print('My Coffee and Muffin Shop')
print('Number of coffees bought?') # Prints number of coffees
print(numCof)
print('Number of Muffins bought') # Prints number of muffins
print(numMuf)
print('*' * 20, '\n')
print('*' * 20)
print('My Coffee and Muffin Shop Receipt') # Prints price of coffees and muffins, determines plurality
if numCof <= 1 :
    print(f'{numCof} Coffee at $5 each: ${totalCof:.2f}')
elif numCof > 1 :
    print(f'{numCof} Coffees at $5 each: ${totalCof:.2f}')
if numMuf <= 1 :
    print(f'{numMuf} Muffin at $4 each: ${totalMuf:.2f}')
elif numMuf > 1 :
    print(f'{numMuf} Muffins at $4 each: ${totalMuf:.2f}')
print('6% tax: $',totalTax) # Prints total tax 
print('-' * 9)
print('Total: $',total) # Prints total including tax
print('*' * 20)
