from VkApi.MessageNew import MessageNew
from Commands.CommandInterface import CommandInterface
from VkApi.Button.ButtonLine import ButtonLine
from VkApi.Button.Button import Button
from VkApi.Button.ButtonMessage import ButtonMessage


class ChatCommand(CommandInterface):

    def on_click(self, message: MessageNew):
        message.send_message('Вы нажали на кнопку!')

    def __init__(self, command_manager):
        super().__init__(command_manager)
        command_manager.register_click_event('test.button', self)

    def main(self, message: MessageNew):
        pass

    def get_names(self) -> list:
        return ['chat']
