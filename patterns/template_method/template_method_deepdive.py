from rich.console import Console

console = Console()

def run_deepdive():
    console.print("[bold magenta]Template Method Pattern Deep Dive[/bold magenta]\n")

    console.print(
        "The [bold cyan]Template Method Pattern[/bold cyan] defines the skeleton of an algorithm in a method, "
        "deferring some steps to subclasses. Subclasses redefine certain steps without changing the overall structure.\n"
    )

    console.print("[bold yellow]Mapping in Game:[/bold yellow]")
    console.print("- [green]Template:[/green] Drink.prepare() defines skeleton: take cup -> wash cup -> add ingredients -> assemble -> serve")
    console.print("- [green]Concrete Drinks:[/green] Tea, Coffee, Juice implement specific steps for add_ingredients and assemble")
    console.print("- [green]Client:[/green] Player choosing which drink to prepare\n")

    console.print("[bold green]Visual Highlight:[/bold green]")
    console.print("- [yellow]Yellow steps:[/yellow] common steps shared by all drinks")
    console.print("- [green]Green steps:[/green] variant steps unique per drink\n")

    console.print("[bold blue]Educational Insights:[/bold blue]")
    console.print("- Skeleton method calls all steps in order")
    console.print("- Subclasses redefine specific steps without altering overall flow")
    console.print("- Demonstrates separation of invariant (yellow) and variant (green) parts of an algorithm")
