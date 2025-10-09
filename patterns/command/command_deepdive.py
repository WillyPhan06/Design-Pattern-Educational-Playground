# patterns/command/command_deepdive.py
from rich.console import Console
from rich.table import Table
from rich.syntax import Syntax
import time

console = Console()

def run_deepdive():
    console.print("[bold magenta]=== Command Pattern — Deep Dive ===[/bold magenta]\n")

    console.print(
        "The [bold yellow]Command Pattern[/bold yellow] encapsulates a request as an object, "
        "allowing you to parameterize clients with queues, requests, and support undoable operations.\n"
    )
    time.sleep(0.5)

    # Roles table
    table = Table(title="Command Pattern — Roles", show_lines=True)
    table.add_column("Role", style="bold cyan", justify="center")
    table.add_column("Responsibility", style="white")
    table.add_row("Command", "Declares an interface for executing an operation (execute, undo).")
    table.add_row("ConcreteCommand", "Implements execute by invoking operations on the Receiver.")
    table.add_row("Receiver", "Performs the actual work (e.g., Robot).")
    table.add_row("Invoker", "Stores and executes commands (can support undo/redo/replay).")
    table.add_row("Client", "Creates ConcreteCommand objects and configures the Invoker.")
    console.print(table)
    time.sleep(0.8)

    # Small illustrated example
    console.print("\n[bold magenta]Minimal Example (Python)[/bold magenta]\n")
    code = '''class Command:
    def execute(self): pass
    def undo(self): pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    def execute(self):
        self.light.on()
    def undo(self):
        self.light.off()

class Light:
    def on(self): print("Light ON")
    def off(self): print("Light OFF")

# Client/Invoker usage:
light = Light()
cmd = LightOnCommand(light)
cmd.execute()  # Light ON
cmd.undo()     # Light OFF
'''
    console.print(Syntax(code, "python", theme="monokai", line_numbers=True))
    time.sleep(0.9)

    # Explain common features
    console.print("\n[bold magenta]Key Features & Uses[/bold magenta]")
    console.print("""
- Commands decouple the object that invokes the operation from the one that knows how to perform it.
- Easy to add undo/redo by storing history of commands (each command implements undo).
- Useful for queuing, scheduling, or logging operations.
- Commands can be composed to build macros (composite commands).
    """)
    time.sleep(0.6)

    # Small walk-through demonstrating undo / replay conceptually
    console.print("[bold magenta]Conceptual Walk-through[/bold magenta]\n")
    console.print("1) Client creates a ConcreteCommand (binds receiver).")
    time.sleep(0.6)
    console.print("2) Invoker executes the command and pushes it onto a history stack.")
    time.sleep(0.6)
    console.print("3) To undo, the Invoker pops the last command and calls undo().")
    time.sleep(0.6)
    console.print("4) To replay, the Invoker re-executes commands from history in order.\n")
    time.sleep(0.6)

    console.print("[bold yellow]TL;DR[/bold yellow]")
    console.print("Encapsulate actions as objects → store/queue/undo/replay them easily. Great for UI actions, macros, and transactional workflows.\n")

    console.print("[italic green]Try the Robot Commander game now to see execute/undo/replay in action![/italic green]\n")
