class Message:
    """
    Represents a single message to be sent
    Parameters
    ----------
    message_type : str; one of statement, carousel, list, media
    """
    def __init__(self, message_type):
        self.message_type = message_type
