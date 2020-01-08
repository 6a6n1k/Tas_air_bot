import requests
from bs4 import BeautifulSoup as bs
import telebot
import json
import datetime

bot = telebot.TeleBot('937403692:AAGeiMrpb5N-zgN1rLCUHlGLV93aR4kUyhA')

url=('https://www.flightradar24.com/')
headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36 '}
base_url = 'https://ru.flightaware.com/ajax/trackpoll.rvt?token=88dd7c1a0d41355dafa2ce4ff0e607704b11c422c13281779a15400a02823f7ccf96a80adf3baec3--76e86d4bff8ac1c5d7a0813749e14e00972848c7&locale=ru_RU&summary=0'



def fr_parse(base_url, headers,):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser').text
        data = json.loads(soup)
        flights = data.get('flights', '')
        i=0
        from1 = [0] * len(flights)
        to1 = [0] * len(flights)
        bort1 = [0]* len(flights)
        reis1 = [0]* len(flights)
        lg1 = [0]* len(flights)
        botsend = [0]* len(flights)

        for _, item,  in flights.items():
            #to
            destination = item.get('destination', '-')
            to2 = destination.get('friendlyName', '-')
            to1[i]=to2
            #from
            origin=item.get('origin','-')
            from2=origin.get('friendlyName', '-')
            from1[i]=from2
            #bort
            type=item.get('type','-')
            bort1[i]=type
            #reis
            ident=item.get('ident','-')
            reis1[i]=ident
            #landing
            landingtimes=item.get('landingTimes','-')
            lg3=landingtimes.get('estimated','-')
            lg2 = datetime.datetime.fromtimestamp(lg3)
            lg1[i]=str(lg2)

            i=i+1
    for j in range(len(botsend)):
        botsend[j]='*'+(str(j + 1)) + ')* ' + '[' + reis1[j] + ' на FR24]' + '('+url+reis1[j]+')' + '   ✈ ' + bort1[j] + '\n' + '*' +from1[j] + '➡' + to1[j] + '*' + '\n' + '🕙(Таш)' + lg1[j]
    str1 = '\n'.join(botsend)
    return (str1)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/tas":
        urlg = fr_parse(base_url, headers)
        bot.send_message(message.from_user.id, urlg,disable_web_page_preview = True, parse_mode='markdown' )
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши /tas")
    else:
        bot.send_message(message.from_user.id, "Что бы увидеть активные рейсы в/из Ташкента отправь /tas")

bot.polling(none_stop=True, interval=0)
