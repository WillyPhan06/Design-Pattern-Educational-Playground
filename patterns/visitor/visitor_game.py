from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import time

console = Console()

# Visitor base class
class Visitor:
    def visit_painting(self, painting):
        raise NotImplementedError

    def visit_sculpture(self, sculpture):
        raise NotImplementedError

    def visit_artifact(self, artifact):
        raise NotImplementedError

# Concrete Visitors
class ValuationVisitor(Visitor):
    def visit_painting(self, painting):
        console.print(f"[green]Valuing painting '{painting.name}' → ${painting.value * 1.2}k[/green]")

    def visit_sculpture(self, sculpture):
        console.print(f"[green]Valuing sculpture '{sculpture.name}' → ${sculpture.value * 1.5}k[/green]")

    def visit_artifact(self, artifact):
        console.print(f"[green]Valuing artifact '{artifact.name}' → ${artifact.value * 2}k[/green]")

class RestorationVisitor(Visitor):
    def visit_painting(self, painting):
        console.print(f"[cyan]Restoring painting '{painting.name}'... done![/cyan]")

    def visit_sculpture(self, sculpture):
        console.print(f"[cyan]Polishing sculpture '{sculpture.name}'... done![/cyan]")

    def visit_artifact(self, artifact):
        console.print(f"[cyan]Cleaning artifact '{artifact.name}'... done![/cyan]")

class SecurityVisitor(Visitor):
    def visit_painting(self, painting):
        console.print(f"[yellow]Inspecting security for painting '{painting.name}'... secure[/yellow]")

    def visit_sculpture(self, sculpture):
        console.print(f"[yellow]Inspecting security for sculpture '{sculpture.name}'... secure[/yellow]")

    def visit_artifact(self, artifact):
        console.print(f"[yellow]Inspecting security for artifact '{artifact.name}'... secure[/yellow]")

# Elements
class Painting:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def accept(self, visitor):
        visitor.visit_painting(self)

class Sculpture:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def accept(self, visitor):
        visitor.visit_sculpture(self)

class Artifact:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def accept(self, visitor):
        visitor.visit_artifact(self)

# Game function
def run_game():
    console.print("[bold cyan]Visitor Pattern - Museum Exhibit Inspector[/bold cyan]\n")

    # Museum exhibits
    exhibits = [
        Painting("Starry Night", 100),
        Sculpture("The Thinker", 200),
        Artifact("Ancient Vase", 50)
    ]

    visitors = {
        "Valuation": ValuationVisitor(),
        "Restoration": RestorationVisitor(),
        "Security": SecurityVisitor()
    }

    while True:
        console.print("\nActions:")
        for i, name in enumerate(visitors.keys(), 1):
            console.print(f"{i}. Apply {name} Visitor")
        console.print("0. Exit")

        choice = Prompt.ask("Choose action", choices=[str(i) for i in range(len(visitors)+1)])

        if choice == "0":
            console.print("\n👋 Exiting Museum Exhibit Inspector...\n")
            break
        else:
            visitor_name = list(visitors.keys())[int(choice)-1]
            visitor = visitors[visitor_name]
            console.print(f"\nApplying [bold]{visitor_name} Visitor[/bold] to all exhibits...\n")
            for exhibit in exhibits:
                time.sleep(0.5)
                exhibit.accept(visitor)
