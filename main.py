from rich.console import Console
from rich.table import Table
from rich.prompt import IntPrompt
import sys

console = Console()

from patterns.singleton import singleton_game, singleton_deepdive
from patterns.factory import factory_game, factory_deepdive
from patterns.abstract_factory import abstract_factory_game, abstract_factory_deepdive
from patterns.builder import builder_game, builder_deepdive
from patterns.prototype import prototype_game, prototype_deepdive
from patterns.adapter import adapter_game, adapter_deepdive
from patterns.bridge import bridge_game, bridge_deepdive
from patterns.composite import composite_game, composite_deepdive
from patterns.decorator import decorator_game, decorator_deepdive
from patterns.facade import facade_game, facade_deepdive
from patterns.flyweight import flyweight_game, flyweight_deepdive
from patterns.proxy import proxy_game, proxy_deepdive
from patterns.chain_of_responsibility import chain_of_responsibility_game, chain_of_responsibility_deepdive
from patterns.command import command_game, command_deepdive
from patterns.interpreter import interpreter_game, interpreter_deepdive
from patterns.iterator import iterator_game, iterator_deepdive
from patterns.mediator import mediator_game, mediator_deepdive
from patterns.memento import memento_game, memento_deepdive
from patterns.observer import observer_game, observer_deepdive
from patterns.state import state_game, state_deepdive
from patterns.strategy import strategy_game, strategy_deepdive
from patterns.template_method import template_method_game, template_method_deepdive
from patterns.visitor import visitor_game, visitor_deepdive

PATTERNS = {
    1: {'name': 'Singleton', 'game': singleton_game.run_game, 'deep': singleton_deepdive.run_deepdive},
    2: {'name': 'Factory', 'game': factory_game.run_game, 'deep': factory_deepdive.run_deepdive},
    3: {'name': 'Abstract_Factory', 'game': abstract_factory_game.run_game, 'deep': abstract_factory_deepdive.run_deepdive},
    4: {'name': 'Builder', 'game': builder_game.run_game, 'deep': builder_deepdive.run_deepdive},
    5: {'name': 'Prototype', 'game': prototype_game.run_game, 'deep': prototype_deepdive.run_deepdive},
    6: {'name': 'Adapter', 'game': adapter_game.run_game, 'deep': adapter_deepdive.run_deepdive},
    7: {'name': 'Bridge', 'game': bridge_game.run_game, 'deep': bridge_deepdive.run_deepdive},
    8: {'name': 'Composite', 'game': composite_game.run_game, 'deep': composite_deepdive.run_deepdive},
    9: {'name': 'Decorator', 'game': decorator_game.run_game, 'deep': decorator_deepdive.run_deepdive},
    10: {'name': 'Facade', 'game': facade_game.run_game, 'deep': facade_deepdive.run_deepdive},
    11: {'name': 'Flyweight', 'game': flyweight_game.run_game, 'deep': flyweight_deepdive.run_deepdive},
    12: {'name': 'Proxy', 'game': proxy_game.run_game, 'deep': proxy_deepdive.run_deepdive},
    13: {'name': 'Chain_Of_Responsibility', 'game': chain_of_responsibility_game.run_game, 'deep': chain_of_responsibility_deepdive.run_deepdive},
    14: {'name': 'Command', 'game': command_game.run_game, 'deep': command_deepdive.run_deepdive},
    15: {'name': 'Interpreter', 'game': interpreter_game.run_game, 'deep': interpreter_deepdive.run_deepdive},
    16: {'name': 'Iterator', 'game': iterator_game.run_game, 'deep': iterator_deepdive.run_deepdive},
    17: {'name': 'Mediator', 'game': mediator_game.run_game, 'deep': mediator_deepdive.run_deepdive},
    18: {'name': 'Memento', 'game': memento_game.run_game, 'deep': memento_deepdive.run_deepdive},
    19: {'name': 'Observer', 'game': observer_game.run_game, 'deep': observer_deepdive.run_deepdive},
    20: {'name': 'State', 'game': state_game.run_game, 'deep': state_deepdive.run_deepdive},
    21: {'name': 'Strategy', 'game': strategy_game.run_game, 'deep': strategy_deepdive.run_deepdive},
    22: {'name': 'Template_Method', 'game': template_method_game.run_game, 'deep': template_method_deepdive.run_deepdive},
    23: {'name': 'Visitor', 'game': visitor_game.run_game, 'deep': visitor_deepdive.run_deepdive},
}

def show_menu():
    table = Table(title="Design Patterns Playground")
    table.add_column("No.", justify="right")
    table.add_column("Pattern Name", justify="left")
    table.add_column("Description", justify="left")
    for num, pattern in PATTERNS.items():
        table.add_row(str(num), pattern["name"], f"Interactive mini-game for {pattern['name']} pattern")
    table.add_row("0", "Exit", "Exit the playground")
    console.print(table)

def select_mode(pattern_name):
    console.print(f"\n[bold cyan]You selected {pattern_name}![/bold cyan]")
    console.print("Choose mode:")
    console.print("1. Interactive Mini-Game")
    console.print("2. Deep Dive Mode (See internal workings)")
    console.print("0. Back to main menu")
    while True:
        choice = IntPrompt.ask("Enter your choice", default=1)
        if choice in [0, 1, 2]:
            return choice
        console.print("[red]Invalid choice! Try again.[/red]")

def main():
    console.print("[bold green]Welcome to the Design Patterns Playground![/bold green]\n")
    while True:
        show_menu()
        try:
            choice = IntPrompt.ask("\nSelect a pattern number", default=0)
        except KeyboardInterrupt:
            console.print("\n[bold red]Exiting...[/bold red]")
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
        console.print("\n[bold green]Returning to main menu...[/bold green]\n")

if __name__ == "__main__":
    main()
