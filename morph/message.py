import json


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
        self.elements = []

    def add_carousal_element(self, element):
        self.elements.extend(element)

    def to_json(self):
        attr = {'messageType': self.message_type}
        if len(self.suggestions) > 0:
            attr['suggestionElements'] = [suggestion.to_json() for suggestion in self.suggestions]
        attr['carousalElements'] = [element.to_json() for element in self.elements]
        return json.dumps(attr)


class ListMessage(CarousalMessage):
    def __init__(self):
        CarousalMessage.__init__(self)
        self.cover = True
        self.message_type = "list"


class MediaMessage(Message):
    def __init__(self, media_url, media_type):
        Message.__init__(self, "media")
        self.media_url = media_url
        self.media_type = media_type


class TextMessage(Message):
    def __init__(self, text):
        Message.__init__(self, "statement")
        self.text = text
        self.buttons = []

    def add_button(self, button):
        self.buttons.extend(button)


class CarousalElement:
    def __init__(self, title, sub_title, image_url, click_url):
        self.image_url = image_url
        self.sub_title = sub_title
        self.title = title
        self.click_url = click_url
        self.buttons = []

    def add_button(self, button):
        self.buttons.extend(button)

    def to_json(self):
        attr = {'title': self.title, 'subtitle': self.sub_title, 'imageUrl': self.image_url, 'clickUrl': self.click_url}
        if len(self.buttons) > 0:
            attr['buttons'] = [button.to_json() for button in self.buttons]
        return json.dumps(attr)


class Button:
    def __init__(self, title, button_type):
        self.button_type = button_type
        self.title = title


class URLButton(Button):
    def __init__(self, title, url, height):
        Button.__init__(self, title, "URL")
        self.height = height
        self.url = url

    def to_json(self):
        attr = {'buttonType': self.button_type, 'webviewHeightRatio': self.height, 'url': self.url, 'title': self.title}
        return json.dumps(attr)


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

    def to_json(self):
        attr = {'title': self.title, 'suggestionType': self.suggestion_type, 'payload': self.payload,
                'imageUrl': self.imageUrl}
        return json.dumps(attr)
