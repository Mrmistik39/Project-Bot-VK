import os


class Utils:
    FILE_APPEND = 'a+'

    @staticmethod
    def file_put_contents(file, content, mode='w+'):
        file = open(file, mode)
        file.write(content)
        file.close()

    @staticmethod
    def file_get_contents(file):
        file = open(file, 'r')
        content = file.read()
        file.close()
        return content

    @staticmethod
    def kill():
        os.kill(os.getpid(), 9)
