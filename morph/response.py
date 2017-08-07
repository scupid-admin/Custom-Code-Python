from morph.base import MorphSerializable


class Response(MorphSerializable):
    def __init__(self):
        MorphSerializable.__init__(self, ["actions"], None)
        self.actions = []

    def add_action(self, action):
        self.actions.extend(action)
        return self

    def build(self):
        pass
