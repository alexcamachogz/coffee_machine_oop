# Coffee Machine

This repository contains a coffee machine simulation implemented in Python. The program allows users to interact with a virtual coffee machine, select drinks from a menu, and process payments.

## Prerequisites

Before running the code, make sure you have the following installed:
* Python 3.x

## Installation

To get started, follow the steps below:
1. Clone the repository:
```
  git clone https://github.com/your-username/coffee-machine.git
```  
2. Change into the project directory:
```
  cd coffee-machine
```
3. No additional dependencies are required.

## Usage

To run the quiz game, execute the following command:
```
  python main.py
```

## Code Explanation

The code consists of several components:

1. `menu.py`: This module defines the `Menu` class, which represents the menu options available in the coffee machine. It provides methods for retrieving the drink items and finding a specific drink based on user input.

2. `coffee_maker.py`: This module contains the `CoffeeMaker` class, responsible for handling the coffee-making functionality. It tracks the available resources (such as water, milk, coffee, and cups) and checks if there are sufficient resources to make a specific drink. The `make_coffee()` method is used to brew a drink, and the `report()` method provides a report of the current resource levels.

3. money_machine.py: This module defines the MoneyMachine class, which handles payment processing. It keeps track of the total amount of money collected and provides methods for accepting payments and checking if a payment is sufficient. The report() method provides a report of the money collected.

4. The main part of the code initializes instances of the `Menu`, `CoffeeMaker`, and `MoneyMachine` classes.

5. The program runs in an infinite loop to continuously prompt the user for their desired drink selection. It retrieves the available drink options from the menu and displays them to the user.

6. Depending on the user's input, different actions are taken:

* If the user enters "off", the program prints a farewell message and exits the loop, turning off the coffee machine.
* If the user enters "report", the coffee maker and money machine generate and display reports of their respective statuses.
* If the user enters a valid drink option, the program checks if there are sufficient resources and if the payment is successful. If both conditions are met, the coffee maker brews the drink.

7. If the user enters an invalid option, the program displays an error message and prompts the user to try again.

## License
This project is licensed under the [MIT License](LICENSE).
