class Photo:

    date, id, owner_id, url = None, None, None, None
    name = 'photo'

    def __init__(self, data):
        print(data)
        self.date = data['photo']['date']
        self.id = data['photo']['id']
        self.owner_id = data['photo']['owner_id']
        self.url = data['photo']['sizes'][len(data['photo']['sizes']) - 1]['url']
