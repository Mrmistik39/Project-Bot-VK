from VkApi.MessageNew import MessageNew
from Commands.CommandInterface import CommandInterface


class IpCommand(CommandInterface):

    def main(self, message: MessageNew):
        args = message.text.split(" ")
        if len(args) > 1:
            import requests
            ip = requests.get('http://ip-api.com/json/' + args[1]).json()
            if ip['status'] == 'fail':
                message.send_message('Не удалось получить информацию об IP')
            else:
                country = ip['country']
                country_code = ip['countryCode']
                region_name = ip['regionName']
                city = ip['city']
                zip = ip['zip']
                lat, lon = ip['lat'], ip['lon']
                timezone = ip['timezone']
                org = ip['org']
                query = ip['query']
                lines = [
                    f'Страна: {country}',
                    f'Код страны: {country_code}',
                    f'Регион: {region_name}',
                    f'Город: {city}',
                    f'zip: {zip}',
                    f'Координаты: lat {lat}, long {lon}',
                    f'Timezone: {timezone}',
                    f'Организация: {org}',
                    f'IP: {query}'
                ]
                message.send_message('\n'.join(lines), lat=lat, long=lon)
        else:
            message.send_message('Вы указали недостаточно аргументов')

    def get_names(self) -> list:
        return ['ip', 'айпи']

    def help(self) -> str:
        return 'Показывает данные об IP'
