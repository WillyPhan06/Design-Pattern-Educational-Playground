from rich.console import Console

console = Console()

def run_deepdive():
    console.print("[bold magenta]Composite Pattern Deep Dive[/bold magenta]\n")

    console.print(
        "The [bold cyan]Composite Pattern[/bold cyan] allows you to treat individual objects and "
        "compositions of objects uniformly.\n"
    )

    console.print("[bold yellow]Example Mapping in Game:[/bold yellow]")
    console.print("- [green]File[/green]: Leaf object")
    console.print("- [green]Folder[/green]: Composite object")
    console.print("- [green]root[/green]: Top-level composite")
    console.print("- Operations: create, display, delete — work for both files and folders\n")

    console.print("[bold green]Benefits:[/bold green]")
    console.print("- ✅ Simplifies client code: treat leaves and composites uniformly")
    console.print("- ✅ Makes tree structures easy to manage")
    console.print("- ✅ Supports recursive operations naturally\n")

    console.print("[bold blue]Try experimenting:[/bold blue]")
    console.print("- Create files and folders at different levels")
    console.print("- Delete files/folders and see the structure update dynamically")
    console.print("- Notice how display works uniformly for both single files and nested folders")
