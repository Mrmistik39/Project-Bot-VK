from VkApi.VkApi import VkApi
from VkApi.Attachments.Photo import Photo


class MessageNew:

    message, text, peer_id, user_id, id = None, None, None, None, None
    conversation_message_id = None
    attachments = []
    button = None

    def __init__(self, data):
        self.message = data['object']['message']
        self.text = self.message['text']
        self.peer_id = self.message['peer_id']
        self.user_id = self.message['from_id']
        try:
            import json
            self.button = json.loads(self.message['payload'])['button']
        except KeyError:
            pass
        except IndexError:
            pass
        if len(self.message['attachments']) > 0:
            for attachment in self.message['attachments']:
                if attachment['type'] == 'photo':
                    self.attachments.append(Photo(attachment))

    def is_group(self) -> bool:
        return self.peer_id >= 2000000000

    def send_message(self, text, keyboard=None, lat='', long=''):
        VkApi.send_message(self.peer_id, text, button=keyboard, lat=lat, long=long)
