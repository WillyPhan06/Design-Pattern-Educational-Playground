from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import random

console = Console()

# Observer interface
class Observer:
    def update(self, temperature, humidity, pressure):
        raise NotImplementedError

# Subject interface
class Subject:
    def register_observer(self, observer):
        raise NotImplementedError

    def remove_observer(self, observer):
        raise NotImplementedError

    def notify_observers(self):
        raise NotImplementedError

# Concrete Subject
class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    # Simulate new weather measurement
    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()

# Concrete Observers
class PhoneDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        console.print(f"[cyan]Phone Display:[/cyan] Temp: {temperature}°C, Humidity: {humidity}%, Pressure: {pressure} hPa")

class WebDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        console.print(f"[magenta]Web Display:[/magenta] Temp: {temperature}°C, Humidity: {humidity}%, Pressure: {pressure} hPa")

class TVDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        console.print(f"[yellow]TV Display:[/yellow] Temp: {temperature}°C, Humidity: {humidity}%, Pressure: {pressure} hPa")

# Game function
def run_game():
    console.print("[bold cyan]Observer Pattern - Weather Station[/bold cyan]\n")

    weather_data = WeatherData()

    phone_display = PhoneDisplay()
    web_display = WebDisplay()
    tv_display = TVDisplay()

    weather_data.register_observer(phone_display)
    weather_data.register_observer(web_display)
    weather_data.register_observer(tv_display)

    while True:
        console.print("\nActions:")
        console.print("1. Update Weather")
        console.print("0. Exit")

        choice = Prompt.ask("Choose action", choices=["0","1"])

        if choice == "0":
            console.print("\n👋 Exiting Weather Station...\n")
            break
        else:
            temp = random.randint(-10, 40)
            humidity = random.randint(0, 100)
            pressure = random.randint(950, 1050)
            console.print(f"\n[bold green]New Weather Measurements: Temp={temp}°C, Humidity={humidity}%, Pressure={pressure} hPa[/bold green]\n")
            weather_data.set_measurements(temp, humidity, pressure)
