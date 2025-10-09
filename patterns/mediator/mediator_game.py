from rich.console import Console
from rich.prompt import Prompt

console = Console()

# Mediator Interface
class ChatRoomMediator:
    def show_message(self, user, message):
        raise NotImplementedError

# Concrete Mediator
class ChatRoom(ChatRoomMediator):
    def __init__(self):
        self.users = []

    def register_user(self, user):
        self.users.append(user)
        user.mediator = self

    def show_message(self, sender, message):
        for user in self.users:
            if user != sender:
                console.print(f"[cyan]{sender.name} -> ChatRoom -> {user.name}[/cyan]: {message}")


# Colleague
class User:
    def __init__(self, name):
        self.name = name
        self.mediator = None

    def send_message(self, message):
        if self.mediator:
            self.mediator.show_message(self, message)

# Game function
def run_game():
    console.print("[bold cyan]Mediator Pattern - Chat Room Simulator[/bold cyan]\n")

    chat_room = ChatRoom()

    # Registering users
    alice = User("Alice")
    bob = User("Bob")
    charlie = User("Charlie")

    chat_room.register_user(alice)
    chat_room.register_user(bob)
    chat_room.register_user(charlie)

    users = {"1": alice, "2": bob, "3": charlie}

    while True:
        console.print("\nUsers:")
        console.print("1. Alice")
        console.print("2. Bob")
        console.print("3. Charlie")
        console.print("0. Exit")

        choice = Prompt.ask("Select user to send message", choices=["0","1","2","3"])

        if choice == "0":
            console.print("\n👋 Exiting Chat Room Simulator...\n")
            break
        else:
            user = users[choice]
            message = Prompt.ask(f"Enter message as {user.name}")
            user.send_message(message)
