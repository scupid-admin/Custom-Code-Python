class Response:
    def __init__(self):
        self.actions = []

    def add_action(self, action):
        self.actions.extend(action)