from abc import ABC, abstractmethod


# abstraction
class Coffee(ABC):

    def __init__(self, name):
        # encapsulation
        self._name = name
        self._water = 0
        self._milk = 0
        self._coffee = 0

    @abstractmethod
    def recipe(self):
        pass

    @abstractmethod
    def serve(self):
        pass

    def show_ingredients(self):
        print(f"\n{self._name} Ingredients")
        print(f"Water  : {self._water} ml")
        print(f"Milk   : {self._milk} ml")
        print(f"Coffee : {self._coffee} g")


# inheritance
class Espresso(Coffee):

    def __init__(self):
        super().__init__("Espresso")

    # overriding
    def recipe(self):
        self._water = 30
        self._milk = 0
        self._coffee = 18

    # overriding
    def serve(self):
        print("Serving Espresso ☕")


# americano inherits espresso
class Americano(Espresso):

    def __init__(self):
        super().__init__()
        self._name = "Americano"

    # overriding
    def recipe(self):
        super().recipe()
        self._water += 90

    # overriding
    def serve(self):
        print("Serving Americano ☕")


# latte inherits espresso
class Latte(Espresso):

    def __init__(self):
        super().__init__()
        self._name = "Latte"

    # overriding
    def recipe(self):
        super().recipe()
        self._milk = 150

    # overriding
    def serve(self):
        print("Serving Latte ☕")


# cappuccino inherits espresso
class Cappuccino(Espresso):

    def __init__(self):
        super().__init__()
        self._name = "Cappuccino"

    # overriding
    def recipe(self):
        super().recipe()
        self._milk = 100

    # overriding
    def serve(self):
        print("Serving Cappuccino ☕")


class CoffeeMachine:

    # overloading using default parameter
    def make_coffee(self, coffee, sugar=0):

        print("\nPreparing Coffee...")

        coffee.recipe()
        coffee.show_ingredients()

        print(f"Sugar  : {sugar} spoon")

        coffee.serve()

        print(f"{coffee._name} is Ready!\n")

    def menu(self):

        while True:

            print("====== ECO COFFEE MACHINE ======")
            print("1. Espresso")
            print("2. Americano")
            print("3. Latte")
            print("4. Cappuccino")
            print("5. Exit")

            choice = input("\nEnter your choice : ")

            if choice == "1":
                coffee = Espresso()
                self.make_coffee(coffee)

            elif choice == "2":
                coffee = Americano()
                self.make_coffee(coffee, 1)

            elif choice == "3":
                coffee = Latte()
                self.make_coffee(coffee, 2)

            elif choice == "4":
                coffee = Cappuccino()
                self.make_coffee(coffee, 1)

            elif choice == "5":
                print("\nThank You For Using Eco Coffee Machine ☕")
                break

            else:
                print("\nInvalid Choice\n")


machine = CoffeeMachine()
machine.menu()