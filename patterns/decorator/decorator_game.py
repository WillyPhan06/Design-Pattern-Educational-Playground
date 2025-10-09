from rich.console import Console
from rich.prompt import Prompt

console = Console()

# Base Component
class Beverage:
    def get_description(self):
        return "Unknown Beverage"

    def cost(self):
        return 0

# Concrete Components
class Coffee(Beverage):
    def get_description(self):
        return "Coffee"

    def cost(self):
        return 5

class Tea(Beverage):
    def get_description(self):
        return "Tea"

    def cost(self):
        return 4

# Decorator
class BeverageDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description()

    def cost(self):
        return self.beverage.cost()

# Concrete Decorators
class Milk(BeverageDecorator):
    def get_description(self):
        return self.beverage.get_description() + ", Milk"

    def cost(self):
        return self.beverage.cost() + 1

class Sugar(BeverageDecorator):
    def get_description(self):
        return self.beverage.get_description() + ", Sugar"

    def cost(self):
        return self.beverage.cost() + 0.5

class Chocolate(BeverageDecorator):
    def get_description(self):
        return self.beverage.get_description() + ", Chocolate"

    def cost(self):
        return self.beverage.cost() + 2

class WhippedCream(BeverageDecorator):
    def get_description(self):
        return self.beverage.get_description() + ", Whipped Cream"

    def cost(self):
        return self.beverage.cost() + 2.5

def run_game():
    console.print("[bold cyan]Decorator Pattern - Coffee Customizer[/bold cyan]\n")

    # Choose base drink
    console.print("Select a base beverage:")
    console.print("1. Coffee")
    console.print("2. Tea")
    base_choice = Prompt.ask("Enter choice", choices=["1","2"])

    beverage = Coffee() if base_choice == "1" else Tea()

    while True:
        console.print("\nCurrent beverage: [bold yellow]" + beverage.get_description() + f"[/bold yellow]")
        console.print("Current cost: [bold green]" + str(beverage.cost()) + "$[/bold green]\n")

        console.print("Add Decorator:")
        console.print("1. Milk (+$1)")
        console.print("2. Sugar (+$0.5)")
        console.print("3. Chocolate (+$2)")
        console.print("4. Whipped Cream (+$2.5)")
        console.print("0. Finish")

        choice = Prompt.ask("Choose decorator", choices=["0","1","2","3","4"])

        if choice == "0":
            console.print("\n☕ Final Beverage: [bold yellow]" + beverage.get_description() + f"[/bold yellow]")
            console.print("💰 Total Cost: [bold green]" + str(beverage.cost()) + "$[/bold green]\n")
            console.print("👋 Enjoy your drink!\n")
            break
        elif choice == "1":
            beverage = Milk(beverage)
        elif choice == "2":
            beverage = Sugar(beverage)
        elif choice == "3":
            beverage = Chocolate(beverage)
        elif choice == "4":
            beverage = WhippedCream(beverage)
