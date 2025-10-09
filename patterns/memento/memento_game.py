from rich.console import Console
from rich.prompt import Prompt

console = Console()

# Memento
class EditorMemento:
    def __init__(self, content):
        self.content = content

# Originator
class TextEditor:
    def __init__(self):
        self.content = ""

    def type_text(self, text):
        self.content += text + "\n"

    def save(self):
        return EditorMemento(self.content)

    def restore(self, memento):
        self.content = memento.content

# Caretaker
class EditorHistory:
    def __init__(self):
        self.history = []

    def push(self, memento):
        self.history.append(memento)

    def pop(self):
        if self.history:
            return self.history.pop()
        return None

# Game function
def run_game():
    console.print("[bold cyan]Memento Pattern - Text Editor Undo[/bold cyan]\n")

    editor = TextEditor()
    history = EditorHistory()

    while True:
        console.print("\nCurrent Text Editor Content:\n")
        console.print(editor.content or "[grey]-- empty --[/grey]\n")

        console.print("Actions:")
        console.print("1. Type text")
        console.print("2. Save checkpoint")
        console.print("3. Undo to last checkpoint")
        console.print("0. Exit")

        choice = Prompt.ask("Choose action", choices=["0","1","2","3"])

        if choice == "0":
            console.print("\n👋 Exiting Text Editor...\n")
            break
        elif choice == "1":
            text = Prompt.ask("Enter text")
            editor.type_text(text)
        elif choice == "2":
            history.push(editor.save())
            console.print("[green]Checkpoint saved![/green]")
        elif choice == "3":
            memento = history.pop()
            if memento:
                editor.restore(memento)
                console.print("[yellow]Undo performed![/yellow]")
            else:
                console.print("[red]No checkpoints available![/red]")
