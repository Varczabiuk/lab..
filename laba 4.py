# === Composite Pattern ===

class GameComponent:
    def show(self):
        raise NotImplementedError()


# Leaf — окрема гра
class GameItem(GameComponent):
    def __init__(self, game):
        self.game = game

    def show(self):
        self.game.show()


# Composite — колекція ігор
class GameCollection(GameComponent):
    def __init__(self, name):
        self.name = name
        self.games = []

    def add(self, component: GameComponent):
        self.games.append(component)

    def remove(self, component: GameComponent):
        self.games.remove(component)

    def show(self):
        print(f"\n Колекція: {self.name}")
        for game in self.games:
            game.show()


# === Конкретні типи ігор ===

class ActionGame:
    def __init__(self, title, developer, difficulty):
        self.title = title
        self.developer = developer
        self.difficulty = difficulty

    def show(self):
        print(f"[Action] {self.title} — by {self.developer} (Difficulty: {self.difficulty})")


class StrategyGame:
    def __init__(self, title, developer, players):
        self.title = title
        self.developer = developer
        self.players = players

    def show(self):
        print(f"[Strategy] {self.title} — {self.players}-player by {self.developer}")


# === Facade Pattern ===

class GameLibraryManager:
    def __init__(self):
        self.root_collection = GameCollection("Моя Ігрова Бібліотека")

    def add_action_game(self, title, developer, difficulty):
        game = ActionGame(title, developer, difficulty)
        self.root_collection.add(GameItem(game))

    def add_strategy_game(self, title, developer, players):
        game = StrategyGame(title, developer, players)
        self.root_collection.add(GameItem(game))

    def create_collection(self, name):
        group = GameCollection(name)
        self.root_collection.add(group)
        return group

    def add_to_collection(self, group: GameCollection, item: GameComponent):
        group.add(item)

    def show_all(self):
        self.root_collection.show()


# === Консольна демонстрація ===

def run_game_library_demo():
    manager = GameLibraryManager()

    print("== Додавання ігор ==")
    manager.add_action_game("CyberBlade", "NeoGames", "Hard")
    manager.add_strategy_game("Empire Mind", "LogicSoft", 4)

    print("\n== Створення підколекції ==")
    classics = manager.create_collection("Класичні Ігри")
    manager.add_to_collection(classics, GameItem(ActionGame("Retro Runner", "OldStudio", "Easy")))
    manager.add_to_collection(classics, GameItem(StrategyGame("Battle Grid", "TactiCorp", 2)))

    print("\n== Вміст бібліотеки ==")
    manager.show_all()


if __name__ == "__main__":
    run_game_library_demo()
