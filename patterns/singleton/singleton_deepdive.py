from rich.console import Console
from rich.panel import Panel
from time import sleep

console = Console()

def run_deepdive():
    console.print("[bold magenta]Singleton - Deep Dive[/bold magenta]\n")
    
    console.print(Panel.fit("Goal: Only one instance of a class can exist.\nAccess it globally."))
    
    console.print("Step 1: User tries to create the first instance...")
    sleep(1)
    console.print("[green]Instance created successfully![/green]\n")
    
    console.print("Step 2: User tries to create a second instance...")
    sleep(1)
    console.print("[red]Creation blocked! This is the same existing instance.[/red]\n")
    
    console.print("Step 3: Accessing the singleton instance again anywhere...")
    sleep(1)
    console.print("[cyan]Always returns the same object![/cyan]\n")
    
    console.print("[bold yellow]Key takeaway:[/bold yellow] Singleton ensures a single instance and global access.\n")
