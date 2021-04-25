from VkApi.MessageNew import MessageNew
from Commands.CommandInterface import CommandInterface
from VkApi.Button.ButtonLine import ButtonLine
from VkApi.Button.Button import Button
from VkApi.Button.ButtonMessage import ButtonMessage


class TestCommand(CommandInterface):

    def on_click(self, message: MessageNew):
        message.send_message('Вы нажали на кнопку!')

    def __init__(self, command_manager):
        super().__init__(command_manager)
        command_manager.register_click_event('test.button', self)

    def main(self, message: MessageNew):
        button_message = ButtonMessage(
            ButtonLine(
                Button('test.button1').set_text('blue').set_color(Button.BLUE),
                Button('test.button2').set_text('green').set_color(Button.GREEN)
            )
        )
        from VkApi.method.getConversationMembers import getConversationMembers
        getConversationMembers(message.peer_id).send()
        message.send_message("Бот работает!", keyboard=button_message)

    def get_names(self) -> list:
        return ['test', 'тест']

    def help(self) -> str:
        return 'Тестовая команда'
