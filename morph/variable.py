class Variable:
    def __init__(self, type):
        self.type = type


class StringVariable(Variable):
    def __init__(self, value):
        Variable.__init__(self, "STRING")
        self.value = value


class StringArrayVariable(Variable):
    def __init__(self, values):
        Variable.__init__(self, "STRING_ARRAY")
        self.values = values


class NumberVariable(Variable):
    def __init__(self, value):
        Variable.__init__(self, "DOUBLE")
        self.value = value