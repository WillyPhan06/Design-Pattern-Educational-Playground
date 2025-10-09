from rich.console import Console

console = Console()

def run_deepdive():
    console.print("[bold magenta]Memento Pattern Deep Dive[/bold magenta]\n")

    console.print(
        "The [bold cyan]Memento Pattern[/bold cyan] allows capturing an object's internal state "
        "without exposing its implementation so it can be restored later.\n"
    )

    console.print("[bold yellow]Mapping in Game:[/bold yellow]")
    console.print("- [green]Originator:[/green] TextEditor (object whose state changes)")
    console.print("- [green]Memento:[/green] EditorMemento (snapshot of editor content)")
    console.print("- [green]Caretaker:[/green] EditorHistory (manages saved checkpoints)\n")

    console.print("[bold green]Key Insights:[/bold green]")
    console.print("- ✅ Save and restore object state without exposing internals")
    console.print("- ✅ Enables undo/redo functionality")
    console.print("- ✅ Keeps history of multiple snapshots\n")

    console.print("[bold blue]Educational Insights:[/bold blue]")
    console.print("- Player types text, saves checkpoints, and performs undo")
    console.print("- Immediate feedback shows state restoration")
    console.print("- Reinforces concept of encapsulation and state management")
