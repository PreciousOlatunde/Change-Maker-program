#ChangeMaker.py

#define different denomincations in cents
penny = 1
nickel = 5
dime = 10
quarter = 25
dollar = 100
five = 500
ten = 1000
twenty = 2000

#prompt user for item price
price = input("Price of the item: $")
price = float(price)

#prompt user for amount of cash paid
cash = input("Cash tendered: $")
cash = float(cash)

#calculate change
change = cash - price
print("Change: ${}".format(change))
change = int(change * 100)

twenties = int(change / twenty)
change = change % twenty

tens = int(change / ten)
change = change % ten

fives = int(change / five)
change = change % five

ones = int(change / dollar)
change = change % dollar

quarters = int(change / quarter)
change = change % quarter

dimes = int(change / dime)
change = change % dime

nickels = int(change / nickel)
change = change % nickel

pennies = change

#print change
print("Twenties ($20): {}".format(twenties))
print("Tens ($10): {}".format(tens))
print("Fives ($5): {}".format(fives))
print("Ones ($1): {}".format(ones))
print("Quarters ($0.25): {}".format(quarters))
print("Dimes ($0.10): {}".format(dimes))
print("Nickels ($0.05): {}".format(nickels))
print("Pennies ($0.01): {}".format(pennies))




