# Vending Machine Logic

class VendingMachine:
    def __init__(self):
        self.drinks = {
            "Coke": 4.00,
            "Water": 2.00,
            "Milo": 3.00
        }

    def buy_drink(self, choice, amount):
        if choice not in self.drinks:
            print("Drink not available!")
            return

        price = self.drinks[choice]
        if amount < price:
            print("Insufficient amount!")
            return

        change = amount - price
        print(f"You bought {choice} for ${price:.2f}.")
        if change > 0:
            print("Your change:")
            self.give_change(change)

    def give_change(self, change):
        notes = [100, 50, 20, 10, 5, 1]  # Available notes
        for note in notes:
            count = change // note
            if count > 0:
                print(f"${note}: {count}")
                change -= count * note


def main():
    vending_machine = VendingMachine()
    print("Welcome to the vending machine!")
    print("Available drinks:")
    for drink, price in vending_machine.drinks.items():
        print(f"{drink}: ${price:.2f}")

    while True:
        choice = input("Enter your drink choice: ")
        amount = float(input("Insert notes: $"))
        vending_machine.buy_drink(choice, amount)
        if input("Do you want to buy more drinks? (yes/no): ").lower() != "yes":
            break


if __name__ == "__main__":
    main()
