from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

console = Console()

# Products
class Pizza:
    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = price

class Margherita(Pizza):
    def __init__(self):
        super().__init__("Margherita", ["Tomato Sauce", "Mozzarella", "Basil"], 8)

class Pepperoni(Pizza):
    def __init__(self):
        super().__init__("Pepperoni", ["Tomato Sauce", "Mozzarella", "Pepperoni"], 10)

class Veggie(Pizza):
    def __init__(self):
        super().__init__("Veggie", ["Tomato Sauce", "Mozzarella", "Bell Peppers", "Olives", "Onions"], 9)

class Hawaiian(Pizza):
    def __init__(self):
        super().__init__("Hawaiian", ["Tomato Sauce", "Mozzarella", "Ham", "Pineapple"], 11)

# Factory
class PizzaFactory:
    def create_pizza(self, pizza_type):
        if pizza_type == "Margherita":
            return Margherita()
        elif pizza_type == "Pepperoni":
            return Pepperoni()
        elif pizza_type == "Veggie":
            return Veggie()
        elif pizza_type == "Hawaiian":
            return Hawaiian()
        else:
            return None

# Game function
def run_game():
    console.print("[bold cyan]Factory Pattern - Pizza Factory[/bold cyan]\n")

    factory = PizzaFactory()
    ordered_pizzas = []

    while True:
        console.print("\nPizza Menu:")
        console.print("1. Margherita ($8)")
        console.print("2. Pepperoni ($10)")
        console.print("3. Veggie ($9)")
        console.print("4. Hawaiian ($11)")
        console.print("0. Exit")

        choice = Prompt.ask("Choose pizza to order", choices=["0","1","2","3","4"])

        if choice == "0":
            console.print("\n👋 Exiting Pizza Factory...\n")
            break
        else:
            pizza_map = {"1": "Margherita", "2": "Pepperoni", "3": "Veggie", "4": "Hawaiian"}
            pizza_type = pizza_map[choice]
            pizza = factory.create_pizza(pizza_type)
            ordered_pizzas.append(pizza)

            console.print(f"\n[green]You ordered: {pizza.name}![/green]")
            console.print("[bold yellow]Ingredients:[/bold yellow] " + ", ".join(pizza.ingredients))
            console.print(f"[bold cyan]Price:[/bold cyan] ${pizza.price}\n")

            # Display recent orders (last 5)
            table = Table(title="Recent Pizza Orders")
            table.add_column("No.", justify="center")
            table.add_column("Pizza", justify="center")
            table.add_column("Price", justify="center")
            recent = ordered_pizzas[-5:]
            for i, p in enumerate(recent, start=len(ordered_pizzas)-len(recent)+1):
                table.add_row(str(i), p.name, f"${p.price}")
            console.print(table)
