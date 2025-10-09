from rich.console import Console
from rich.prompt import Prompt
from rich.progress import track
import time, random

console = Console()

# -------------------------------
# Product
# -------------------------------
class Burger:
    def __init__(self):
        self.bun = None
        self.patty = None
        self.cheese = None
        self.toppings = []
        self.sauce = None

    def __str__(self):
        toppings_str = ", ".join(self.toppings) if self.toppings else "None"
        return (
            f"[bold yellow]🍔 Final Burger:[/bold yellow]\n"
            f"Bun: {self.bun}\n"
            f"Patty: {self.patty}\n"
            f"Cheese: {self.cheese}\n"
            f"Toppings: {toppings_str}\n"
            f"Sauce: {self.sauce}"
        )

# -------------------------------
# Builder
# -------------------------------
class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def add_bun(self, bun):
        console.print(f"[cyan][Builder][/cyan] Toasting {bun} bun... 🔥")
        time.sleep(1)
        console.print("[green]Done! ✅[/green]")
        self.burger.bun = bun

    def add_patty(self, patty):
        console.print(f"[cyan][Builder][/cyan] Grilling {patty} patty... 🍳")
        time.sleep(1.2)
        console.print("[green]Patty ready! ✅[/green]")
        self.burger.patty = patty

    def add_cheese(self, cheese):
        if cheese != "None":
            console.print(f"[cyan][Builder][/cyan] Melting {cheese} cheese... 🧀")
            time.sleep(0.8)
            console.print("[green]Cheese added! ✅[/green]")
        else:
            console.print("[yellow]Skipping cheese.[/yellow]")
        self.burger.cheese = cheese

    def add_toppings(self, toppings):
        for topping in toppings:
            console.print(f"[cyan][Builder][/cyan] Adding {topping}... 🥬")
            time.sleep(0.5)
        self.burger.toppings = toppings
        console.print("[green]All toppings added! ✅[/green]")

    def add_sauce(self, sauce):
        console.print(f"[cyan][Builder][/cyan] Spreading {sauce} sauce... 🍶")
        time.sleep(0.7)
        console.print("[green]Sauce ready! ✅[/green]")
        self.burger.sauce = sauce

    def get_burger(self):
        return self.burger

# -------------------------------
# Director
# -------------------------------
class BurgerDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        console.print("[magenta][Director][/magenta] Assembling your burger... 🍳")
        for _ in track(range(3), description="[bold cyan]Wrapping up your burger... 🎁"):
            time.sleep(0.7)
        console.print("[green][Director][/green] Burger ready to serve!\n")

# -------------------------------
# Interactive Game
# -------------------------------
def run_game():
    console.print("[bold cyan]=== Builder Pattern - Burger Builder Game ===[/bold cyan]\n")
    console.print("Welcome to the [bold yellow]Burger Builder[/bold yellow]! 🍔 Let's build your burger step by step.\n")

    builder = BurgerBuilder()
    director = BurgerDirector(builder)

    # Step 1: Bun
    buns = ["Sesame", "Brioche", "Whole Wheat"]
    bun_choice = Prompt.ask("Choose your bun", choices=buns)
    builder.add_bun(bun_choice)

    # Step 2: Patty
    patties = ["Beef", "Chicken", "Veggie"]
    patty_choice = Prompt.ask("Choose your patty", choices=patties)
    builder.add_patty(patty_choice)

    # Step 3: Cheese
    cheeses = ["Cheddar", "Swiss", "None"]
    cheese_choice = Prompt.ask("Choose your cheese", choices=cheeses)
    builder.add_cheese(cheese_choice)

    # Step 4: Toppings
    toppings = ["Lettuce", "Tomato", "Onion", "Bacon"]
    console.print("\nPick your toppings (type separated by commas, e.g. Lettuce,Tomato):")
    topping_input = input("Toppings: ").strip()
    topping_list = [t.strip().capitalize() for t in topping_input.split(",") if t.strip()]
    valid_toppings = [t for t in topping_list if t in toppings]
    builder.add_toppings(valid_toppings)

    # Step 5: Sauce
    sauces = ["Ketchup", "Mayo", "Special"]
    sauce_choice = Prompt.ask("Choose your sauce", choices=sauces)
    builder.add_sauce(sauce_choice)

    # Director constructs
    director.construct()

    # Final burger
    burger = builder.get_burger()
    console.print(str(burger))
    rating = round(random.uniform(7.0, 10.0), 1)
    console.print(f"\n⭐ [bold green]Customer satisfaction:[/bold green] {rating}/10")

    console.print("\n[italic cyan]You just learned the Builder Pattern![/italic cyan] 🎉")

