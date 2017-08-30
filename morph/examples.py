from morph.response import Response
from morph.action import *
from morph.variable import *
from morph.message import *


def read_and_set_attribute(event, context):
    response = Response()

    number_dict = {
        "9711xxx400": True,
        "8130xxx599": True
    }
    phone_number = context["userVariables"]["_PHONE_NUMBER"]
    if phone_number is None:
        phone_number = ""
    else:
        phone_number = str(phone_number)

    if phone_number in number_dict.keys():
        # This is creating a variable. Variables can be of different kinds. See variable.py. They can be
        # StringVariable, NumberVariable, StringArrayVariable
        #
        # variable_scope can be either USER or FLOW
        variable = SetVariable(variable_scope="USER", variable_title="Valid Customer", variable=StringVariable("true"))
        response.add_action(variable)
    else:
        # This redirects user to a new conversation called "number invalid"
        response.add_action(GoToFlow("number invalid"))
    return response.build()


def text_payload(event, context):
    publish_action = Publish()
    text_message = TextMessage("Hello, please select options from below.")
    complaint_suggestion = Suggestion("File a complain", "TEXT", "complaint", None)
    demo_suggestion = Suggestion("Schedule a demo", "TEXT", "demo", None)
    text_message.add_suggestion(complaint_suggestion)
    text_message.add_suggestion(demo_suggestion)
    publish_action.add_message(text_message)

    return Response().add_action(publish_action).build()


def carousal(event, context):
    publish_action = Publish()
    carousal_message = CarousalMessage()
    element = CarousalElement(title="Morph.ai", sub_title="Experience the best",
                              image_url="https://res.cloudinary.com/crunchbase-production/image/upload/v1460728564/g0plluoyihiq8ap8pzp9.jpg",
                              click_url="http://www.morph.ai")
    element.add_button(button=URLButton(title="Signup", url="app.morph.ai", height="TALL"))
    carousal_message.add_carousal_element(
        element)

    element2 = CarousalElement(title="Payload button", sub_title="Showing how to create a card with payload button",
                               image_url="https://res.cloudinary.com/crunchbase-production/image/upload/v1460728564/g0plluoyihiq8ap8pzp9.jpg",
                               click_url="http://www.morph.ai")
    element2.add_button(button=PostbackButton(title="Postback button", payload="payload_to_be_sent"))
    carousal_message.add_carousal_element(element2)
    publish_action.add_message(carousal_message)
    return Response().add_action(publish_action).build()


def media(event, context):
    publish_action = Publish()
    media_message = MediaMessage(media_url="http://morph.ai/logo.jpeg", media_type="image")
    publish_action.add_message(media_message)
    return Response().add_action(publish_action).build()


print(read_and_set_attribute(None, {"userVariables": {"_PHONE_NUMBER": "9711xxx400"}}))
print(text_payload(None, None))
print(carousal(None, None))
print(media(None, None))
