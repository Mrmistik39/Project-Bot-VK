from Commands.CommandInterface import CommandInterface
from Commands.TestCommand import TestCommand
from VkApi.MessageNew import MessageNew
from Commands.FilterCommand import FilterCommand
from Commands.IpCommand import IpCommand
from Commands.MorCommand import MorCommand
from Commands.HelpCommand import HelpCommand


class CommandManager:

    commands = {}
    register_button_click_event = {}
    instance = None

    TestCommand = None
    FilterCommand = None
    IpCommand = None
    MorCommand = None
    HelpCommand = None

    def init_command(self):
        self.TestCommand = TestCommand(self)
        self.FilterCommand = FilterCommand(self)
        self.IpCommand = IpCommand(self)
        self.MorCommand = MorCommand(self)

        self.register_command(self.MorCommand)
        self.register_command(self.IpCommand)
        self.register_command(self.FilterCommand)
        self.register_command(self.TestCommand)

        self.HelpCommand = HelpCommand(self)
        self.HelpCommand.command_manager = self
        self.register_command(self.HelpCommand)
        print(f'Загружено {len(self.commands)} команд')

    def register_click_event(self, name, cmd: CommandInterface):
        self.register_button_click_event[name] = cmd

    def push_click_button_event(self, message: MessageNew):
        if message.button is not None:
            for cmd in self.register_button_click_event:
                if message.button == cmd:
                    self.register_button_click_event[cmd].on_click(message)

    def register_command(self, cmd: CommandInterface):
        print("Загрузка: " + ", ".join(cmd.get_names()))
        for name in cmd.get_names():
            self.commands[name] = cmd

    def send_command(self, pk: MessageNew):
        try:
            text = pk.text.split(" ")[0].lower()
            self.commands[text].main(pk)
            self.commands[text].send += 1
        except KeyError:
            print('debug: Command not found')
            pass
