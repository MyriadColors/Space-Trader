class State:

    def __init__(self, game) -> None:
        self.game = game

    def handle_events(self, events: list) -> None:
        pass

    def update(self, actions) -> None:
        pass

    def render(self, canvas) -> None:
        pass
