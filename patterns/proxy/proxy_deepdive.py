from rich.console import Console

console = Console()

def run_deepdive():
    console.print("[bold magenta]Proxy Pattern Deep Dive[/bold magenta]\n")

    console.print(
        "The [bold cyan]Proxy Pattern[/bold cyan] provides a surrogate or placeholder for another object to control access, "
        "add functionality, or delay expensive operations.\n"
    )

    console.print("[bold yellow]Mapping in Game:[/bold yellow]")
    console.print("- [green]Real Subject:[/green] BankVault (actual vault contents)")
    console.print("- [green]Proxy:[/green] VaultProxy controlling access")
    console.print("- [green]Client:[/green] Player trying to access the vault\n")

    console.print("[bold green]Benefits:[/bold green]")
    console.print("- ✅ Controls access to sensitive resources")
    console.print("- ✅ Adds security, logging, or lazy initialization")
    console.print("- ✅ Hides complexity from client\n")

    console.print("[bold blue]Educational Insights:[/bold blue]")
    console.print("- Only authorized users can access the vault")
    console.print("- Proxy keeps track of failed attempts")
    console.print("- Demonstrates real-world security use of Proxy Pattern")
