from rich.console import Console

console = Console()

def run_deepdive():
    console.print("[bold magenta]Strategy Pattern Deep Dive[/bold magenta]\n")

    console.print(
        "The [bold cyan]Strategy Pattern[/bold cyan] defines a family of algorithms, encapsulates each one, "
        "and makes them interchangeable. This allows the algorithm to vary independently from clients that use it.\n"
    )

    console.print("[bold yellow]Mapping in Game:[/bold yellow]")
    console.print("- [green]Context:[/green] Soldier executing commands in battle")
    console.print("- [green]Strategies:[/green] Attack or Defend, implemented differently per soldier type")
    console.print("- [green]Client:[/green] Player issuing the command\n")

    console.print("[bold green]Benefits:[/bold green]")
    console.print("- ✅ Change behavior dynamically at runtime")
    console.print("- ✅ Reuse same interface for different algorithms")
    console.print("- ✅ Clear separation of concerns between context and strategy\n")

    console.print("[bold blue]Educational Insights:[/bold blue]")
    console.print("- Same command produces different outcomes based on soldier strategy")
    console.print("- Demonstrates flexibility and maintainability in software design")
    console.print("- Illustrates real-world analogy: different types of agents following the same orders but acting according to their specialty")
