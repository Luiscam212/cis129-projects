# Module 4 Lab-4
# Luis Camacho
# 03/01/2025
# Calculates and prints the store and employee bonus based on user input of the monthly sales of the store and the sales increase of the store

# The main function
def main():
# declare local variables
    monthlySales = 0    # monthly sales amount
    storeAmount = 0         # store bonus amount
    empAmount = 0          # employee bonus amount
    salesIncrease = .00      # percent of sales increase

    monthlySales = getSales(monthlySales)          # call to getSales(monthlySales)
    salesIncrease = getIncrease(salesIncrease)        # call to getIncrease(salesIncrease)
    storeAmount = calcStoreBonus(monthlySales)         # call to calcStoreBonus(smonthlySales)
    empAmount = calcEmpBonus(salesIncrease)             # call to calcEmpBonus(salesIncrease)
    printBonus(storeAmount,empAmount)   # call to printBonus(storeAmount,empAmount)

# This function gets the monthly sales
def getSales(prompt):
    monthlySales = float(input("Enter the monthly sales: "))
    return monthlySales

# This function gets the percent of increase in sales
def getIncrease(prompt):
    salesIncrease = float(input("Enter the percent increase: "))
    salesIncrease = salesIncrease / 100
    return salesIncrease    # This function determines the storeAmount bonus

def calcStoreBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 4000
    else:
        storeAmount = 0
    return storeAmount

# This function determines the empAmount bonus
def calcEmpBonus(salesIncrease):
    if salesIncrease >= .05:
        empAmount = 75
    elif salesIncrease >= .04:
        empAmount = 50
    elif salesIncrease >= .03:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount

# This function prints the bonus information
def printBonus(storeAmount,empAmount):
    print("The store bonus amount is $",storeAmount)
    print("The employee bonus amount is $",empAmount)
    if storeAmount == 6000 and empAmount == 75:
        print('Congrats! You have reached the highest bonus amounts possible!')

# calls main
main()
