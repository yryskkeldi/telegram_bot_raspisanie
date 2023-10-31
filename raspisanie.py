import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('5673605579:AAH-kGT5pqqpNmH3PDpt19YZJMCo5wuSLZk')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот")

@bot.message_handler(commands=['schedule'])
def send_schedule(message):

    bot.reply_to(message, "Введите дату в формате ГГГГ-ММ-ДД")

@bot.message_handler(regexp='\\d{4}-\\d{2}-\\d{2}')
def handle_date(message):
    date = message.text
    response = requests.get(f'<https://schedule.mi.university/ruz/main/{date}>')
    soup = BeautifulSoup(response.content, 'html.parser')
    schedule2 = soup
    schedule = soup.find('div', {'class': 'schedule__table'}).text
    bot.reply_to(message, schedule)

bot.polling()

