import json


class Variable:
    def __init__(self, type):
        self.type = type


class StringVariable(Variable):
    def __init__(self, value):
        Variable.__init__(self, "STRING")
        self.value = value

    def to_json(self):
        attr = {'variableType': self.type, 'value': self.value}
        return json.dumps(attr)


class StringArrayVariable(Variable):
    def __init__(self, values):
        Variable.__init__(self, "STRING_ARRAY")
        self.values = values

    def to_json(self):
        attr = {'variableType': self.type, 'values': self.values}
        return json.dumps(attr)


class NumberVariable(Variable):
    def __init__(self, value):
        Variable.__init__(self, "DOUBLE")
        self.value = value

    def to_json(self):
        attr = {'variableType': self.type, 'value': self.value}
        return json.dumps(attr)
