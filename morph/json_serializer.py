class JsonSerializer:
    def __init__(self):
        pass

    def serialize(self, o):
        properties = o.properties_to_serialize()
        properties_dict = o.properties_dict()