# Vending Machine Logic

This Python script implements a simple vending machine simulation where customers can buy drinks by inserting notes. The vending machine calculates the change in the least amount of notes.

Usage

Run the script in a Python environment.
Follow the prompts to select a drink, insert notes, and receive change.
Repeat the process to buy more drinks or exit the vending machine.

VendingMachine Class

__init__(self): Initializes the vending machine with a dictionary of available drinks and their prices.
buy_drink(self, choice, amount): Allows the customer to buy a drink by specifying the drink choice and the amount inserted. Checks for drink availability and handles insufficient amount scenarios.
give_change(self, change): Calculates and gives back the change in the least amount of notes.

Main Function

main(): Acts as the entry point for the program. Displays available drinks, prompts the user to buy drinks, and manages the vending machine operations.

Available Drinks

- Coke: $4.00
- Water: $2.00
- Milo: $3.00

Notes

Available notes for change: $100, $50, $20, $10, $5, $1
