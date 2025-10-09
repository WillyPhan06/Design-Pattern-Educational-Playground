from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

console = Console()

# Flyweight: Human
class Human:
    def __init__(self, name):
        self.name = name
        self.weight = 50  # kg

# Factory to manage humans (shared intrinsic state)
class HumanFactory:
    def __init__(self):
        self._humans = {}

    def get_human(self, name):
        if name not in self._humans:
            self._humans[name] = Human(name)
            console.print(f"[green]Created new human:[/green] {name}")
        else:
            console.print(f"[yellow]Reusing existing human:[/yellow] {name}")
        return self._humans[name]

# Client-side: Photo
class Photo:
    def __init__(self, human):
        self.human = human
        self.weight = 0.5  # kg

def run_game():
    console.print("[bold cyan]Flyweight Pattern - Human & Photo Simulator[/bold cyan]\n")
    factory = HumanFactory()
    photos = []

    while True:
        console.print("\nActions:")
        console.print("1. Create new Human")
        console.print("2. Take Photo of existing Human")
        console.print("3. Show current Humans & Photos and total weight")
        console.print("0. Exit")

        choice = Prompt.ask("Choose action", choices=["0","1","2","3"])

        if choice == "0":
            console.print("\n👋 Exiting Flyweight Simulator...\n")
            break

        elif choice == "1":
            name = Prompt.ask("Enter human name")
            human = factory.get_human(name)

        elif choice == "2":
            if not factory._humans:
                console.print("[red]No humans exist. Create a human first.[/red]")
                continue
            console.print("Existing humans:")
            for human_name in factory._humans.keys():
                console.print(f"- {human_name}")
            chosen_name = Prompt.ask("Choose human name to take photo of")
            if chosen_name not in factory._humans:
                console.print("[red]Invalid human name[/red]")
                continue
            human = factory.get_human(chosen_name)
            photo = Photo(human)
            photos.append(photo)
            console.print(f"[cyan]Took a photo of {human.name}[/cyan]")

        elif choice == "3":
            table = Table(title="Humans & Photos")
            table.add_column("Human Name")
            table.add_column("Number of Photos")
            for human_name, human_obj in factory._humans.items():
                count = sum(1 for p in photos if p.human == human_obj)
                table.add_row(human_name, str(count))
            console.print(table)

            # Calculate total weight
            total_weight = sum(h.weight for h in factory._humans.values()) + sum(p.weight for p in photos)
            console.print(f"[bold yellow]Total weight:[/bold yellow] {total_weight} kg")
