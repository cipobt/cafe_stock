# This program calculates the total stock worth in a cafe.

# To add features in output messages

BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
WHITE = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

# Creating the list 'menu'

menu = ["Flavoured Mocha", "Ginger Ale Can", "Black Coffee", "Sausage Roll"]

# Creating dictionaries 'stock' and 'price'

stock = {
    'Flavoured Mocha': 150,
    'Ginger Ale Can': 300,
    'Black Coffee': 2000,
    'Sausage Roll': 600
}

price = {
    'Flavoured Mocha': 3.45,
    'Ginger Ale Can': 1.5,
    'Black Coffee': 2.85,
    'Sausage Roll': 1.5
}

# Creating a new dictionary to register total stock value

stock_worth = {}

# Calculating total value of cafe's stock

for item in menu:
    stock_worth[item] = stock[item] * price[item]

# Printing out the results

print(f"{BOLD}{YELLOW}♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦{WHITE}")
print(f"{BOLD}{UNDERLINE}{RED}Café Paris Stock Inventory{WHITE}")
print(f"{BOLD}{YELLOW}♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦{WHITE}\n")
print(f"\t{BOLD}{UNDERLINE}TOTAL STOCK WORTH\n")

for item in menu:
    print(f"{BOLD}{BLUE}{UNDERLINE}{item}{WHITE} (in £): {GREEN}{stock_worth[item]}")
