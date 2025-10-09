from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.tree import Tree

console = Console()

class FileComponent:
    def __init__(self, name):
        self.name = name

    def display(self, tree):
        raise NotImplementedError

class File(FileComponent):
    def display(self, tree):
        tree.add(f"📄 {self.name}")

class Folder(FileComponent):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, name):
        for c in self.children:
            if c.name == name:
                self.children.remove(c)
                return True
            if isinstance(c, Folder):
                if c.remove(name):
                    return True
        return False

    def display(self, tree=None):
        if tree is None:
            tree = Tree(f"📁 {self.name}")
        for c in self.children:
            if isinstance(c, Folder):
                subtree = tree.add(f"📁 {c.name}")
                c.display(subtree)
            else:
                c.display(tree)
        console.print(tree)

root = Folder("root")

def run_game():
    console.print("[bold cyan]Composite Pattern - File System Explorer[/bold cyan]\n")

    while True:
        console.print("\nActions:")
        console.print("1. Create File")
        console.print("2. Create Folder")
        console.print("3. Display File Structure")
        console.print("4. Delete File/Folder")
        console.print("0. Exit")

        choice = Prompt.ask("Choose action", choices=["0","1","2","3","4"])

        if choice == "0":
            console.print("\n👋 Exiting File System Explorer...")
            break

        elif choice == "1":
            name = Prompt.ask("Enter file name")
            folder_name = Prompt.ask("Enter folder path to place file (or 'root')", default="root")
            parent = root if folder_name.lower() == "root" else find_folder(root, folder_name)
            if parent:
                parent.add(File(name))
                console.print(f"📄 File '{name}' created in '{parent.name}'")
            else:
                console.print(f"[red]Folder '{folder_name}' not found[/red]")

        elif choice == "2":
            name = Prompt.ask("Enter folder name")
            folder_name = Prompt.ask("Enter folder path to place folder (or 'root')", default="root")
            parent = root if folder_name.lower() == "root" else find_folder(root, folder_name)
            if parent:
                parent.add(Folder(name))
                console.print(f"📁 Folder '{name}' created in '{parent.name}'")
            else:
                console.print(f"[red]Folder '{folder_name}' not found[/red]")

        elif choice == "3":
            console.print("\n[bold green]Current File Structure:[/bold green]")
            root.display()

        elif choice == "4":
            name = Prompt.ask("Enter the name of file/folder to delete")
            if root.remove(name):
                console.print(f"[green]Deleted '{name}'[/green]")
            else:
                console.print(f"[red]Item '{name}' not found[/red]")

def find_folder(current, name):
    if current.name == name:
        return current
    for c in getattr(current, "children", []):
        if isinstance(c, Folder):
            found = find_folder(c, name)
            if found:
                return found
    return None
