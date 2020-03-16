from mycroft import MycroftSkill, intent_file_handler


class Room(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('room.intent')
    def handle_room(self, message):
        roomname = message.data.get('roomname')
        if roomname != None:
            self.speak_dialog('room', data={
                'roomname': roomname
            })
            response = self.ask_yesno('Do_you_want_me_to_repeat')
            print(response)
            if response == 'yes':
                 self.speak_dialog('room', data={
                'roomname': roomname
            })
                self.speak_dialog('Have_a_nice_day')
        else:

            self.speak_dialog('test')

def create_skill():
    return Room()

