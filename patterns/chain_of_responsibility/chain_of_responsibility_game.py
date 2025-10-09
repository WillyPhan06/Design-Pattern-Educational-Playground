from rich.console import Console
from rich.prompt import Prompt
from rich.progress import track
import time

console = Console()

# Handler base class
class SupportHandler:
    def __init__(self, name, next_handler=None):
        self.name = name
        self.next_handler = next_handler

    def handle(self, ticket):
        if self.can_handle(ticket):
            console.print(f"[green]{self.name} handled ticket '{ticket}'[/green]")
            return True
        elif self.next_handler:
            console.print(f"[yellow]{self.name} cannot handle '{ticket}', passing to {self.next_handler.name}...[/yellow]")
            time.sleep(0.5)
            return self.next_handler.handle(ticket)
        else:
            console.print(f"[red]No one could handle ticket '{ticket}'[/red]")
            return False

    def can_handle(self, ticket):
        raise NotImplementedError

# Concrete Handlers
class Level1Support(SupportHandler):
    def can_handle(self, ticket):
        return ticket.lower() in ["password reset", "login issue"]

class Level2Support(SupportHandler):
    def can_handle(self, ticket):
        return ticket.lower() in ["software bug", "network issue"]

class ManagerSupport(SupportHandler):
    def can_handle(self, ticket):
        return ticket.lower() in ["refund request", "policy escalation"]

def run_game():
    console.print("[bold cyan]Chain of Responsibility - Customer Support Simulator[/bold cyan]\n")

    # Setup chain
    manager = ManagerSupport("Manager")
    level2 = Level2Support("Level 2 Support", next_handler=manager)
    level1 = Level1Support("Level 1 Support", next_handler=level2)

    tickets_handled = []

    while True:
        console.print("\nActions:")
        console.print("1. Submit a support ticket")
        console.print("2. Show all tickets handled")
        console.print("0. Exit")

        choice = Prompt.ask("Choose action", choices=["0","1","2"])

        if choice == "0":
            console.print("\n👋 Exiting Customer Support Simulator...\n")
            break

        elif choice == "1":
            ticket = Prompt.ask("Enter ticket description (e.g.,'software bug', 'password reset', 'network issue', 'refund request')")
            console.print("[bold blue]Processing ticket...[/bold blue]")

            # Progress bar animation
            for _ in track(range(20), description="Ticket moving through support chain..."):
                time.sleep(0.05)

            if level1.handle(ticket):
                tickets_handled.append(ticket)

        elif choice == "2":
            if not tickets_handled:
                console.print("[yellow]No tickets handled yet.[/yellow]")
            else:
                console.print("[bold green]Tickets handled:[/bold green]")
                for t in tickets_handled:
                    console.print(f"- {t}")
