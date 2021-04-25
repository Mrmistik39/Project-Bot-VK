from VkApi.VkApi import VkApi
from Utils.Info import Info
import requests
from Commands.CommandManager import CommandManager
from VkApi.MessageNew import MessageNew
import json


class LongPoll:

    ts = {}
    CommandManager = None

    def command_manager(self):
        return self.CommandManager

    def __init__(self):
        super().__init__()
        self.CommandManager = CommandManager()
        self.CommandManager.init_command()
        self.get_session()

    def get_session(self):
        print('Получение сессии')
        session = VkApi.HOST + f'groups.getLongPollServer?group_id={Info.GROUP_ID}&v={Info.VERSION}&access_token={Info.TOKEN}'
        self.ts = json.loads(requests.get(session).text)

    def get_ts(self):
        key = self.ts['response']['key']
        server = self.ts['response']['server']
        ts = self.ts['response']['ts']
        response = json.loads(requests.get(f'{server}?act=a_check&key={key}&ts={ts}&wait=25').text)
        self.ts['response']['ts'] = response['ts']
        return response

    @property
    def update(self):
        # {$server}?act=a_check&key={$key}&ts={$ts}&wait=25
        try:
            return self.get_ts()
        except:
            self.get_session()
            return self.get_ts()

    def run(self):
        print('Запуск бота')
        while True:
            update = self.update['updates']
            for data in update:
                type = data['type']
                print('Пришло новое событие: ' + type)
                if type == 'message_new':
                    message = MessageNew(data)
                    self.CommandManager.push_click_button_event(message)
                    self.CommandManager.send_command(message)
                elif type == 'message_edit':
                    print('message_edit:' + data)
                else:
                    print('Неизвестное событие')


LongPoll().run()


