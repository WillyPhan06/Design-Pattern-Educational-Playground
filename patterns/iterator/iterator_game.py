from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

console = Console()

# Iterator Interface
class Iterator:
    def has_next(self):
        raise NotImplementedError

    def next(self):
        raise NotImplementedError

# Concrete Iterator
class TreasureIterator(Iterator):
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def has_next(self):
        return self.index < len(self.collection.items)

    def next(self):
        if self.has_next():
            item = self.collection.items[self.index]
            self.index += 1
            return item
        return None

# Collection Interface
class Collection:
    def create_iterator(self):
        raise NotImplementedError

# Concrete Collection
class TreasureChest(Collection):
    def __init__(self, items):
        self.items = items

    def create_iterator(self):
        return TreasureIterator(self)

# Game function
def run_game():
    console.print("[bold cyan]Iterator Pattern - Treasure Chest Explorer[/bold cyan]\n")

    items = ["Gold Coin", "Silver Ring", "Emerald Gem", "Potion", "Ancient Scroll"]
    chest = TreasureChest(items)
    iterator = chest.create_iterator()

    while True:
        console.print("\nActions:")
        console.print("1. Inspect next item")
        console.print("0. Exit")

        choice = Prompt.ask("Choose action", choices=["0","1"])

        if choice == "0":
            console.print("\n👋 Exiting Treasure Chest Explorer...\n")
            break
        elif choice == "1":
            if iterator.has_next():
                item = iterator.next()
                console.print(f"[yellow]You found:[/yellow] {item}")
            else:
                console.print("[red]No more items in the chest![/red]")
