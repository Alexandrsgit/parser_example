from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import textwrap


load_dotenv()


def search(login):
    payload = {'q': login, 'where': 'ur'}
    response = requests.get(
        'SECRET_HTTP', params=payload
    )
    response = response.text
    soup = BeautifulSoup(response, 'lxml')
    try:
        answer = soup.find('td', class_='descr')
        print('-' * 120)
        print(textwrap.fill((answer.text.strip()), width=120))
        url1 = soup.find_all('a')
        print('-' * 120)
        print(url1[0].text.strip())
        print(url1[1].text.strip())
    except IndexError:
        print('Логин не найден')
    except AttributeError:
        print('Логин не найден')
    print('-' * 120)
    print('\n')


while True:
    login = input('login= ')
    search(login)
    again = input('Продолжить работу?(y/n)')
    if again != 'y':
        break
