class Action:
    def __init__(self, name):
        self.name = name


class GoToFlow(Action):
    def __init__(self, flow_title):
        Action.__init__(self, name="goToFlow")
        self.flow_title = flow_title


class SetVariable(Action):
    def __init__(self):
        Action.__init__(self, name="setVariableAction")


class Publish(Action):
    def __init__(self):
        Action.__init__(self, name="publish")