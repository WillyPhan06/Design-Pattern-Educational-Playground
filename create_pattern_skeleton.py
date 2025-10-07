# create_pattern_skeleton.py
import os

# List of all 23 design patterns
patterns = [
    "singleton", "factory", "abstract_factory", "builder", "prototype", "adapter", "bridge",
    "composite", "decorator", "facade", "flyweight", "proxy",
    "chain_of_responsibility", "command", "interpreter", "iterator",
    "mediator", "memento", "observer", "state", "strategy",
    "template_method", "visitor"
]

# Base directory
base_dir = "patterns"

# Ensure base directory exists
os.makedirs(base_dir, exist_ok=True)

# Template for *_game.py
game_template = '''from rich.console import Console

console = Console()

def run_game():
    console.print("[bold cyan]{pattern_name} - Interactive Mini-Game[/bold cyan]")
    console.print("This is where the interactive game for {pattern_name} will run.\\n")
'''

# Template for *_deepdive.py
deepdive_template = '''from rich.console import Console

console = Console()

def run_deepdive():
    console.print("[bold magenta]{pattern_name} - Deep Dive[/bold magenta]")
    console.print("This is where the detailed internal workings of {pattern_name} will be shown.\\n")
'''

# Create folders and stub files
for pattern in patterns:
    pattern_dir = os.path.join(base_dir, pattern)
    os.makedirs(pattern_dir, exist_ok=True)
    
    # __init__.py
    init_file = os.path.join(pattern_dir, "__init__.py")
    with open(init_file, "w") as f:
        f.write("# Module for {} pattern\n".format(pattern))
    
    # *_game.py
    game_file = os.path.join(pattern_dir, f"{pattern}_game.py")
    with open(game_file, "w") as f:
        f.write(game_template.format(pattern_name=pattern.title()))
    
    # *_deepdive.py
    deep_file = os.path.join(pattern_dir, f"{pattern}_deepdive.py")
    with open(deep_file, "w") as f:
        f.write(deepdive_template.format(pattern_name=pattern.title()))

print("All 23 design pattern folders and stub files created successfully!")
