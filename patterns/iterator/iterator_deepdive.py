from rich.console import Console

console = Console()

def run_deepdive():
    console.print("[bold magenta]Iterator Pattern Deep Dive[/bold magenta]\n")

    console.print(
        "The [bold cyan]Iterator Pattern[/bold cyan] provides a way to access elements "
        "of a collection sequentially without exposing its underlying representation.\n"
    )

    console.print("[bold yellow]Mapping in Game:[/bold yellow]")
    console.print("- [green]Collection:[/green] TreasureChest (holds items)")
    console.print("- [green]Iterator:[/green] TreasureIterator (traverses items sequentially)")
    console.print("- [green]Client:[/green] Player exploring the chest\n")

    console.print("[bold green]Key Insights:[/bold green]")
    console.print("- ✅ Separates traversal logic from the collection")
    console.print("- ✅ Can traverse without exposing internal structure")
    console.print("- ✅ Supports multiple ways of iteration if needed\n")

    console.print("[bold blue]Educational Insights:[/bold blue]")
    console.print("- Player inspects items one by one")
    console.print("- Reinforces idea of accessing elements without knowing internal storage")
    console.print("- Demonstrates clean separation of concerns between collection and iterator")
