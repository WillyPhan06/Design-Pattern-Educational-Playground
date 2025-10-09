from rich.console import Console

console = Console()

def run_deepdive():
    console.print("[bold magenta]Facade Pattern Deep Dive[/bold magenta]\n")

    console.print(
        "The [bold cyan]Facade Pattern[/bold cyan] provides a simplified interface to a complex subsystem.\n"
    )

    console.print("[bold yellow]Mapping in Game:[/bold yellow]")
    console.print("- [green]Subsystems:[/green] CPU, GPU, RAM, HardDrive, Network")
    console.print("- [green]Facade:[/green] Computer class providing start(), shutdown()")
    console.print("- [green]Internals:[/green] Direct subsystem interaction for advanced exploration\n")

    console.print("[bold green]Benefits:[/bold green]")
    console.print("- ✅ Simplifies usage of complex systems with a single interface")
    console.print("- ✅ Reduces coupling between client and subsystems")
    console.print("- ✅ Allows optional advanced interaction for deeper understanding\n")

    console.print("[bold blue]Educational Insights:[/bold blue]")
    console.print("- Using [cyan]Facade[/cyan] you hide complexity while providing ease of use")
    console.print("- Directly interacting with subsystems shows the inner workings")
    console.print("- Combining both illustrates the power of abstraction and separation of concerns\n")

    console.print("[bold green]Try experimenting:[/bold green]")
    console.print("- Start the computer via facade, then open internals to see individual subsystems")
    console.print("- Shutdown via facade vs. manually shutting subsystems")
    console.print("- Observe the effect of abstraction and encapsulation in practice")
