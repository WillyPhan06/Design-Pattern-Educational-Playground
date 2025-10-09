from rich.console import Console
from rich.prompt import Prompt

console = Console()

# Abstract Expression
class Expression:
    def interpret(self):
        raise NotImplementedError

# Terminal Expression for numbers
class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self):
        return self.value

# Non-terminal Expression for operations
class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

class Subtract(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

class Multiply(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() * self.right.interpret()

class Divide(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() / self.right.interpret()

# Simple parser for "number operator number" expressions
def parse_expression(expr_str):
    tokens = expr_str.split()
    if len(tokens) != 3:
        return None
    left, op, right = tokens
    try:
        left = Number(float(left))
        right = Number(float(right))
    except ValueError:
        return None

    if op == '+':
        return Add(left, right)
    elif op == '-':
        return Subtract(left, right)
    elif op == '*':
        return Multiply(left, right)
    elif op == '/':
        return Divide(left, right)
    else:
        return None

# Game function
def run_game():
    console.print("[bold cyan]Interpreter Pattern - Math Expression Evaluator[/bold cyan]\n")

    while True:
        console.print("Enter expression in format: number operator number (e.g., 2 + 3)")
        console.print("Operators: + - * /")
        console.print("Type '0' to exit.\n")

        expr_input = Prompt.ask("Your expression")
        if expr_input.strip() == '0':
            console.print("\n👋 Exiting Math Expression Evaluator...\n")
            break

        expr = parse_expression(expr_input)
        if expr:
            result = expr.interpret()
            console.print(f"[green]Result:[/green] {result}")
        else:
            console.print("[red]Invalid expression! Try again.[/red]")
