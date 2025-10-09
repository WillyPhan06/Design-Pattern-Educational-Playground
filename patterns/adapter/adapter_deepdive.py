from rich.console import Console

console = Console()

def run_deepdive():
    console.rule("[bold cyan]Adapter Pattern - Deep Dive[/bold cyan]")
    console.print("""
[bold]Concept:[/bold]
The Adapter Pattern allows incompatible interfaces to work together.
It's like using a plug adapter to make a foreign device work with a local socket.

[bold]Example Breakdown:[/bold]
- [green]Plug (Client)[/green]: The object that wants to connect.
- [green]Socket (Target Interface)[/green]: The system expecting a specific interface.
- [green]Adapter[/green]: The bridge that converts one interface into another.

[bold]Why it matters:[/bold]
Adapters are used everywhere:
- Integrating legacy code with modern systems
- Making APIs compatible
- Connecting systems with different data formats or protocols

[bold]In this simulation:[/bold]
- Plug = client object
- Socket = expected interface
- Adapter = object that makes them compatible
    """)

    console.print("\n[bold yellow]Example (in code):[/bold yellow]")
    console.print("""
class USPlug:
    def power(self):
        return "120V power"

class EUAdapter:
    def __init__(self, plug):
        self.plug = plug
    def power(self):
        return self.plug.power().replace("120V", "230V")

plug = USPlug()
adapter = EUAdapter(plug)
print(adapter.power())  # "230V power"
""")
    console.print("\n[bold green]=> The Adapter pattern helps incompatible objects work together seamlessly.[/bold green]\n")
