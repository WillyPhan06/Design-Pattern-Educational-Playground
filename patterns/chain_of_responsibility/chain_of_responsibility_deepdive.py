from rich.console import Console

console = Console()

def run_deepdive():
    console.print("[bold magenta]Chain of Responsibility Pattern Deep Dive[/bold magenta]\n")

    console.print(
        "The [bold cyan]Chain of Responsibility Pattern[/bold cyan] allows a request to pass along a chain "
        "of handlers until one of them handles it. This decouples the sender and the receiver.\n"
    )

    console.print("[bold yellow]Mapping in Game:[/bold yellow]")
    console.print("- [green]Handlers:[/green] Level 1, Level 2, Manager support")
    console.print("- [green]Request:[/green] Support ticket submitted by player")
    console.print("- [green]Chain:[/green] Tickets pass through handlers until one can handle\n")

    console.print("[bold green]Benefits:[/bold green]")
    console.print("- ✅ Decouples sender (player) from receivers (support levels)")
    console.print("- ✅ Flexible addition/removal of handlers")
    console.print("- ✅ Each handler focuses on what it can process\n")

    console.print("[bold blue]Educational Insights:[/bold blue]")
    console.print("- Tickets are processed in order")
    console.print("- Handlers decide if they can handle the request")
    console.print("- Demonstrates dynamic request handling using a chain")
