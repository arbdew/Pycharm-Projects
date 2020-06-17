class CoffeeMachine:

    def __init__(self):
        self.dollars = 550
        self.water = 400
        self.milk = 540
        self.coff = 120
        self.cups = 9
        self.things = ["water", "milk", "coffee beans", "cups", "money"]

    def menu(self):

        while True:
            action = input("\nWrite action(buy, fill, take, remaining, exit): ")
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.returnvalues()
            elif action == "exit":
                print("Goodbye!")
                break

    def buy(self):

        choice = input("Which variety would you like? 1 - espresso, 2 - latte, 3 - cappuccino, back: ")
        quantity = int(input("How many?: "))
        if choice == '1':
            self.water = self.water - (250 * quantity)
            self.coff = self.coff - (16 & quantity)
            self.dollars = self.dollars + (4 * quantity)
            self.cups = self.cups - 1 * quantity
            if self.water < 0 or self.coff < 0 or self.cups < 0:
                if self.water < 0:
                    print("Sorry, not enough water.")
                elif self.coff < 0:
                    print("Sorry, not enough coffee.")
                elif self.cups < 0:
                    print("Sorry, not enough coffee cups")
                self.water = self.water + (250 * quantity)
                self.coff = self.coff + (16 * quantity)
                self.dollars = self.dollars - (4 * quantity)
                self.cups = self.cups + (1 * quantity)

            elif quantity == 0:
                print("Taking you to the menu")
                pass
            else:
                print("I have enough resources, making you an espresso!")

        elif choice == '2':
            self.water = self.water - (350 * quantity)
            self.coff = self.coff - (30 * quantity)
            self.milk = self.milk - (75 * quantity)
            self.dollars = self.dollars + (7 * quantity)
            self.cups = self.cups - 1 * quantity
            if self.water < 0 or self.coff < 0 or self.milk < 0 or self.cups < 0:
                if self.water < 0:
                    print("Sorry, not enough water.")
                elif self.coff < 0:
                    print("Sorry, not enough coffee.")
                elif self.milk < 0:
                    print("Sorry, not enough milk.")
                elif self.coff < 0:
                    print("Sorry, not enough coffee")
                elif self.cups < 0:
                    print("Sorry, not enough coffee cups")
                self.water = self.water + (350 * quantity)
                self.coff = self.coff + (30 * quantity)
                self.milk = self.milk + (75 * quantity)
                self.dollars = self.dollars - (7 * quantity)
                self.cups = self.cups + (1 * quantity)
            elif quantity == 0:
                print("Taking you to the menu")
            else:
                print("I have enough resources, making you a latte!")

        elif choice == '3':
            self.water = self.water - (200 * quantity)
            self.coff = self.coff - (12 * quantity)
            self.milk = self.milk - (100 * quantity)
            self.dollars = self.dollars + (6 * quantity)
            self.cups = self.cups - (1 * quantity)
            if self.water < 0 or self.coff < 0 or self.milk < 0 or self.cups < 0:
                if self.water < 0:
                    print("Sorry, not enough water.")
                elif self.coff < 0:
                    print("Sorry, not enough coffee.")
                elif self.milk < 0:
                    print("Sorry, not enough milk.")
                elif self.coff < 0:
                    print("Sorry, not enough coffee")
                elif self.cups < 0:
                    print("Sorry, not enough coffee cups")
                self.water = self.water + (200 * quantity)
                self.coff = self.coff + (12 * quantity)
                self.milk = self.milk + (100 * quantity)
                self.dollars = self.dollars - (6 * quantity)
                self.cups = self.cups + (1 * quantity)
            elif quantity == 0:
                print("Taking you to the menu")
            else:
                print("I have enough resources, making you a cappucino!")


        elif choice == 'back':
            print("Taking you to the menu")
            pass

    def fill(self):

        while True:
            ing = input("What would you like to fill? water, milk, coffee or cups?\nexit to return to main menu: ")
            if ing == "exit":
                break
            elif ing == "water":
                self.water = self.water + int(input("Write how many ml of water do you want to add:"))
            elif ing == "milk":
                self.milk = self.milk + int(input("Write how many ml of milk do you want to add:"))
            elif ing == "coffee":
                self.cb = self.coff + int(input("Write how many g of coffee beans do you want to add:"))
            elif ing == "cups":
                self.cups = self.cups + int(input("Write how many disposable cups of coffee do you want to add:"))

    def take(self):
        dollars = self.dollars
        print("I gave you $", dollars)

        self.dollars = 0

    def returnvalues(self):
        water = self.water
        milk = self.milk
        coffee = self.coff
        cups = self.cups
        dollars = self.dollars
        print("The coffee machine has\n")
        print(water, "ml of water")
        print(milk, "ml of milk")
        print(coffee, "g of coffee")
        print(cups, "cups")
        print("$", dollars)
        print()
        print("remaining")


douwe = CoffeeMachine()
douwe.menu()
