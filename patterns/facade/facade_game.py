from rich.console import Console
from rich.prompt import Prompt
from rich.progress import Progress, BarColumn, TimeElapsedColumn
from time import sleep

console = Console()

# ASCII Images
COMPUTER_OFF = """
      _______
     |       |
     |  OFF  |
     |_______|
"""
COMPUTER_ON = """
      _______
     |       |
     |  ON   |
     |_______|
"""

# Subsystems
class CPU:
    def start(self):
        self._load("CPU powered on")
    def shutdown(self):
        self._load("CPU powered down")
    def _load(self, message):
        with Progress("[progress.description]{task.description}", BarColumn(), TimeElapsedColumn()) as progress:
            task = progress.add_task(f"{message}", total=100)
            for _ in range(20):
                progress.update(task, advance=5)
                sleep(0.05)

class GPU:
    def start(self):
        self._load("GPU initialized")
    def shutdown(self):
        self._load("GPU shut down")
    def _load(self, message):
        with Progress("[progress.description]{task.description}", BarColumn(), TimeElapsedColumn()) as progress:
            task = progress.add_task(f"{message}", total=100)
            for _ in range(20):
                progress.update(task, advance=5)
                sleep(0.05)

class RAM:
    def start(self):
        self._load("RAM loaded")
    def shutdown(self):
        self._load("RAM cleared")
    def _load(self, message):
        with Progress("[progress.description]{task.description}", BarColumn(), TimeElapsedColumn()) as progress:
            task = progress.add_task(f"{message}", total=100)
            for _ in range(20):
                progress.update(task, advance=5)
                sleep(0.05)

class HardDrive:
    def start(self):
        self._load("Hard Drive spinning up")
    def shutdown(self):
        self._load("Hard Drive spun down")
    def _load(self, message):
        with Progress("[progress.description]{task.description}", BarColumn(), TimeElapsedColumn()) as progress:
            task = progress.add_task(f"{message}", total=100)
            for _ in range(20):
                progress.update(task, advance=5)
                sleep(0.05)

class Network:
    def start(self):
        self._load("Network connected")
    def shutdown(self):
        self._load("Network disconnected")
    def _load(self, message):
        with Progress("[progress.description]{task.description}", BarColumn(), TimeElapsedColumn()) as progress:
            task = progress.add_task(f"{message}", total=100)
            for _ in range(20):
                progress.update(task, advance=5)
                sleep(0.05)

# Facade
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.gpu = GPU()
        self.ram = RAM()
        self.hdd = HardDrive()
        self.network = Network()
        self.on = False

    def start(self):
        console.print(COMPUTER_ON)
        console.print("[bold green]Starting Computer (Facade)...[/bold green]")
        self.cpu.start()
        self.gpu.start()
        self.ram.start()
        self.hdd.start()
        self.network.start()
        self.on = True
        console.print("[bold cyan]💻 Computer is now ON![/bold cyan]\n")

    def shutdown(self):
        console.print(COMPUTER_OFF)
        console.print("[bold red]Shutting Down Computer (Facade)...[/bold red]")
        self.network.shutdown()
        self.hdd.shutdown()
        self.ram.shutdown()
        self.gpu.shutdown()
        self.cpu.shutdown()
        self.on = False
        console.print("[bold magenta]🛑 Computer is now OFF![/bold magenta]\n")

    def open_internals(self):
        console.print("[bold yellow]Opening Computer Internals...[/bold yellow]")
        while True:
            console.print("\nSubsystems:")
            console.print("1. CPU")
            console.print("2. GPU")
            console.print("3. RAM")
            console.print("4. Hard Drive")
            console.print("5. Network")
            console.print("0. Back")
            choice = Prompt.ask("Choose subsystem to toggle start/shutdown", choices=["0","1","2","3","4","5"])
            if choice == "0":
                break
            subsystem = {"1": self.cpu, "2": self.gpu, "3": self.ram, "4": self.hdd, "5": self.network}[choice]
            action = Prompt.ask("Action?", choices=["start","shutdown"])
            if action == "start":
                subsystem.start()
            else:
                subsystem.shutdown()

def run_game():
    console.print("[bold cyan]Facade Pattern - Computer Startup Simulator (Interactive)[/bold cyan]\n")
    computer = Computer()

    while True:
        console.print("Actions:")
        console.print("1. Start Computer (Facade)")
        console.print("2. Shutdown Computer (Facade)")
        console.print("3. Open Internals (Interact with Subsystems)")
        console.print("0. Exit")

        choice = Prompt.ask("Choose action", choices=["0","1","2","3"])

        if choice == "0":
            console.print("\n👋 Exiting Computer Simulator...\n")
            break
        elif choice == "1":
            computer.start()
        elif choice == "2":
            computer.shutdown()
        elif choice == "3":
            computer.open_internals()
