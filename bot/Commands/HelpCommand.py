from VkApi.MessageNew import MessageNew
from Commands.CommandInterface import CommandInterface


class HelpCommand(CommandInterface):

    command_manager = None

    def main(self, message: MessageNew):
        if self.command_manager is None:
            message.send_message('Ошибка инициализации CommandManager')
        else:
            commands = self.command_manager.commands
            list = []
            in_use = []
            for cmd in commands:
                if commands[cmd].get_names()[0] not in in_use:
                    list.append(', '.join(commands[cmd].get_names()) + '\n    * ' + commands[cmd].help() + ' (вызвано ' + str(commands[cmd].send) + ' раз)')
                    in_use.append(commands[cmd].get_names()[0])
            message.send_message('\n\n'.join(list))

    def get_names(self) -> list:
        return ['help', 'помощь']

    def help(self) -> str:
        return 'Помощь по командам'
