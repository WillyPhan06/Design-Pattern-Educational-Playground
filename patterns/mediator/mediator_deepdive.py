from rich.console import Console

console = Console()

def run_deepdive():
    console.print("[bold magenta]Mediator Pattern Deep Dive[/bold magenta]\n")

    console.print(
        "The [bold cyan]Mediator Pattern[/bold cyan] defines an object that encapsulates "
        "how a set of objects interact. It promotes loose coupling by preventing "
        "objects from referring to each other explicitly.\n"
    )

    console.print("[bold yellow]Mapping in Game:[/bold yellow]")
    console.print("- [green]Mediator:[/green] ChatRoom (central hub for messages)")
    console.print("- [green]Colleagues:[/green] Alice, Bob, Charlie (users sending messages)")
    console.print("- [green]Client:[/green] Player sending messages\n")

    console.print("[bold green]Key Insights:[/bold green]")
    console.print("- ✅ All communication goes through a central mediator")
    console.print("- ✅ Users do not need to know about each other directly")
    console.print("- ✅ Makes adding new users easier without changing others\n")

    console.print("[bold blue]Educational Insights:[/bold blue]")
    console.print("- Player sees messages delivered automatically via mediator")
    console.print("- Reinforces loose coupling and centralized control")
    console.print("- Great for understanding real-world messaging systems")
