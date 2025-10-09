from rich.console import Console

console = Console()

def run_deepdive():
    console.print("[bold magenta]Factory Pattern Deep Dive - Pizza Version[/bold magenta]\n")

    console.print(
        "The [bold cyan]Factory Pattern[/bold cyan] defines an interface for creating objects, "
        "but lets the subclass (or factory) decide which concrete class to instantiate. "
        "It encapsulates object creation, keeping client code simple.\n"
    )

    console.print("[bold yellow]Mapping in Game:[/bold yellow]")
    console.print("- [green]Factory:[/green] PizzaFactory (decides which Pizza to create)")
    console.print("- [green]Products:[/green] Margherita, Pepperoni, Veggie, Hawaiian (different pizza types)")
    console.print("- [green]Client:[/green] Player ordering a pizza\n")

    console.print("[bold green]Key Insights:[/bold green]")
    console.print("- ✅ Centralizes creation logic in one place (PizzaFactory)")
    console.print("- ✅ Player doesn’t need to know internal details (ingredients, price)")
    console.print("- ✅ Adding new pizzas is easy and does not affect existing code\n")

    console.print("[bold blue]Educational Insights:[/bold blue]")
    console.print("- Player sees a single interface (order pizza) producing multiple objects")
    console.print("- Demonstrates loose coupling: player doesn’t care how pizza is made")
    console.print("- Reinforces concept of scalable and maintainable object creation")
