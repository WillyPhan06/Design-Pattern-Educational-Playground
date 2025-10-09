from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text
from rich.progress import track
import time

console = Console()

# Template Class
class Drink:
    def prepare(self):
        self.take_cup()
        self.wash_cup()
        self.add_ingredients()
        self.assemble()
        self.serve()

    # Common steps (yellow)
    def take_cup(self):
        console.print(Text("Taking out cup", style="yellow"))
        time.sleep(0.5)

    def wash_cup(self):
        console.print(Text("Washing cup", style="yellow"))
        time.sleep(0.5)

    # Steps that vary per drink (green)
    def add_ingredients(self):
        raise NotImplementedError

    def assemble(self):
        raise NotImplementedError

    # Common step (yellow)
    def serve(self):
        console.print(Text("Serving the drink", style="yellow"))
        time.sleep(0.5)

# Concrete Drinks
class Tea(Drink):
    def add_ingredients(self):
        console.print(Text("Adding tea leaves and hot water", style="green"))
        time.sleep(0.5)

    def assemble(self):
        console.print(Text("Steeping tea and stirring", style="green"))
        for _ in track(range(20), description="Brewing tea..."):
            time.sleep(0.03)

class Coffee(Drink):
    def add_ingredients(self):
        console.print(Text("Adding ground coffee and hot water", style="green"))
        time.sleep(0.5)

    def assemble(self):
        console.print(Text("Brewing coffee and pouring", style="green"))
        for _ in track(range(20), description="Brewing coffee..."):
            time.sleep(0.03)

class Juice(Drink):
    def add_ingredients(self):
        console.print(Text("Adding fresh fruit", style="green"))
        time.sleep(0.5)

    def assemble(self):
        console.print(Text("Squeezing and mixing juice", style="green"))
        for _ in track(range(20), description="Mixing juice..."):
            time.sleep(0.03)

# Game function
def run_game():
    console.print("[bold cyan]Template Method Pattern - Drinks Preparation Simulator[/bold cyan]\n")

    drinks = {
        "Tea": Tea(),
        "Coffee": Coffee(),
        "Juice": Juice()
    }

    while True:
        console.print("\nActions:")
        for i, name in enumerate(drinks.keys(), 1):
            console.print(f"{i}. Prepare {name}")
        console.print("0. Exit")

        choice = Prompt.ask("Choose action", choices=[str(i) for i in range(len(drinks)+1)])

        if choice == "0":
            console.print("\n👋 Exiting Drinks Preparation Simulator...\n")
            break

        else:
            drink_name = list(drinks.keys())[int(choice)-1]
            console.print(f"\n🍹 You chose to prepare {drink_name}!\n")
            drinks[drink_name].prepare()
