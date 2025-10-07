from rich.console import Console
from rich.prompt import IntPrompt
from rich.panel import Panel

console = Console()

def run_game():
    console.print("[bold cyan]Singleton - Interactive Mini-Game[/bold cyan]\n")

    normal_count = 0
    singleton_created = False
    singleton_clicks = 0
    objects_limit_display = 5

    while True:
        console.print(Panel.fit("[1] Normal Factory  |  [2] Singleton Factory  |  [0] Exit", title="Choose a factory"))
        choice = IntPrompt.ask("Which factory do you want to use?", default=0)
        if choice == 0:
            console.print("[bold yellow]Returning to main menu...[/bold yellow]\n")
            break
        elif choice == 1:
            normal_count += 1
            console.print(f"[green]Normal Factory:[/green] Created object #{normal_count}")
            display_objects = min(normal_count, objects_limit_display)
            console.print("Recent objects: " + " ".join([f"[{i}]" for i in range(normal_count-display_objects+1, normal_count+1)]))
            console.print("\n")
        elif choice == 2:
            singleton_clicks += 1
            if not singleton_created:
                singleton_created = True
                console.print("[bold green]Singleton Factory:[/bold green] Object created successfully! ✅")
                console.print("Recent objects: [1]\n")
            else:
                # Dynamic guard message
                suffix = {1: "st", 2: "nd", 3: "rd"}.get(singleton_clicks, "th")
                guard_message = f"Hey, don't try to create that same thing for the {singleton_clicks}{suffix} time! ❌"
                console.print(f"[bold yellow]Singleton Factory:[/bold yellow] No new object created [1]")
                console.print("Recent objects: [1]")
                console.print(f"[bold red]Guard:[/bold red] {guard_message}\n")

