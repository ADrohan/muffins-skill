from mycroft import MycroftSkill, intent_file_handler
from random import randint

class Muffins(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

# To do
#    def initialize(self):
#       self.register_entity_file('flavour.entity')

    @intent_file_handler('muffins.intent')
    def handle_muffins(self, message):
        self.speak_dialog('welcome')
        flavour = message.data.get('flavour')
        if flavour is None:
            self.speak_dialog('plain.recipe')
        elif flavour.casefold() == "plain":
            self.speak_dialog('plain.recipe')
        else: self.speak_dialog('flavour.recipe', data={'flavour' : flavour})

    def quantity_check (self):
        quantity = randint(1,9)
        return quantity

    @intent_file_handler('check.ingredients.intent')
    def handle_check_ingredients(self, message):
        stock = self.quantity_check()
#        self.log.info(stock)

        if stock <= 5:
            self.speak_dialog('unstocked', wait=True)
            self.place_order()
        else:
            self.speak_dialog('stocked', wait=True)
            self.anything_else()

    def place_order(self):
        order_response = self.ask_yesno('help.request')
        if order_response ==  "yes":
            self.speak_dialog('do.it')
        elif order_response == "no":
            self.speak_dialog('dont.do.it')
        else:
            self.log.info('user replied with (utterance)')
        self.anything_else()

    def anything_else(self):
        anything_else_response = self.ask_yesno('anything.request')

        if anything_else_response == "yes":
            self.speak_dialog('anything.response')
        elif anything_else_response  == "no":
            self.speak_dialog('goodbye')
        else: self.log.info('user replied with (utterance)')

    @intent_file_handler('method.intent')
    def handle_method(self, message):
        flavour = message.data.get('flavour')
        if flavour is None:
            self.speak_dialog('method', wait=True)
        elif flavour.casefold() == "plain":
            self.speak_dialog('method', wait=True)
        else:
            self.speak_dialog('flavour.method', data={'flavour' : flavour}, wait=True)
        self.anything_else()

def create_skill():
    return Muffins()

