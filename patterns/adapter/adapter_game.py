from rich.console import Console
from rich.table import Table
import time

console = Console()

adapters = {
    "EU-US Adapter": ("EU", "US"),
    "EU-UK Adapter": ("EU", "UK"),
    "US-UK Adapter": ("US", "UK")
}

def check_connection(plug, socket, use_adapter=False, adapter_name=None):
    if plug == socket:
        return True, f"✅ Perfect match! {plug} plug fits {socket} socket directly!"
    
    if not use_adapter:
        return False, f"💥 Oops! {plug} plug doesn’t fit {socket} socket without an adapter!"
    
    if adapter_name not in adapters:
        return False, "❌ Invalid adapter."
    
    a1, a2 = adapters[adapter_name]
    if (plug, socket) in [(a1, a2), (a2, a1)]:
        return True, f"⚡ Success! {plug} plug connects to {socket} socket via {adapter_name}!"
    
    return False, f"💥 Adapter {adapter_name} doesn’t support {plug} ↔ {socket}!"

def run_game():
    console.rule("[bold cyan]Adapter Pattern - Plug & Socket Simulator[/bold cyan]")

    plug_types = ["EU", "US", "UK"]
    socket_types = ["EU", "US", "UK"]

    while True:
        console.print("\n[bold yellow]Available Plug Types:[/bold yellow] EU, US, UK")
        plug = console.input("🔌 Choose your plug type: ").strip().upper()
        if plug not in plug_types:
            console.print("[red]Invalid plug type! Try again.[/red]")
            continue

        console.print("\n[bold yellow]Available Socket Types:[/bold yellow] EU, US, UK")
        socket = console.input("⚙️  Choose your socket type: ").strip().upper()
        if socket not in socket_types:
            console.print("[red]Invalid socket type! Try again.[/red]")
            continue

        use_adapter = console.input("\nUse adapter? (y/n): ").strip().lower()
        if use_adapter == 'y':
            table = Table(title="Available Adapters", show_header=True, header_style="bold magenta")
            table.add_column("Option", justify="center")
            table.add_column("Adapter Name", justify="center")
            for i, name in enumerate(adapters.keys(), 1):
                table.add_row(str(i), name)
            console.print(table)

            choice = console.input("🔧 Choose an adapter by number: ").strip()
            if not choice.isdigit() or int(choice) not in range(1, len(adapters) + 1):
                console.print("[red]Invalid choice![/red]")
                continue
            adapter_name = list(adapters.keys())[int(choice) - 1]
            success, message = check_connection(plug, socket, True, adapter_name)
        else:
            success, message = check_connection(plug, socket, False)

        console.print(f"\n{message}\n")

        # Small visual delay for immersion
        for _ in range(3):
            console.print("⚙️  Checking connection...", end="\r")
            time.sleep(0.4)
        console.print(" " * 30, end="\r")

        if success:
            console.print("[bold green]Connection stable![/bold green] ⚡\n")
        else:
            console.print("[bold red]Connection failed.[/bold red] 💥\n")

        again = console.input("Try again? (y/n): ").strip().lower()
        if again != 'y':
            console.print("\n[bold cyan]Exiting Plug & Socket Simulator...[/bold cyan]")
            break
