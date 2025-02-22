'''coffeShop'''

# Variable holds price of items and number of items
cofPrice = 5
mufPrice = 4
espPrice = 6 #NEW ITEM PRICE: ESPRESSP
latPrice = 6.5 #NEW ITEM PRICE: LATTE
sconPrice = 4 #NEW ITEM PRICE: SCONE
numCof = 0
numMuf = 0 
numEsp = 0 #NEW ITEM: ESPRESSO
numLat = 0 #NEW ITEM: LATTE
numScon = 0 #NEW ITEM: SCONE
totalCof = 0
totalMuf = 0 
totalEsp = 0 #NEW ITEM TOTAL: ESPRESSO
totalLat = 0 #NEW ITEM TOTAL: LATTE
totalScon = 0 #NEW ITEM TOTAL: SCONE
tax = 0.06
totalTax = 0 
total = 0

# Get's imput from user and assigns it to variables
numCof = int(input('How many coffees would you like? '))
numMuf = int(input('How many muffins would you like? '))

# INPUT FOR NEW ITEMS
numEsp = int(input('How many espressos would you like? '))
numLat = int(input('How many lattes would you like? '))
numScon = int(input('How many scones would you like? '))

# Calculates and assigns values to remaining variables
totalCof = float(numCof * cofPrice)
totalMuf = float(numMuf * mufPrice)
totalEsp = float(numEsp * espPrice) # ESPRESSO TOTAL
totalLat = float(numLat * latPrice) # LATTE TOTAL
totalScon = float(numScon * sconPrice) # SCONE TOTAL
totalTax = (totalCof + totalMuf + totalEsp + totalLat + totalScon) * tax # CALCULATES TOTALTAX WITH NEW ITEMS
total = totalCof + totalMuf + totalEsp + totalLat + totalScon + totalTax # CALCULATES TOTAL WITH NEW ITEMS 

# Prints the reciept
print('*' * 20)
print('My Coffee and Muffin Shop')
print('Number of coffees bought?') # Prints number of coffees
print(numCof)
print('Number of Muffins bought') # Prints number of muffins
print(numMuf)
print('Number of espressos bought?') # Prints number of espressos
print(numEsp)
print('Number of lattes bought?') # Prints number of lattes
print(numLat)
print('Number of scones bought?') # Prints number of scones
print(numScon)
print('*' * 20, '\n')
print('*' * 20)
print('My Coffee and Muffin Shop Receipt') 

# Prints price of coffees and muffins, determines plurality
if numCof <= 1 :
    print(f'{numCof} Coffee at $5.00 each: ${totalCof:.2f}')
elif numCof > 1 :
    print(f'{numCof} Coffees at $5.00 each: ${totalCof:.2f}')
if numMuf <= 1 :
    print(f'{numMuf} Muffin at $4.00 each: ${totalMuf:.2f}')
elif numMuf > 1 :
    print(f'{numMuf} Muffins at $4.00 each: ${totalMuf:.2f}')

# PRINTS PRICE OF NEW ITEMS AND DETERMINES PLURALITY
if numEsp <= 1 :
    print(f'{numEsp} Espresso at $6.00 each: ${totalEsp:.2f}')
elif numEsp > 1 :
    print(f'{numEsp} Espressos at $6.00 each: ${totalEsp:.2f}')
if numLat <= 1 :
    print(f'{numLat} Latte at $6.50 each: ${totalLat:.2f}')
elif numLat > 1 :
    print(f'{numLat} Lattes at $6.50 each: ${totalLat:.2f}')
if numScon <= 1 :
    print(f'{numScon} Scone at $4.00 each: ${totalScon:.2f}')
elif numScon > 1 :
    print(f'{numScon} Scones at $4.00 each: ${totalScom:.2f}')
    
print('6% tax: $',totalTax) # Prints total tax 
print('-' * 9)
print('Total: $',total) # Prints total including tax
print('*' * 20)

# PRINTS THANK YOU MESSAGE
print('Thank you for coming \n Enjoy')
print('*' * 20)
