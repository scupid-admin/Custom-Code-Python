class MorphSerializable:
    def __init__(self, properties_to_serialize, property_dict):
        self.property_dict = property_dict
        self.properties_to_serialize = properties_to_serialize
