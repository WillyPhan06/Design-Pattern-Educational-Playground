from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

console = Console()

# Real Subject: BankVault
class BankVault:
    def __init__(self):
        self.contents = ["Gold Bars", "Diamond Necklace", "Secret Documents"]

    def access_contents(self):
        console.print("[green]Access granted! Contents of the vault:[/green]")
        for item in self.contents:
            console.print(f"- {item}")

# Proxy: VaultProxy
class VaultProxy:
    def __init__(self, vault):
        self.vault = vault
        self.authorized_users = ["admin", "manager"]
        self.failed_attempts = {}

    def access_contents(self, username):
        if username in self.authorized_users:
            console.print(f"[cyan]Welcome, {username}![/cyan]")
            self.vault.access_contents()
        else:
            self.failed_attempts[username] = self.failed_attempts.get(username, 0) + 1
            console.print(f"[red]Access denied for {username}![/red] Attempt #{self.failed_attempts[username]}")

def run_game():
    console.print("[bold cyan]Proxy Pattern - Bank Vault Simulator[/bold cyan]\n")
    vault = BankVault()
    proxy = VaultProxy(vault)

    while True:
        console.print("\nActions:")
        console.print("1. Access Vault")
        console.print("2. Show Failed Attempts")
        console.print("0. Exit")

        choice = Prompt.ask("Choose action", choices=["0","1","2"])

        if choice == "0":
            console.print("\n👋 Exiting Proxy Simulator...\n")
            break

        elif choice == "1":
            username = Prompt.ask("Enter your username")
            proxy.access_contents(username)

        elif choice == "2":
            if not proxy.failed_attempts:
                console.print("[yellow]No failed attempts yet.[/yellow]")
            else:
                table = Table(title="Failed Access Attempts")
                table.add_column("Username")
                table.add_column("Attempts")
                for user, count in proxy.failed_attempts.items():
                    table.add_row(user, str(count))
                console.print(table)
