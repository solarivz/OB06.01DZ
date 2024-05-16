from abc import ABC, abstractmethod
import random

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

class Interface(ABC):
    @abstractmethod
    def display_menu(self):
        pass

    @abstractmethod
    def get_menu_choice(self):
        pass

    @abstractmethod
    def display_first_attacker(self, attacker):
        pass

    @abstractmethod
    def display_attack(self, attacker, defender):
        pass

    @abstractmethod
    def display_winner(self, winner):
        pass

class ConsoleInterface(Interface):
    def display_menu(self):
        print("=== Битва героев ===")
        print("1. Начать новую игру")
        print("2. Выйти из игры")

    def get_menu_choice(self):
        choice = input("Выберите действие: ")
        return choice

    def display_first_attacker(self, attacker):
        print(f"{attacker.name} начинает первым!")

    def display_attack(self, attacker, defender):
        print(f"{attacker.name} атакует {defender.name}. Здоровье {defender.name}: {defender.health}")

    def display_winner(self, winner):
        print(f"Победитель: {winner.name}")


class Hero(HeroA):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.health = random.randint(80, 120)
        self.attack_power = random.randint(15, 25)

    def attack(self, other):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0


class Game(GameA):
    def __init__(self, player, computer, interface):
        super().__init__(player, computer)
        self.player = player
        self.computer = computer
        self.interface = interface
        self.first_attacker = None

    def determine_first_attacker(self):
        self.first_attacker = random.choice([self.player, self.computer])

    def start(self):
        self.determine_first_attacker()
        self.interface.display_first_attacker(self.first_attacker)
        while self.player.is_alive() and self.computer.is_alive():
            if self.first_attacker == self.player:
                self.player_attack()
                if not self.computer.is_alive():
                    break
                self.computer_attack()
            else:
                self.computer_attack()
                if not self.player.is_alive():
                    break
                self.player_attack()

        if self.player.is_alive():
            self.interface.display_winner(self.player)
        else:
            self.interface.display_winner(self.computer)

    def player_attack(self):
        self.player.attack(self.computer)
        self.interface.display_attack(self.player, self.computer)

    def computer_attack(self):
        self.computer.attack(self.player)
        self.interface.display_attack(self.computer, self.player)




class ConsoleGame:
    def __init__(self, interface):
        self.interface = interface
        self.player = Hero("Player")
        self.computer = Hero("Computer")
        self.game = Game(self.player, self.computer, self.interface)

    def run(self):
        self.interface.display_menu()
        choice = self.interface.get_menu_choice()
        if choice == "1":
            self.game.start()
        elif choice == "2":
            print("Игра завершена.")
        else:
            print("Неверный выбор.")


# Тестирование:
if __name__ == "__main__":
    interface = ConsoleInterface()
    game = ConsoleGame(interface)
    game.run()

