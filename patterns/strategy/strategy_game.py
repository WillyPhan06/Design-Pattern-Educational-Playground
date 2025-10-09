from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.progress import track
import time
import random

console = Console()

# Strategy Interface
class SoldierStrategy:
    def execute_action(self, command, threat):
        raise NotImplementedError

# Concrete Strategies
class Sniper(SoldierStrategy):
    def execute_action(self, command, threat):
        if command == "Attack":
            damage = random.randint(25, 50)
            return f"Sniper attacks {threat} from afar for {damage} damage!"
        else:
            return f"Sniper takes cover and prepares a precision shot against {threat}!"

class AssaultRifler(SoldierStrategy):
    def execute_action(self, command, threat):
        if command == "Attack":
            damage = random.randint(15, 35)
            return f"Assault Rifler sprays bullets at {threat} for {damage} damage!"
        else:
            return f"Assault Rifler braces and reduces incoming damage from {threat}!"

class Shotguner(SoldierStrategy):
    def execute_action(self, command, threat):
        if command == "Attack":
            damage = random.randint(20, 40)
            return f"Shotguner rushes close and blasts {threat} for {damage} damage!"
        else:
            return f"Shotguner sets traps to defend against {threat}!"

class MeleeFighter(SoldierStrategy):
    def execute_action(self, command, threat):
        if command == "Attack":
            damage = random.randint(10, 30)
            return f"Melee Fighter strikes {threat} with a heavy blow for {damage} damage!"
        else:
            return f"Melee Fighter blocks and counter-attacks {threat}!"

# Soldier Context
class Soldier:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy

    def perform_action(self, command, threat):
        return self.strategy.execute_action(command, threat)

# Game function
def run_game():
    console.print("[bold cyan]Strategy Pattern - Commander Battle Simulator[/bold cyan]\n")

    soldiers = [
        Soldier("Sniper", Sniper()),
        Soldier("Assault Rifler", AssaultRifler()),
        Soldier("Shotguner", Shotguner()),
        Soldier("Melee Fighter", MeleeFighter()),
    ]

    threats = ["Orc", "Goblin", "Bandit", "Enemy Tank", "Dragon"]

    while True:
        console.print("\nActions:")
        console.print("1. Issue command to soldiers")
        console.print("0. Exit")

        choice = Prompt.ask("Choose action", choices=["0","1"])

        if choice == "0":
            console.print("\n👋 Exiting Commander Battle Simulator...\n")
            break

        elif choice == "1":
            threat = random.choice(threats)
            console.print(f"\n⚠️  A wild {threat} appears!\n")

            command = Prompt.ask("Choose command for all soldiers", choices=["Attack", "Defend"])

            console.print("[bold blue]Soldiers executing command...[/bold blue]")
            for _ in track(range(20), description="Command in action..."):
                time.sleep(0.03)

            table = Table(title=f"Results of {command}")
            table.add_column("Soldier")
            table.add_column("Action Outcome")

            for soldier in soldiers:
                result = soldier.perform_action(command, threat)
                table.add_row(soldier.name, result)

            console.print(table)
