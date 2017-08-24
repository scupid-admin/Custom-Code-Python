import json
from morph.base import MorphSerializable


class Response(MorphSerializable):
    def __init__(self):
        MorphSerializable.__init__(self, ["actions"], None)
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)
        return self

    def build(self):
        attr = {'actions': [action.to_json() for action in self.actions]}
        return json.dumps(attr)
