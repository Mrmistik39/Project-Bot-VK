import requests
from Utils.Info import Info
import json
import urllib.parse
from VkApi.Button.ButtonMessage import ButtonMessage


class VkApi:
    HOST = 'https://api.vk.com/method/'

    @staticmethod
    def get_user(user_id):
        data = {
            'user_ids': user_id,
            'access_token': Info.TOKEN,
            'v': Info.VERSION
        }
        return json.loads(requests.get('https://api.vk.com/method/users.get?' + urllib.parse.urlencode(data)).text)

    @staticmethod
    def send_message(peer_id, message, attachment='', button: ButtonMessage = None, lat='', long=''):
        data = {
            'peer_id': peer_id,
            'random_id': 0,
            'access_token': Info.TOKEN,
            'v': Info.VERSION,
            'message': message,
            'attachment': attachment,
            'lat': lat,
            'long': long
        }
        if button is not None:
            import json
            # print(button.get())
            data['keyboard'] = json.dumps(button.get())
        return requests.get(VkApi.HOST + f'messages.send?' + urllib.parse.urlencode(data)).text

    @staticmethod
    def sends_message(peer_ids, message, attachment='', lat='', long=''):
        data = {
            'peer_ids': peer_ids,
            'random_id': 0,
            'access_token': Info.TOKEN,
            'v': Info.VERSION,
            'message': message,
            'attachment': attachment,
            'lat': lat,
            'long': long
        }
        return requests.get(VkApi.HOST + f'messages.send?' + urllib.parse.urlencode(data)).text

    @staticmethod
    def get_photo_upload_url():
        data = {
            'v': Info.VERSION,
            'access_token': Info.TOKEN
        }
        url = 'https://api.vk.com/method/photos.getMessagesUploadServer?'
        return json.loads(requests.get(url + urllib.parse.urlencode(data)).text)

    @staticmethod
    def photo_upload_server(peer_id, file):
        server = VkApi.get_photo_upload_url()
        file = {
            'file1': open(file, 'rb')
        }
        return json.loads(requests.post(server['response']['upload_url'], files=file).text)

    @staticmethod
    def save_photo(peer_id, file):
        save = VkApi.photo_upload_server(peer_id, file)
        data = {
            'v': Info.VERSION,
            'access_token': Info.TOKEN,
            'photo': save['photo'],
            'server': save['server'],
            'hash': save['hash']
        }
        return json.loads(
            requests.get('https://api.vk.com/method/photos.saveMessagesPhoto?' + urllib.parse.urlencode(data)).text)

    @staticmethod
    def send_photo(peer_id, file, message=''):
        try:
            files = []
            for _file in file:
                photo = VkApi.save_photo(peer_id, _file)['response'][0]
                owner_id = photo['owner_id']
                media_id = photo['id']
                files.append(f'photo{owner_id}_{media_id}')
            return VkApi.send_message(peer_id, message, ','.join(files))
        except Exception:
            print('Ошибка загрузки изображения, повтор...')
            VkApi.send_photo(peer_id, file, message)
