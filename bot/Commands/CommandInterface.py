from VkApi.MessageNew import MessageNew


class CommandInterface:

    send = 0

    def __init__(self, command_manager):
        pass

    def on_click(self, message: MessageNew):
        pass

    def help(self) -> str:
        pass

    def main(self, message: MessageNew):
        pass

    def get_names(self) -> list:
        pass
