from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
import time

console = Console()

# States
class TrafficLightState:
    def switch(self, context):
        raise NotImplementedError

    def action(self):
        raise NotImplementedError

class RedState(TrafficLightState):
    def switch(self, context):
        context.state = GreenState()
        console.print("[bold red]Switching to Green...[/bold red]")
        time.sleep(1)

    def action(self):
        console.print("[red]Stop![/red] 🚦")

class YellowState(TrafficLightState):
    def switch(self, context):
        context.state = RedState()
        console.print("[bold yellow]Switching to Red...[/bold yellow]")
        time.sleep(1)

    def action(self):
        console.print("[yellow]Ready to go...[/yellow] ⚠️")

class GreenState(TrafficLightState):
    def switch(self, context):
        context.state = YellowState()
        console.print("[bold green]Switching to Yellow...[/bold green]")
        time.sleep(1)

    def action(self):
        console.print("[green]Go![/green] 🟢")

# Context
class TrafficLight:
    def __init__(self):
        self.state = RedState()

    def switch(self):
        self.state.switch(self)

    def action(self):
        self.state.action()

# Game function
def run_game():
    console.print("[bold cyan]State Pattern - Traffic Light Simulator[/bold cyan]\n")
    traffic_light = TrafficLight()

    while True:
        console.print("\nCurrent Traffic Light State:")
        traffic_light.action()
        console.print("\nActions:")
        console.print("1. Switch Light")
        console.print("0. Exit")

        choice = Prompt.ask("Choose action", choices=["0","1"])

        if choice == "0":
            console.print("\n👋 Exiting Traffic Light Simulator...\n")
            break
        else:
            traffic_light.switch()
