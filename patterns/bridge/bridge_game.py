from rich.console import Console
from rich.prompt import IntPrompt

console = Console()


class Device:
    def __init__(self, name):
        self.name = name
        self.is_on = False
        self.volume = 5
        self.channel = 1

    def turn_on(self):
        self.is_on = True
        console.print(f"🔌 [green]{self.name} turned ON.[/green]")

    def turn_off(self):
        self.is_on = False
        console.print(f"🪫 [red]{self.name} turned OFF.[/red]")

    def set_volume(self, level):
        self.volume = max(0, min(level, 10))
        console.print(f"🔊 {self.name} volume set to [bold cyan]{self.volume}[/bold cyan].")

    def set_channel(self, channel):
        self.channel = channel
        console.print(f"📺 {self.name} switched to channel [bold yellow]{self.channel}[/bold yellow].")


class TV(Device):
    def __init__(self):
        super().__init__("TV")


class Radio(Device):
    def __init__(self):
        super().__init__("Radio")


# Abstraction
class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        if self.device.is_on:
            self.device.turn_off()
        else:
            self.device.turn_on()

    def volume_up(self):
        self.device.set_volume(self.device.volume + 1)

    def volume_down(self):
        self.device.set_volume(self.device.volume - 1)


# Refined Abstraction
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        if self.device.is_on:
            self.device.set_volume(0)
            console.print("🔇 [yellow]Muted[/yellow].")
        else:
            console.print("⚠️ [red]Device is off![/red]")

    def change_channel(self):
        if self.device.is_on:
            channel = IntPrompt.ask("Enter new channel number", default=self.device.channel)
            self.device.set_channel(channel)
        else:
            console.print("⚠️ [red]Device is off![/red]")


def run_game():
    console.print("[bold cyan]Bridge Pattern - Universal Remote Simulator[/bold cyan]\n")

    # Choose device
    console.print("Select a device:")
    console.print("1. TV 📺")
    console.print("2. Radio 📻")
    device_choice = IntPrompt.ask("Enter choice", choices=["1", "2"])

    device = TV() if device_choice == 1 else Radio()

    # Choose remote
    console.print("\nSelect a remote:")
    console.print("1. Basic Remote")
    console.print("2. Advanced Remote")
    remote_choice = IntPrompt.ask("Enter choice", choices=["1", "2"])

    remote = RemoteControl(device) if remote_choice == 1 else AdvancedRemoteControl(device)

    # Control loop
    while True:
        console.print("\n[bold green]Actions:[/bold green]")
        console.print("1. Toggle Power")
        console.print("2. Volume Up")
        console.print("3. Volume Down")

        if isinstance(remote, AdvancedRemoteControl):
            console.print("4. Mute")
            console.print("5. Change Channel")

        console.print("0. Exit")

        choice = IntPrompt.ask("Choose action", choices=["0", "1", "2", "3", "4", "5"])

        if choice == 0:
            console.print("👋 Exiting Remote Simulator...\n")
            break
        elif choice == 1:
            remote.toggle_power()
        elif choice == 2:
            remote.volume_up()
        elif choice == 3:
            remote.volume_down()
        elif choice == 4 and isinstance(remote, AdvancedRemoteControl):
            remote.mute()
        elif choice == 5 and isinstance(remote, AdvancedRemoteControl):
            remote.change_channel()
        else:
            console.print("⚠️ Invalid choice for this remote type.")
