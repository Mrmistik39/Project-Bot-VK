class ButtonMessage:

    json = {}

    def __init__(self, *button):
        self.json = {
            'one_time': False,
            'inline': True,
            'buttons': []
        }
        for i in button:
            self.json['buttons'].append(i.get())

    def add(self, button_line):
        self.json['buttons'].append(button_line.get())
        return self

    def set_inline(self, bol):
        self.json['inline'] = bol
        return self

    def set_one_time(self, value):
        self.json['one_time'] = value
        return self

    def get(self):
        return self.json
