class SqlItem:

    value, type = None, None

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def __str__(self):
        return f"{self.value} {self.type}"
