from rich.console import Console
from rich.table import Table
from rich.syntax import Syntax
import time

console = Console()

def run_deepdive():
    console.print("[bold cyan]=== Builder Pattern Deep Dive ===[/bold cyan]\n")

    console.print("The [bold yellow]Builder Pattern[/bold yellow] separates the construction of a complex object "
                  "from its representation so the same construction process can create different representations.\n")

    # Step 1: Class roles
    time.sleep(0.5)
    table = Table(title="👷 Builder Pattern Class Roles", show_lines=True)
    table.add_column("Component", justify="center", style="bold cyan")
    table.add_column("Description", style="white")

    table.add_row("Product", "The complex object that is being built (e.g., Burger).")
    table.add_row("Builder", "Specifies an abstract interface for creating the parts of the Product.")
    table.add_row("ConcreteBuilder", "Implements the Builder interface and assembles parts (e.g., BurgerBuilder).")
    table.add_row("Director", "Constructs the object using the Builder interface in a particular sequence.")
    console.print(table)
    time.sleep(1)

    # Step 2: Code example
    console.print("\n[bold magenta]Example Code Snippet[/bold magenta]\n")
    code = """class Burger:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def add_bun(self):
        self.burger.add_part("Bun")

    def add_patty(self):
        self.burger.add_part("Patty")

    def get_burger(self):
        return self.burger

class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.add_bun()
        self.builder.add_patty()
        return self.builder.get_burger()

# Client
builder = BurgerBuilder()
director = Director(builder)
burger = director.construct()
print(burger.parts)  # ['Bun', 'Patty']
"""
    syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
    console.print(syntax)
    time.sleep(1)

    # Step 3: When to use
    console.print("\n[bold magenta]🧠 When to Use the Builder Pattern[/bold magenta]")
    console.print("""
- When object creation is complex and involves multiple steps.
- When different representations of the same object are needed.
- When you want to separate construction logic from the final product.
    """)

    # Step 4: Summary
    console.print("[bold yellow]\nTL;DR Summary[/bold yellow]")
    console.print("""
Director = controls the process 🔧
Builder = defines the steps 🧩
Product = the final result 🍔

→ The same construction process can make different objects by swapping builders!
    """)

    console.print("\n[italic green]You've mastered the Builder pattern inside and out![/italic green] ✅\n")
