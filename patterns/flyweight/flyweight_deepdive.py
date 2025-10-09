from rich.console import Console

console = Console()

def run_deepdive():
    console.print("[bold magenta]Flyweight Pattern Deep Dive[/bold magenta]\n")

    console.print(
        "The [bold cyan]Flyweight Pattern[/bold cyan] reduces memory usage by sharing objects with "
        "common intrinsic state.\n"
    )

    console.print("[bold yellow]Mapping in Game:[/bold yellow]")
    console.print("- [green]Flyweight objects:[/green] Human instances (weight, name)")
    console.print("- [green]Extrinsic state:[/green] Photo referencing human (weight 0.5 kg)")
    console.print("- [green]Factory:[/green] HumanFactory manages shared human objects")
    console.print("- [green]Client:[/green] Creates photos pointing to humans\n")

    console.print("[bold green]Benefits:[/bold green]")
    console.print("- ✅ Significantly reduces memory/weight when many representations exist")
    console.print("- ✅ Separates intrinsic (shared) vs extrinsic (unique) state")
    console.print("- ✅ Demonstrates object reuse clearly and intuitively\n")

    console.print("[bold blue]Educational Insights:[/bold blue]")
    console.print("- Creating new humans adds full weight (50 kg)")
    console.print("- Taking photos adds minimal weight (0.5 kg)")
    console.print("- Total weight shows tangible effect of object sharing")
