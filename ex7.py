portionDeposit = 0.20
currentSavings = 0
r = 0.04

annualSalary = int(input("Enter your Annual Salary: "))
portionSaved = float(input("Enter the portion of your salary to be saved (decimal form): "))
totalCost = int(input("Enter the cost of your Dream Home: "))

homeDeposit = portionDeposit * totalCost

monthlySalary = annualSalary/12

months = 0

while currentSavings <= homeDeposit:

    savingsInterest = (currentSavings * r)/12
    monthlySavings = (portionSaved * monthlySalary) + savingsInterest
    currentSavings = currentSavings + monthlySavings
    months = months + 1
    print("monthlySavings:      ",monthlySavings)
    print(months)
