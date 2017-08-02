class Message:
    """
    Represents a single message to be sent
    """

    def __init__(self, message_type):
        """
        Parameters
        :param message_type: str; one of statement, carousel, list, media
        """
        self.message_type = message_type
        self.suggestions = []

    def add_suggestion(self, suggestion):
        """
        Adds a suggestion to this message
        :param suggestion: Suggestion type.
        :return: self
        """
        self.suggestions.extend(suggestion)
        return self


class CarousalMessage(Message):
    """
    Represents a carousal message
    """

    def __init__(self):
        Message.__init__(self, "carousel")


class CarousalElement:
    def __init__(self, title, sub_title, image_url, click_url):
        self.image_url = image_url
        self.sub_title = sub_title
        self.title = title
        self.click_url = click_url
        self.buttons = []

    def add_button(self, button):
        self.buttons.extend(button)


class Button:
    def __init__(self, title, button_type):
        self.button_type = button_type
        self.title = title


class URLButton(Button):
    def __init__(self, title, url, height):
        Button.__init__(self, title, "URL")
        self.height = height
        self.url = url


class Suggestion:
    """
    Represents a suggestion, aka quick replies
    """

    def __init__(self, title, suggestion_type, payload, image_url):
        """
        Constructor

        :param title: str, The title of the suggestion
        :param suggestion_type: str, One of LOCATION or TEXT
        :param payload: str, The payload to be sent when someone clicks it
        :param image_url: str, The URL of the logo image
        """
        self.imageUrl = image_url
        self.payload = payload
        self.suggestion_type = suggestion_type
        self.title = title
