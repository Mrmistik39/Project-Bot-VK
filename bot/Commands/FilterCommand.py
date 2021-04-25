from VkApi.MessageNew import MessageNew
from Commands.CommandInterface import CommandInterface
import threading


class FilterCommand(CommandInterface):

    times = []

    def main(self, message: MessageNew):
        threading.Thread(target=self.async_run, args=(message,)).start()

    def async_run(self, message: MessageNew):
        if len(self.times) < 2:
            times = 'Это может занять пару секунд'
        else:
            secs = 0
            for i in self.times:
                secs += i
            times = 'Это может занять ~ ' + str(round(secs / (len(self.times)), 1)) + ' секунд'
        message.send_message('Обработка изображения... ' + times)
        for attachment in message.attachments:
            if attachment.name == 'photo':
                import time
                time_start = time.time()
                import requests
                from PIL import Image
                from VkApi.VkApi import VkApi
                import os
                from random import randint
                file_name = f'{message.user_id}-{randint(0, 100)}.png'
                print(attachment.url)
                image = Image.open(requests.get(attachment.url, stream=True).raw)
                rand = randint(0, 2)
                if rand == 0:
                    pixels = image.load()
                    x, y = image.size
                    im = Image.new('RGB', (x, y), (255, 255, 255))
                    pix = im.load()
                    delta = randint(2, 13)
                    for i in range(x):
                        for o in range(y):
                            r, g, b = pixels[i, o]
                            if i - delta >= 0:
                                r1, g1, b1 = pixels[i - delta, o]
                                pix[i, o] = r1, g, b
                            else:
                                g, b = pixels[i, o][1:]
                                pix[i, o] = 0, g, b
                    im.save(file_name, 'PNG')
                elif rand == 1:
                    result = Image.new('RGB', image.size)
                    separator = 255 / 0.8 / 2 * 3
                    for x in range(image.size[0]):
                        for y in range(image.size[1]):
                            r, g, b = image.getpixel((x, y))
                            total = r + g + b
                            if total > separator:
                                result.putpixel((x, y), (255, 255, 255))
                            else:
                                result.putpixel((x, y), (0, 0, 0))
                    result.save(file_name, 'PNG')
                elif rand == 2:
                    result = Image.new('RGB', image.size)
                    avg = 0
                    for x in range(image.size[0]):
                        for y in range(image.size[1]):
                            r, g, b = image.getpixel((x, y))
                            avg += r * 0.299 + g * 0.587 + b * 0.114
                    avg /= image.size[0] * image.size[1]
                    palette = []
                    for i in range(256):
                        temp = int(avg + 2 * (i - avg))
                        if temp < 0:
                            temp = 0
                        elif temp > 255:
                            temp = 255
                        palette.append(temp)
                    for x in range(image.size[0]):
                        for y in range(image.size[1]):
                            r, g, b = image.getpixel((x, y))
                            result.putpixel((x, y), (palette[r], palette[g], palette[b]))
                    result.save(file_name, "PNG")
                VkApi.send_photo(message.peer_id, [file_name], 'Готово!')
                self.times.append(time.time() - time_start)
                # os.remove(file_name)
            return
        message.send_message('Изображение не найдено')

    def get_names(self) -> list:
        return ['filter', 'фильтр']

    def help(self) -> str:
        return 'Накладывает на изображение случайный фильтр'
