# setup_patterns_and_main.py
import os

# List of all 23 design patterns
patterns = [
    "singleton", "factory", "abstract_factory", "builder", "prototype", "adapter", "bridge",
    "composite", "decorator", "facade", "flyweight", "proxy",
    "chain_of_responsibility", "command", "interpreter", "iterator",
    "mediator", "memento", "observer", "state", "strategy",
    "template_method", "visitor"
]


base_dir = "patterns"
os.makedirs(base_dir, exist_ok=True)

# Templates for game and deepdive stubs
game_template = '''from rich.console import Console

console = Console()

def run_game():
    console.print("[bold cyan]{pattern_name} - Interactive Mini-Game[/bold cyan]")
    console.print("This is where the interactive game for {pattern_name} will run.\\n")
'''

deepdive_template = '''from rich.console import Console

console = Console()

def run_deepdive():
    console.print("[bold magenta]{pattern_name} - Deep Dive[/bold magenta]")
    console.print("This is where the detailed internal workings of {pattern_name} will be shown.\\n")
'''

# Create pattern folders and stub files if they don't exist
for pattern in patterns:
    pattern_dir = os.path.join(base_dir, pattern)
    os.makedirs(pattern_dir, exist_ok=True)
    
    # __init__.py
    init_file = os.path.join(pattern_dir, "__init__.py")
    if not os.path.exists(init_file):
        with open(init_file, "w") as f:
            f.write(f"# Module for {pattern} pattern\n")
    
    # *_game.py
    game_file = os.path.join(pattern_dir, f"{pattern}_game.py")
    if not os.path.exists(game_file):
        with open(game_file, "w") as f:
            f.write(game_template.format(pattern_name=pattern.title()))
    
    # *_deepdive.py
    deep_file = os.path.join(pattern_dir, f"{pattern}_deepdive.py")
    if not os.path.exists(deep_file):
        with open(deep_file, "w") as f:
            f.write(deepdive_template.format(pattern_name=pattern.title()))

print("Pattern folders and stub files checked/created.")

# -------------------------
# Auto-generate main.py
# -------------------------
main_file = "main.py"

with open(main_file, "w") as f:
    f.write("""from rich.console import Console
from rich.table import Table
from rich.prompt import IntPrompt
import sys

console = Console()

""")

    # Write imports dynamically
    for pattern in patterns:
        import_line = f"from patterns.{pattern} import {pattern}_game, {pattern}_deepdive\n"
        f.write(import_line)
    
    # Write PATTERNS dictionary
    f.write("\nPATTERNS = {\n")
    for i, pattern in enumerate(patterns, start=1):
        f.write(f"    {i}: {{'name': '{pattern.title()}', 'game': {pattern}_game.run_game, 'deep': {pattern}_deepdive.run_deepdive}},\n")
    f.write("}\n\n")

    # Write show_menu function
    f.write("""def show_menu():
    table = Table(title="Design Patterns Playground")
    table.add_column("No.", justify="right")
    table.add_column("Pattern Name", justify="left")
    table.add_column("Description", justify="left")
    for num, pattern in PATTERNS.items():
        table.add_row(str(num), pattern["name"], f"Interactive mini-game for {pattern['name']} pattern")
    table.add_row("0", "Exit", "Exit the playground")
    console.print(table)\n\n""")

    # Write select_mode function
    f.write("""def select_mode(pattern_name):
    console.print(f"\\n[bold cyan]You selected {pattern_name}![/bold cyan]")
    console.print("Choose mode:")
    console.print("1. Interactive Mini-Game")
    console.print("2. Deep Dive Mode (See internal workings)")
    console.print("0. Back to main menu")
    while True:
        choice = IntPrompt.ask("Enter your choice", default=1)
        if choice in [0, 1, 2]:
            return choice
        console.print("[red]Invalid choice! Try again.[/red]")\n\n""")

    # Write main function
    f.write("""def main():
    console.print("[bold green]Welcome to the Design Patterns Playground![/bold green]\\n")
    while True:
        show_menu()
        try:
            choice = IntPrompt.ask("\\nSelect a pattern number", default=0)
        except KeyboardInterrupt:
            console.print("\\n[bold red]Exiting...[/bold red]")
            sys.exit(0)
        if choice == 0:
            console.print("[bold yellow]Goodbye![/bold yellow]")
            sys.exit(0)
        if choice not in PATTERNS:
            console.print("[red]Invalid choice! Please select a valid pattern number.[/red]")
            continue
        pattern = PATTERNS[choice]
        mode = select_mode(pattern["name"])
        if mode == 1:
            pattern["game"]()
        elif mode == 2:
            pattern["deep"]()
        console.print("\\n[bold green]Returning to main menu...[/bold green]\\n")\n\n""")

    # Entry point
    f.write("""if __name__ == "__main__":
    main()
""")

print("main.py generated successfully! You can now run your CLI playground.")
