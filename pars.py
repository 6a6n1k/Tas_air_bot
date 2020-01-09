import requests
from bs4 import BeautifulSoup as bs
import telebot
import json
import datetime
import pytz

bot = telebot.TeleBot('1068881424:AAFB_Dr7HeTokvy8rNeNW4MbmAOsuA7KMWU')

url=('https://www.flightradar24.com/')
headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36 '}




def fr_parse(base_url, headers, name):
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
        toair = [0]* len(flights)
        fromair = [0]* len(flights)
        flt=[0]* len(flights)
        flf=[0]* len(flights)


        for _, item,  in flights.items():
            #to
            destination = item.get('destination', '-')
            flt1=destination.get('friendlyLocation','').split(', ')[0]
            to2 = destination.get('friendlyName', '-')
            to1[i]=to2
            flt[i]=flt1
            #from
            origin=item.get('origin','-')
            flf1=origin.get('friendlyLocation','').split(', ')[0]
            from2=origin.get('friendlyName', '-')
            from1[i]=from2
            flf[i]=flf1
            #bort
            type=item.get('type','-')
            bort1[i]=type
            #reis
            ident=item.get('ident','-')
            reis1[i]=ident
            #landing
            landingtimes=item.get('landingTimes','-')
            lg3=landingtimes.get('estimated','-')
            tz3=item.get('destination','')
            tz2=tz3.get('TZ','')
            tz = pytz.timezone(tz2[1:])
            lg2 = datetime.datetime.fromtimestamp(lg3,tz).strftime("%Y/%m/%d %H:%M")
            lg1[i]=str(lg2)

            i=i+1

    a=0
    b=0
    for j in range(len(botsend)):
        if (to1[j]==name):
            toair[a]='*'+(str(a + 1)) + ')* ' + '[' + reis1[j] + ' LIVE ]' + '('+url+reis1[j]+')' + '   ✈ ' + bort1[j] + '\n' + '*' +from1[j]+' ('+flf[j]+')' + '➡' + to1[j]+' ('+flt[j]+')' + '*' + '\n' + '🕙' + lg1[j]+'\n'
            a=a+1
    for j in range(len(botsend)):
        if (to1[j] != name):
            fromair[b] = '*' + (str(b + 1)) + ')* ' + '[' + reis1[j] + ' LIVE ]' + '(' + url + reis1[j] + ')' + '   ✈ ' +  bort1[j] + '\n' + '*' +from1[j]+' ('+flf[j]+')' + '➡' + to1[j]+' ('+flt[j]+')' + '*'  + '\n' + '🕙' + lg1[j]+'\n'
            b=b+1
    toair1=toair[:a]
    strtoair1='\n'.join(toair1)
    fromair1=fromair[:b]
    strfromair1='\n'.join(fromair1)
    botsend = '*Время прибытия по аэропорту назначения!*'+'\n\n'+'*Летят в ' + name +'*' + '\n\n' + str(strtoair1) + '\n' + '*Улетают из ' + name + '*'+'\n\n' + str(strfromair1)+'\n'+'*Время прибытия по аэропорту назначения!*'

    str1 = ''.join(botsend)

    return (str1)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/Tashkent" or message.text == "/tashkent" : #1
        name = "Ташкент-Южный"
        base_url = 'https://ru.flightaware.com/ajax/trackpoll.rvt?token=88dd7c1a0d41355dafa2ce4ff0e607704b11c422c13281779a15400a02823f7ccf96a80adf3baec3--76e86d4bff8ac1c5d7a0813749e14e00972848c7&locale=ru_RU&summary=0'
        urlg = fr_parse(base_url, headers, name)
        bot.send_message(message.from_user.id, urlg,disable_web_page_preview = True, parse_mode='markdown' )
    elif message.text == "/Samarkand" or message.text == "/samsrkand":  #2
        name = 'Samarkand'
        base_url = 'https://ru.flightaware.com/ajax/trackpoll.rvt?token=88dd7c1a0d41355dafa2ce4ff0e607704b11c422c1328177ee3a6b2bb5b861bc97ef0d44cce137d0--cde90a37b96c9c3026a7fc2ccffc41868fbdcc24&locale=ru_RU&summary=0'
        urlg = fr_parse(base_url, headers, name)
        bot.send_message(message.from_user.id, urlg,disable_web_page_preview = True, parse_mode='markdown' )
    elif message.text == "/Termez" or message.text == "/termez": #3
        name = 'Termez'
        base_url = 'https://ru.flightaware.com/ajax/trackpoll.rvt?token=88dd7c1a0d41355dafa2ce4ff0e607704b11c422c1328177ee3a6b2bb5b861bccf96a80adf3baec3--baff8e88c8b1f38fffa0b02f85e279c394ffe39b&locale=ru_RU&summary=0'
        urlg = fr_parse(base_url, headers, name)
        bot.send_message(message.from_user.id, urlg, disable_web_page_preview=True, parse_mode='markdown')
    elif message.text == "/Karshi" or message.text == "/karshi":   #4
        name = 'Karshi'
        base_url = 'https://ru.flightaware.com/ajax/trackpoll.rvt?token=88dd7c1a0d41355dafa2ce4ff0e607704b11c422c1328177ee3a6b2bb5b861bca6157c45c30d3788--25dc51283529b530453acc0d4f58143e25094584&locale=ru_RU&summary=0'
        urlg = fr_parse(base_url, headers, name)
        bot.send_message(message.from_user.id, urlg, disable_web_page_preview=True, parse_mode='markdown')
    elif message.text == "/Navoi" or message.text == "/navoi":   #5
        name = "Navoi Int'l"
        base_url = 'https://ru.flightaware.com/ajax/trackpoll.rvt?token=88dd7c1a0d41355dafa2ce4ff0e607704b11c422c1328177ee3a6b2bb5b861bc50ac60b9e5e59625--c93fddf78a5a50b226ee9fb3d0e194ac7d1417c8&locale=ru_RU&summary=0'
        urlg = fr_parse(base_url, headers, name)
        bot.send_message(message.from_user.id, urlg, disable_web_page_preview=True, parse_mode='markdown')
    elif message.text == "/Bukhara" or message.text == "/bukhara":   #6
        name = 'Bukhara'
        base_url = 'https://ru.flightaware.com/ajax/trackpoll.rvt?token=88dd7c1a0d41355dafa2ce4ff0e607704b11c422c1328177ee3a6b2bb5b861bc83fd403f2e47bbfa--af2d70eca1450afa66515c694be9709ed22c868c&locale=ru_RU&summary=0'
        urlg = fr_parse(base_url, headers, name)
        bot.send_message(message.from_user.id, urlg, disable_web_page_preview=True, parse_mode='markdown')
    elif message.text == "/Urgench" or message.text == "/urgench":    #7
        name = 'Urgench'
        base_url = 'https://ru.flightaware.com/ajax/trackpoll.rvt?token=88dd7c1a0d41355dafa2ce4ff0e607704b11c422c1328177140bab01cfa017ba77dcb401fae35b1b--5dafd36f04b543bf248d07b03f303052a090e45b&locale=ru_RU&summary=0'
        urlg = fr_parse(base_url, headers, name)
        bot.send_message(message.from_user.id, urlg, disable_web_page_preview=True, parse_mode='markdown')
    elif message.text == "/Nukus" or message.text == "/nukus":    #8
        name = 'Nukus'
        base_url = 'https://ru.flightaware.com/ajax/trackpoll.rvt?token=88dd7c1a0d41355dafa2ce4ff0e607704b11c422c1328177140bab01cfa017bad0b69931a0f4ad61--cff055a07cefd1bc32a5f38b3e41e8dbac3adf14&locale=ru_RU&summary=0'
        urlg = fr_parse(base_url, headers, name)
        bot.send_message(message.from_user.id, urlg, disable_web_page_preview=True, parse_mode='markdown')
    elif message.text == "/Namangan" or message.text == "/namangan":    #9
        name = 'Namangan'
        base_url = 'https://ru.flightaware.com/ajax/trackpoll.rvt?token=88dd7c1a0d41355dafa2ce4ff0e607704b11c422c1328177b765184eca690891d0b69931a0f4ad61--07d1c20b08f5b0e6cfcdf847bea8fa62143a3641&locale=ru_RU&summary=0'
        urlg = fr_parse(base_url, headers, name)
        bot.send_message(message.from_user.id, urlg, disable_web_page_preview=True, parse_mode='markdown')
    elif message.text == "/Andizhan" or message.text == "/andizhan" or message.text == "/Andijan" or message.text == "/andijan" :    #10
        name = 'Andizhan (Andijan)'
        base_url = 'https://ru.flightaware.com/ajax/trackpoll.rvt?token=88dd7c1a0d41355dafa2ce4ff0e607704b11c422c1328177b765184eca69089150ac60b9e5e59625--12ab2ee968ea205caa136148740c04186c0e4ae9&locale=ru_RU&summary=1'
        urlg = fr_parse(base_url, headers, name)
        bot.send_message(message.from_user.id, urlg, disable_web_page_preview=True, parse_mode='markdown')
    elif message.text == "/Fergana" or message.text == "/fergana":    #11
        name = 'Fergana'
        base_url = 'https://ru.flightaware.com/ajax/trackpoll.rvt?token=88dd7c1a0d41355dafa2ce4ff0e607704b11c422c1328177b765184eca690891c7bac9c3e7d3966a--96db7d7ddb5500542ccf3123482d69cc2976aa40&locale=ru_RU&summary=0'
        urlg = fr_parse(base_url, headers, name)
        bot.send_message(message.from_user.id, urlg, disable_web_page_preview=True, parse_mode='markdown')
    elif message.text == "/help":
        bot.send_message(message.from_user.id,"Бот предоставляет информацию о выполняющихся рейсах всех аэропортов Узбекистана 🇺🇿  \nБот создан каналом [@AKU_rus](AKU_rus)  \n*Время прибытия по аэропорту назначения!* \nДоступные аэропорты Узбекистана: \n /Tashkent \n /Samarkand \n /Bukhara \n /Navoi \n /Andizhan \n /Fergana \n /Nukus \n /Karshi \n /Termez \n /Urgench \n /Namangan",disable_web_page_preview=True,parse_mode='markdown')

    elif message.text == "/start":
        bot.send_message(message.from_user.id,"Выбери аэропорт города из списка: \n /Tashkent \n /Samarkand \n /Bukhara \n /Navoi \n /Andizhan \n /Fergana \n /Nukus \n /Karshi \n /Termez \n /Urgench \n /Namangan", parse_mode='markdown')
    else:
        bot.send_message(message.from_user.id, "Попробуй снова или выбери из списка: \n /Tashkent \n /Samarkand \n /Bukhara \n /Navoi \n /Andizhan \n /Fergana \n /Nukus \n /Karshi \n /Termez \n /Urgench \n /Namangan"  , parse_mode='markdown')

bot.polling(none_stop=True, interval=0)
