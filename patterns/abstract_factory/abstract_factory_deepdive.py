# patterns/abstract_factory/abstract_factory_deepdive.py
from rich.console import Console
from rich.panel import Panel
from time import sleep

console = Console()

def run_deepdive():
    console.print("[bold magenta]Abstract Factory - Deep Dive[/bold magenta]\n")

    console.print(Panel.fit("Goal: Create families of related objects without specifying their concrete classes."))

    console.print("Step 1: Choose a family (Modern or Victorian)...")
    sleep(1)
    console.print("[green]Family selected![/green]\n")

    console.print("Step 2: Create a Chair and Sofa from the selected family...")
    sleep(1)
    console.print("[green]Objects created successfully![/green]\n")

    console.print("Step 3: Attempt to mix objects from different families...")
    sleep(1)
    console.print("[red]Warning! Chair and Sofa belong to different families![/red]\n")

    console.print("Step 4: Access objects via abstract interfaces...")
    sleep(1)
    console.print("[cyan]Creation logic remains independent of concrete classes![/cyan]\n")

    console.print("[bold yellow]Key takeaway:[/bold yellow] Abstract Factory ensures family consistency and decouples client code from concrete classes.\n")
