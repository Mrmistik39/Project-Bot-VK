from VkApi.MessageNew import MessageNew
from Commands.CommandInterface import CommandInterface


class MorCommand(CommandInterface):

    def main(self, message: MessageNew):
        args = message.text.split(' ')
        if len(args) > 1:
            import pymorphy2
            morph = pymorphy2.MorphAnalyzer()
            get = morph.parse(args[1])[0]
            list = ''
            if get.tag.POS in ['INFN', 'VERB']:
                for key, val in {
                    ('past', 'Прошедшее время:'): [
                        {'masc'}, {'femn'}, {'neut'}, {'plur'}
                    ],
                    ('pres', 'Настоящее время:'): [
                        {'1per', 'sing'},
                        {'1per', 'plur'},
                        {'2per', 'sing'},
                        {'2per', 'plur'},
                        {'3per', 'sing'},
                        {'3per', 'plur'}
                    ]
                }.items():
                    list += '\n' + str(key[1]) + '\n'
                    for cases in val:
                        cases.add(key[0])
                        if get.inflect(cases) is None:
                            message.send_message('Это не глагол')
                            return
                        w = get.inflect(cases).word
                        list += str(w) + '\n'
                message.send_message('Результат:\n' + list)
            else:
                message.send_message('Это не глагол')
        else:
            message.send_message('Вы не указали слово')

    def get_names(self) -> list:
        return ['склонение', 'morph', 'морф']

    def help(self) -> str:
        return 'Склоняет глаголы'
