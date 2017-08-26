"""
Your code basically returns a list of actions. This is the goal of your code.

There are 3 type of Actions that you can add.
1) GoToFlow - Used for jumping to a conversation
2) SetVariable - Used for setting an attribute
3) Publish - Used to reply back to the user

Actions are executed in the order that you send them.
"""


class Action:
    """
    Base class for Action
    """

    def __init__(self, name):
        self.name = name


class GoToFlow(Action):
    """
    Use this Action when you want to jump to a conversation
    """

    def __init__(self, flow_title):
        """
        Parameters
        -------------
        flow_title: str;
        """
        Action.__init__(self, name="goToFlow")
        self.flow_title = flow_title

    def to_json(self):
        attr = {'name': self.name, 'nextFlowTitle': self.flow_title}
        return attr


class SetVariable(Action):
    def __init__(self, variable_scope, variable_title, variable):
        Action.__init__(self, name="setVariableAction")
        self.variable_scope = variable_scope
        self.variable_title = variable_title
        self.variable = variable

    def to_json(self):
        attr = {'name': self.name, 'variableScope': self.variable_scope, 'variableTitle': self.variable_title,
                'variable': self.variable.to_json()}
        return attr


class Publish(Action):
    def __init__(self):
        Action.__init__(self, name="publish")
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def to_json(self):
        # attr = {'name': self.name, 'simplifiedMessage': [message.to_json() for message in self.messages]}
        attr = {'name': self.name, 'simplifiedMessage': {'messages': [message.to_json() for message in self.messages]}}
        return attr
