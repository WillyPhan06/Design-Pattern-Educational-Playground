from rich.console import Console

console = Console()

def run_deepdive():
    console.print("[bold magenta]Visitor Pattern Deep Dive[/bold magenta]\n")

    console.print(
        "The [bold cyan]Visitor Pattern[/bold cyan] lets you define a new operation on a set of objects "
        "without changing the classes of those objects.\n"
    )

    console.print("[bold yellow]Mapping in Game:[/bold yellow]")
    console.print("- [green]Elements:[/green] Painting, Sculpture, Artifact (objects in museum)")
    console.print("- [green]Visitors:[/green] Valuation, Restoration, Security (new operations)")
    console.print("- [green]Client:[/green] Player choosing which visitor to apply\n")

    console.print("[bold green]Key Insights:[/bold green]")
    console.print("- ✅ Add new operations without modifying existing element classes")
    console.print("- ✅ Demonstrates separation of data (elements) and behavior (visitors)")
    console.print("- ✅ Supports multiple distinct operations on the same set of elements\n")

    console.print("[bold blue]Educational Insights:[/bold blue]")
    console.print("- Player sees same exhibits reacting differently depending on visitor")
    console.print("- Reinforces decoupling: elements know nothing about visitors’ logic")
    console.print("- Perfect for demonstrating extensibility in large systems")
