from rich.console import Console

console = Console()

def run_deepdive():
    console.print("[bold magenta]Bridge Pattern Deep Dive[/bold magenta]\n")

    console.print(
        "The [bold cyan]Bridge Pattern[/bold cyan] decouples abstraction from implementation "
        "so that both can evolve independently.\n"
    )

    console.print("[bold yellow]Example Mapping:[/bold yellow]")
    console.print("- Abstraction: RemoteControl")
    console.print("- Refined Abstraction: AdvancedRemoteControl")
    console.print("- Implementor Interface: Device")
    console.print("- Concrete Implementors: TV, Radio\n")

    console.print("[bold green]Without Bridge Pattern:[/bold green]")
    console.print(
        "We'd need separate remotes for every device type, e.g., TVRemote, TVAdvancedRemote, "
        "RadioRemote, RadioAdvancedRemote... This leads to class explosion.\n"
    )

    console.print("[bold green]With Bridge Pattern:[/bold green]")
    console.print(
        "We can have one Remote hierarchy and one Device hierarchy.\n"
        "The remote uses the device interface — they are connected via a 'bridge'."
    )

    console.print("\n[bold blue]Benefits:[/bold blue]")
    console.print("- ✅ Avoids class explosion.")
    console.print("- ✅ Allows independent extension of remotes and devices.")
    console.print("- ✅ Cleaner, modular, and flexible design.\n")

    console.print("🎮 Try experimenting in the simulator: Connect the same remote to different devices!\n")
