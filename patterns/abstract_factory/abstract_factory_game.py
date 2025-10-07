# patterns/abstract_factory/abstract_factory_game.py
from rich.console import Console
from rich.prompt import IntPrompt
from rich.panel import Panel

console = Console()

def run_game():
    console.print("[bold cyan]Abstract Factory - Interactive Mini-Game[/bold cyan]\n")

    families = ["Modern", "Victorian"]
    products = ["Chair", "Sofa"]
    created_objects = []

    while True:
        console.print(Panel.fit("[1] Modern  |  [2] Victorian  |  [0] Exit", title="Choose a product family"))
        family_choice = IntPrompt.ask("Select a family", default=0)

        if family_choice == 0:
            console.print("[bold yellow]Returning to main menu...[/bold yellow]\n")
            break
        elif family_choice in [1, 2]:
            family_name = families[family_choice - 1]

            # User chooses object
            console.print(Panel.fit("[1] Chair  |  [2] Sofa  |  [0] Back", title=f"{family_name} Family - Choose object"))
            obj_choice = IntPrompt.ask("Select an object", default=0)

            if obj_choice == 0:
                continue
            elif obj_choice in [1, 2]:
                product_name = products[obj_choice - 1]
                created_objects.append((family_name, product_name))
                console.print(f"[green]Created {family_name} {product_name}[/green]\n")

                # Display last 2 objects only
                display_objects = created_objects[-2:]
                obj_str = " | ".join([f"{fam} {prod}" for fam, prod in display_objects])
                console.print(f"Recent objects: {obj_str}\n")

                # If we have at least 2 objects, ask relationship quiz
                if len(created_objects) >= 2:
                    obj1 = created_objects[-2]
                    obj2 = created_objects[-1]

                    console.print("[bold magenta]Quiz: What's the relationship between the last two objects?[/bold magenta]")
                    console.print(f"1️⃣ Same family, same object")
                    console.print(f"2️⃣ Same family, different object")
                    console.print(f"3️⃣ Same object, different family")
                    console.print(f"4️⃣ Different object, different family")

                    answer = IntPrompt.ask("Your answer (1-4)", default=2)

                    # Determine correct answer
                    if obj1[0] == obj2[0] and obj1[1] != obj2[1]:
                        correct = 2
                    elif obj1[0] == obj2[0] and obj1[1] == obj2[1]:
                        correct = 1
                    elif obj1[0] != obj2[0] and obj1[1] == obj2[1]:
                        correct = 3
                    else:
                        correct = 4

                    if answer == correct:
                        console.print("[bold green]Correct! ✅[/bold green]\n")
                    else:
                        console.print(f"[bold red]Incorrect! ❌ The correct answer was {correct}[/bold red]\n")

            else:
                console.print("[red]Invalid object choice.[/red]\n")
        else:
            console.print("[red]Invalid family choice.[/red]\n")
