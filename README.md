# Café Stock Worth Calculator

This program calculates the total stock worth in a café based on the items in the menu and their respective quantities and prices.

Features
The program includes the following features:

• A list of available items in the café's menu.

• Dictionaries to store the stock and price information for each item.

• Calculation of the total value of each item's stock.

• Display of the total stock worth for each item in the menu.

Usage
To run the program, ensure you have Python installed on your machine.

Clone the repository:
git clone https://github.com/cipobt/cafe_stock/
cd cafe-stock-worth

Run the script:
python cafe_stock_worth.py

The program will display the total stock worth for each item in the café's menu.

Output Format
The program will output the total stock worth in the following format:

♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦
Café Paris Stock Inventory
♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦

        TOTAL STOCK WORTH

Flavoured Mocha (in £): 517.5
Ginger Ale Can (in £): 450.0
Black Coffee (in £): 5700.0
Sausage Roll (in £): 900.0

Customize
To customize the menu and prices, modify the menu, stock, and price dictionaries in the cafe.py file. Add or remove items as needed, ensuring the item names are consistent between the menu, stock, and price dictionaries.

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

Color Codes
The program uses color codes for better visual presentation:

BLUE: '\033[94m'

GREEN: '\033[92m'

YELLOW: '\033[93m'

RED: '\033[91m'

WHITE: '\033[0m'

BOLD: '\033[1m'

UNDERLINE: '\033[4m'

License

This project is licensed under the MIT License. Feel free to use and modify it according to your needs.

This project is licensed under the MIT License. Feel free to use and modify it according to your needs.
