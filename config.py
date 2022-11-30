import requests
import telebot
from bs4 import BeautifulSoup as bts


url = 'https://www.anekdot.ru/random/anekdot/'
TOKEN = 'you token'

def parser(url):
    r = requests.get(url)
    soup = bts(r.text, 'html.parser')
    anecdot = soup.find_all('div', class_='text')
    return [c.text for c in anecdot]

final_anecdot = parser(url)
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'начать'])
def hello(message):
    bot.send_message(message.chat.id, 'Здравствуйте! что бы получить анектод введите любую цыфру')

@bot.message_handler(content_types=['text'])
def anecdot(message):
    if message.text.lower() in '0123456789':
        bot.send_message(message.chat.id, final_anecdot[0])
        del final_anecdot[0]
    else:
        bot.send_message(message.chat.id, 'Введите любую цыфру')


bot.polling()



