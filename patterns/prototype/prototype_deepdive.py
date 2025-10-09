from rich.console import Console
from rich.table import Table
from rich.syntax import Syntax
import time

console = Console()

def run_deepdive():
    console.print("[bold magenta]🧬 Prototype Pattern — Deep Dive[/bold magenta]\n")
    console.print("The Prototype pattern lets you create new objects by copying a prototype instance.\n"
                  "It's useful when creating a new object is expensive or complex.\n")

    # Show roles in table
    table = Table(title="Prototype Pattern - Roles", show_lines=True)
    table.add_column("Role", style="bold cyan")
    table.add_column("Description", style="white")
    table.add_row("Prototype", "An object that can clone itself (provides clone method).")
    table.add_row("Client", "Asks the prototype to clone itself and may mutate the clone.")
    table.add_row("Concrete Prototype", "A concrete instance used as a template (e.g., Worker, Soldier).")
    console.print(table)
    time.sleep(0.8)

    console.print("\n[bold magenta]Minimal Example (Python)[/bold magenta]\n")
    code = '''import copy

class Prototype:
    def __init__(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)

# client code
p = Prototype(42)
p2 = p.clone()
p2.value = 99
print(p.value, p2.value)  # 42 99'''
    console.print(Syntax(code, "python", theme="monokai", line_numbers=True))
    time.sleep(0.8)

    console.print("\n[bold yellow]When to use Prototype[/bold yellow]")
    console.print("""
- When object creation is expensive and you prefer copying to building.
- When you need many similar objects that start from a common template.
- When you want to decouple object creation from specific classes.
    """)

    console.print("\n[bold green]TL;DR:[/bold green] Prototype = clone + tweak. Use a template object to create new instances quickly.\n")
