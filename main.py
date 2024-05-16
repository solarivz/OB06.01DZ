from abc import ABC, abstractmethod

class HeroA(ABC):
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    @abstractmethod
    def attack(self, other):
        pass

    @abstractmethod
    def is_alive(self):
        pass

class GameA(ABC):
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    @abstractmethod
    def start(self):
        pass

class Hero(HeroA):
    def attack(self, other):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0


class Game(GameA):

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            print(
                f"{self.player.name} атакует {self.computer.name}. {self.computer.name} здоровье: {self.computer.health}")
            if self.computer.is_alive():
                self.computer.attack(self.player)
                print(
                    f"{self.computer.name} атакует {self.player.name}. {self.player.name} здоровье: {self.player.health}")

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

class ConsoleInterface:
    @staticmethod
    def display_menu():
        print("=== Битва героев ===")
        print("1. Начать новую игру")
        print("2. Выйти из игры")

    @staticmethod
    def get_menu_choice():
        choice = input("Выберите действие: ")
        return choice

    @staticmethod
    def display_game_state(player, computer):
        print("=== Состояние игры ===")
        print(f"Ваше здоровье: {player.health}")
        print(f"Здоровье компьютера: {computer.health}")

    @staticmethod
    def display_winner(winner):
        print(f"Победитель: {winner}")


