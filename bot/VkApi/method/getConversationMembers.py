class getConversationMembers:

    peer_id = None

    def __init__(self, peer_id):
        self.peer_id = peer_id

    def send(self):
        users = []
        from Utils.Info import Info
        data = {
            'access_token': Info.TOKEN,
            'v': Info.VERSION,
            'peer_id': self.peer_id
        }
        import requests
        from VkApi.VkApi import VkApi
        import urllib.parse
        import json
        from VkApi.method.UserItem import UserItem
        response = requests.get(VkApi.HOST + 'messages.getConversationMembers?' + urllib.parse.urlencode(data)).text
        response = json.loads(response)
        items = response['items']
        for user in items:
            users.append(UserItem(user))
