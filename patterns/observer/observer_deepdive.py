from rich.console import Console

console = Console()

def run_deepdive():
    console.print("[bold magenta]Observer Pattern Deep Dive[/bold magenta]\n")

    console.print(
        "The [bold cyan]Observer Pattern[/bold cyan] defines a one-to-many dependency "
        "between objects. When the subject (WeatherData) changes state, "
        "all registered observers are notified and updated automatically.\n"
    )

    console.print("[bold yellow]Mapping in Game:[/bold yellow]")
    console.print("- [green]Subject:[/green] WeatherData (the weather station)")
    console.print("- [green]Observers:[/green] PhoneDisplay, WebDisplay, TVDisplay (different displays)")
    console.print("- [green]Client:[/green] Player triggering weather updates\n")

    console.print("[bold green]Key Insights:[/bold green]")
    console.print("- ✅ Decouples subject from observers")
    console.print("- ✅ Any number of observers can register/unregister")
    console.print("- ✅ Observers update automatically on state change\n")

    console.print("[bold blue]Educational Insights:[/bold blue]")
    console.print("- Player sees multiple observers receiving updates instantly")
    console.print("- Reinforces understanding of one-to-many dependencies")
    console.print("- Great for modeling real-world notification systems")
