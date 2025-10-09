from rich.console import Console

console = Console()

def run_deepdive():
    console.print("[bold magenta]Decorator Pattern Deep Dive[/bold magenta]\n")

    console.print(
        "The [bold cyan]Decorator Pattern[/bold cyan] allows behavior to be added to individual objects, "
        "dynamically, without affecting other objects of the same class.\n"
    )

    console.print("[bold yellow]Example Mapping in Game:[/bold yellow]")
    console.print("- [green]Coffee / Tea[/green]: Base Component")
    console.print("- [green]Milk, Sugar, Chocolate, Whipped Cream[/green]: Decorators")
    console.print("- [green]BeverageDecorator[/green]: Abstract Decorator\n")

    console.print("[bold green]Benefits:[/bold green]")
    console.print("- ✅ Add responsibilities dynamically at runtime")
    console.print("- ✅ Avoids creating many subclasses for every combination")
    console.print("- ✅ Flexible and reusable\n")

    console.print("[bold blue]Try experimenting:[/bold blue]")
    console.print("- Add multiple decorators to a base beverage")
    console.print("- Observe how description and cost update dynamically")
    console.print("- Notice how the base object remains unchanged while decorators wrap it")
