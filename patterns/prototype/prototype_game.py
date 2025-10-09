from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.progress import track
import time
import copy
import random

console = Console()

# -------------------------------
# Prototype & Aliens
# -------------------------------
class AlienPrototype:
    def __init__(self, kind, color, power, intelligence):
        self.kind = kind
        self.color = color
        self.power = power
        self.intelligence = intelligence

    def clone(self, clone_id):
        # create a deep copy so modifications don't affect the prototype
        c = copy.deepcopy(self)
        c.name = f"{self.kind}#{clone_id}"
        return c

    def to_row(self):
        return [getattr(self, "name", self.kind), self.color, str(self.power), str(self.intelligence)]

# -------------------------------
# Utility display functions
# -------------------------------
def show_prototypes(protos):
    table = Table(title="Available Prototypes")
    table.add_column("#", justify="center")
    table.add_column("Kind")
    table.add_column("Color")
    table.add_column("Power")
    table.add_column("Intelligence")
    for i, p in enumerate(protos, start=1):
        table.add_row(str(i), p.kind, p.color, str(p.power), str(p.intelligence))
    console.print(table)

def show_clones(clones):
    table = Table(title="Cloned Aliens (most recent shown)")
    table.add_column("#", justify="center")
    table.add_column("Name")
    table.add_column("Color")
    table.add_column("Power")
    table.add_column("Intelligence")
    # show only the 3 most recent
    recent = clones[-3:]
    for i, c in enumerate(recent, start=max(1, len(clones)-2)):
        table.add_row(str(i), c.name, c.color, str(c.power), str(c.intelligence))
    console.print(table)

def animate_action(text, seconds=1.0, steps=3):
    # simple staged animation using track for progress feel
    for _ in track(range(steps), description=text):
        time.sleep(seconds/steps)

# -------------------------------
# Interactive Game
# -------------------------------
def run_game():
    console.print("[bold cyan]🧬 Prototype — Alien Clone Lab[/bold cyan]\n")
    console.print("Welcome to the Alien Clone Lab! Clone prototypes and mutate your clones.\n")

    # Define prototypes
    prototypes = [
        AlienPrototype("Worker", "green", 50, 30),
        AlienPrototype("Soldier", "red", 80, 40),
        AlienPrototype("Scientist", "blue", 40, 90),
    ]

    clones = []      # all clones created
    clone_counter = 0

    while True:
        show_prototypes(prototypes)
        console.print("[1] Clone a prototype    [2] View all clones    [0] Exit to main menu")
        action = IntPrompt.ask("Choose an action", default=1)

        if action == 0:
            console.print("[bold yellow]Returning to main menu...[/bold yellow]\n")
            break

        if action == 1:
            idx = IntPrompt.ask("Pick prototype number to clone (1-3)", default=1)
            if idx < 1 or idx > len(prototypes):
                console.print("[red]Invalid prototype number.[/red]\n")
                continue

            proto = prototypes[idx - 1]
            clone_counter += 1

            # Animate cloning
            animate_action(f"[green]Cloning {proto.kind} prototype... 🧬[/green]", seconds=1.2, steps=4)
            new_clone = proto.clone(clone_counter)
            clones.append(new_clone)
            console.print(f"[bold green]Cloned:[/bold green] {new_clone.name} ({proto.kind}) created.\n")

            # Show the 2 latest clones (as requested earlier: 2 latest; but clones table shows 3 most recent)
            show_clones(clones)

            # Offer mutation
            mutate = Prompt.ask("Mutate this clone? (y/n)", choices=["y", "n"], default="n")
            if mutate == "y":
                while True:
                    console.print("\nChoose attribute to mutate:")
                    console.print("[1] Color   [2] Power   [3] Intelligence   [0] Done mutating")
                    choice = IntPrompt.ask("Your choice", default=0)
                    if choice == 0:
                        break
                    elif choice == 1:
                        new_color = Prompt.ask("Enter new color (e.g., purple)")
                        old = new_clone.color
                        new_clone.color = new_color
                        console.print(f"[cyan]Color changed:[/cyan] {old} → {new_color}")
                    elif choice == 2:
                        new_power = IntPrompt.ask("Enter new power (1-200)", default=new_clone.power)
                        old = new_clone.power
                        new_clone.power = max(1, min(200, new_power))
                        console.print(f"[cyan]Power changed:[/cyan] {old} → {new_clone.power}")
                    elif choice == 3:
                        new_int = IntPrompt.ask("Enter new intelligence (1-200)", default=new_clone.intelligence)
                        old = new_clone.intelligence
                        new_clone.intelligence = max(1, min(200, new_int))
                        console.print(f"[cyan]Intelligence changed:[/cyan] {old} → {new_clone.intelligence}")
                    else:
                        console.print("[red]Invalid choice.[/red]")
                console.print(f"\n[bold green]{new_clone.name} mutated successfully![/bold green]\n")
                show_clones(clones)

            # After clone & optional mutation, maybe auto-run a tiny randomized event showcasing difference
            if len(clones) >= 1 and random.random() < 0.35:
                # tiny randomized scenario
                c = clones[-1]
                event = random.choice([
                    f"{c.name} saved a scientist thanks to high intelligence!",
                    f"{c.name} dominated a skirmish with power {c.power}!",
                    f"{c.name} discovered a new mineral with color {c.color}!"
                ])
                console.print(f"[magenta]Lab event:[/magenta] {event}\n")

        elif action == 2:
            if not clones:
                console.print("[yellow]No clones created yet.[/yellow]\n")
            else:
                show_clones(clones)
            console.print("\n")
        else:
            console.print("[red]Invalid action.[/red]\n")
