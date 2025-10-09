# patterns/command/command_game.py
from rich.console import Console
from rich.table import Table
import time
import os

console = Console()

# ==== Command Interface ====
class Command:
    def execute(self):
        pass
    def undo(self):
        pass

# ==== Receiver (Robot) ====
class Robot:
    def __init__(self, grid_size=5):
        self.grid_size = grid_size
        self.x = grid_size // 2
        self.y = grid_size // 2
        self.direction = 'N'  # N, E, S, W
        self.directions = ['N', 'E', 'S', 'W']
        self.symbols = {'N': '↑ ', 'E': '→ ', 'S': '↓ ', 'W': '← '}

    def move_forward(self):
        if self.direction == 'N' and self.y > 0:
            self.y -= 1
        elif self.direction == 'S' and self.y < self.grid_size - 1:
            self.y += 1
        elif self.direction == 'E' and self.x < self.grid_size - 1:
            self.x += 1
        elif self.direction == 'W' and self.x > 0:
            self.x -= 1
        else:
            console.print("[red]⚠ Robot can't move outside the grid![/red]")
        self.display()

    def turn_left(self):
        i = self.directions.index(self.direction)
        self.direction = self.directions[(i - 1) % 4]
        self.display()

    def turn_right(self):
        i = self.directions.index(self.direction)
        self.direction = self.directions[(i + 1) % 4]
        self.display()

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("[bold cyan]🤖 Robot Commander - Command Pattern[/bold cyan]\n")
        for y in range(self.grid_size):
            row = ""
            for x in range(self.grid_size):
                if x == self.x and y == self.y:
                    row += f"[bold yellow]{self.symbols[self.direction]}[/bold yellow] "
                else:
                    row += "⬜ "
            console.print(row)
        console.print(f"\nFacing: [bold]{self.direction}[/bold] | Position: ({self.x + 1}, {self.y + 1})\n")

# ==== Concrete Commands ====
class MoveForwardCommand(Command):
    def __init__(self, robot):
        self.robot = robot
        self.prev_x = None
        self.prev_y = None

    def execute(self):
        self.prev_x, self.prev_y = self.robot.x, self.robot.y
        self.robot.move_forward()

    def undo(self):
        self.robot.x, self.robot.y = self.prev_x, self.prev_y
        self.robot.display()

class TurnLeftCommand(Command):
    def __init__(self, robot):
        self.robot = robot
        self.prev_dir = None

    def execute(self):
        self.prev_dir = self.robot.direction
        self.robot.turn_left()

    def undo(self):
        self.robot.direction = self.prev_dir
        self.robot.display()

class TurnRightCommand(Command):
    def __init__(self, robot):
        self.robot = robot
        self.prev_dir = None

    def execute(self):
        self.prev_dir = self.robot.direction
        self.robot.turn_right()

    def undo(self):
        self.robot.direction = self.prev_dir
        self.robot.display()

# ==== Invoker (Command Manager) ====
class CommandManager:
    def __init__(self):
        self.history = []
        self.redo_stack = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)
        self.redo_stack.clear()

    def undo(self):
        if not self.history:
            console.print("[red]No commands to undo![/red]")
            return
        cmd = self.history.pop()
        cmd.undo()
        self.redo_stack.append(cmd)

    def replay(self):
        if not self.history:
            console.print("[red]No commands to replay![/red]")
            return
        console.print("\n[bold green]Replaying commands...[/bold green]\n")
        time.sleep(1)
        for cmd in self.history:
            cmd.execute()
            time.sleep(0.3)

# ==== Game Runner ====
def run_game():
    robot = Robot(grid_size=5)
    manager = CommandManager()
    robot.display()

    while True:
        console.print("[bold cyan]\nCommands:[/bold cyan]")
        console.print("1️⃣ Move Forward\n2️⃣ Turn Left\n3️⃣ Turn Right\n4️⃣ Undo Last Command\n5️⃣ Replay All Commands\n0️⃣ Exit\n")

        choice = console.input("[bold yellow]Choose an action:[/bold yellow] ").strip()

        if choice == "1":
            manager.execute_command(MoveForwardCommand(robot))
        elif choice == "2":
            manager.execute_command(TurnLeftCommand(robot))
        elif choice == "3":
            manager.execute_command(TurnRightCommand(robot))
        elif choice == "4":
            manager.undo()
        elif choice == "5":
            manager.replay()
        elif choice == "0":
            console.print("[bold red]Exiting Robot Commander...[/bold red]")
            break
        else:
            console.print("[red]Invalid choice. Try again.[/red]")
        time.sleep(0.4)
