from rich.console import Console

console = Console()

def run_deepdive():
    console.print("[bold magenta]State Pattern Deep Dive[/bold magenta]\n")

    console.print(
        "The [bold cyan]State Pattern[/bold cyan] allows an object to alter its behavior "
        "when its internal state changes. The object appears to change its class.\n"
    )

    console.print("[bold yellow]Mapping in Game:[/bold yellow]")
    console.print("- [green]Context:[/green] TrafficLight (object whose behavior changes)")
    console.print("- [green]States:[/green] RedState, YellowState, GreenState (different behaviors)")
    console.print("- [green]Client:[/green] Player interacting with the traffic light\n")

    console.print("[bold green]Key Insights:[/bold green]")
    console.print("- ✅ Behavior changes dynamically with state")
    console.print("- ✅ Avoids large conditional statements")
    console.print("- ✅ Encapsulates state-specific logic in separate classes\n")

    console.print("[bold blue]Educational Insights:[/bold blue]")
    console.print("- Player sees immediate effect of switching states")
    console.print("- Reinforces understanding of state-dependent behavior")
    console.print("- Great for modeling real-world objects with different operational modes")
