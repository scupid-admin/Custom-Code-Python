import json


class Action:
    def __init__(self, name):
        self.name = name


class GoToFlow(Action):
    def __init__(self, flow_title):
        Action.__init__(self, name="goToFlow")
        self.flow_title = flow_title

    def to_json(self):
        attr = {'name': self.name, 'nextFlowTitle': self.flow_title}
        return json.dumps(attr)


class SetVariable(Action):
    def __init__(self, variable_scope, variable_title, variable):
        Action.__init__(self, name="setVariableAction")
        self.variable_scope = variable_scope
        self.variable_title = variable_title
        self.variable = variable

    def to_json(self):
        attr = {'name': self.name, 'variableScope': self.variable_scope, 'variableTitle': self.variable_title,
                'variable': self.variable.to_json()}
        return json.dumps(attr)


class Publish(Action):
    def __init__(self):
        Action.__init__(self, name="publish")
        self.messages = []

    def add_message(self, message):
        self.messages.extend(message)

    def to_json(self):
        attr = {'name': self.name, 'simplifiedMessage': [message.to_json() for message in self.messages]}
        return json.dumps(attr)
