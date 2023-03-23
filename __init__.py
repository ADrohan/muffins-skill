from mycroft import MycroftSkill, intent_file_handler


class Muffins(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('muffins.intent')
    def handle_muffins(self, message):
        flavour = ''

        self.speak_dialog('muffins', data={
            'flavour': flavour
        })


def create_skill():
    return Muffins()

