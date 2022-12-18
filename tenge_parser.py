import requests
import re
from bs4 import BeautifulSoup as bs


url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)

soup = bs(response.text, 'html.parser')
date = re.findall(r"\"Date\":\D+(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})",
                  f'{response.text}')
str_date = ''.join(map(str, date))[2:18].replace("', '", '.')   # готовый вывод даты dd.mm.YYYY

tenge = re.findall(r"(?P<tenge>\"KZT\")"
                   r"(?P<perenos>,\n\W+)"
                   r"(?P<nominal>\"Nominal\": [0-9]{3})"
                   r"(?P=perenos)"
                   r"(?P<name>\"Name\": \"[А-Яа-я]{13} [а-я]{5}\")"
                   r"(?P=perenos)"
                   r"(?P<value>\"Value\": \w+.\w+)",
                   f'{response.text}')

code = ''.join(map(str, tenge))[3:6]
nominal = ''.join(map(str, tenge))[30:44].replace('"', '').replace('Nominal: ', '')
name = ''.join(map(str, tenge))[48:76].replace('"', '').replace('Name: ', '')
value = ''.join(map(str, tenge))[82:97].replace('"', '').replace('Value:', "стоят")


done_tenge = f'{nominal}{code} на {str_date} {value}₽'

print(done_tenge)