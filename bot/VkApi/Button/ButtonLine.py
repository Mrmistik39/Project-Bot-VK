from VkApi.Button import Button


class ButtonLine:

    json = []

    def __init__(self, *buttons):
        for i in buttons:
            self.json.append(i.get())

    def add(self, button: Button):
        self.json.append(button.get())

    def get(self):
        return self.json
