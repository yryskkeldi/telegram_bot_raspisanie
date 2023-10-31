import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('5673605579:AAH-kGT5pqqpNmH3PDpt19YZJMCo5wuSLZk')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот")

@bot.message_handler(commands=['news'])
def send_news(message):
    response = requests.get('<https://www.example.com/news>')
    soup = BeautifulSoup(response.content, 'html.parser')
    news = soup.find('ul', {'class': 'news-list'}).text
    bot.reply_to(message, news)

@bot.message_handler(commands=['blog'])
def send_blog(message):
    response = requests.get('<https://www.example.com/blog>')
    soup = BeautifulSoup(response.content, 'html.parser')
    posts = soup.find('ul', {'class': 'blog-list'}).text
    bot.reply_to(message, posts)

bot.polling()
