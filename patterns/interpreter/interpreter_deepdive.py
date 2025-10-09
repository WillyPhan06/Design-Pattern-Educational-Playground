from rich.console import Console

console = Console()

def run_deepdive():
    console.print("[bold magenta]Interpreter Pattern Deep Dive[/bold magenta]\n")

    console.print(
        "The [bold cyan]Interpreter Pattern[/bold cyan] defines a representation of a grammar "
        "for a language and provides an interpreter to evaluate sentences in that language.\n"
    )

    console.print("[bold yellow]Mapping in Game:[/bold yellow]")
    console.print("- [green]Abstract Expression:[/green] Expression (interface with interpret method)")
    console.print("- [green]Terminal Expression:[/green] Number (represents numbers)")
    console.print("- [green]Non-terminal Expression:[/green] Add, Subtract, Multiply, Divide (operators)")
    console.print("- [green]Client:[/green] Player entering arithmetic expressions\n")

    console.print("[bold green]Key Insights:[/bold green]")
    console.print("- ✅ Grammar is represented by classes (expressions)")
    console.print("- ✅ Interpreter evaluates input based on this grammar")
    console.print("- ✅ Supports easy extension for new operations\n")

    console.print("[bold blue]Educational Insights:[/bold blue]")
    console.print("- Player types arithmetic expressions and sees step-by-step evaluation")
    console.print("- Reinforces the concept of parsing and interpreting structured input")
    console.print("- Clearly demonstrates terminal vs non-terminal expressions")
