import requests
from bs4 import BeautifulSoup as bs
import re
import telebot;

bot = telebot.TeleBot('937403692:AAGeiMrpb5N-zgN1rLCUHlGLV93aR4kUyhA');

url=('https://www.flightradar24.com/')
headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36 '}
base_url = 'https://ru.flightaware.com/ajax/trackpoll.rvt?token=88dd7c1a0d41355dafa2ce4ff0e607704b11c422c13281779a15400a02823f7ccf96a80adf3baec3--76e86d4bff8ac1c5d7a0813749e14e00972848c7&locale=ru_RU&summary=0'



def fr_parse(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser').text
        #reis
        reis=re.findall(r'"displayIdent":"\w+',soup)
        reisstr1=','.join(reis)
        reis1=re.sub(r'"displayIdent":"',"",reisstr1)
        reis2=reis1.split(',')

        #bort
        bort=re.findall(r'"gate":null,"terminal":null,"delays":null},"type":"\w+',soup)
        bortstr1=','.join(bort)
        bort1=re.sub(r'"gate":null,"terminal":null,"delays":null},"type":"',"",bortstr1)
        bort2=bort1.split(',')

        #from-to
        ft=re.findall(r'"isValidAirportCode":true,"altIdent":"\w+',soup)
        ftstr1=','.join(ft)
        ft1=re.sub(r'"isValidAirportCode":true,"altIdent":"',"",ftstr1)
        ft2=ft1.split(',')
        ft3=(bort2)[0:len(bort2)]
        for i in range(int((len(ft2))/2)):
            a=i
            b=i+1
            ft3[i]=ft2[i+b]+' => '+ft2[i+a]

        urlg=reis2
        for i in range(len(reis2)):
            urlg[i]=(str(i+1))+') '+url+reis2[i]+'  '+bort2[i]+'  '+ft3[i]
        return(urlg)
#

    else:
        print('Error')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Tas":
        urlg = fr_parse(base_url, headers)
        str = '\n'.join(urlg)
        bot.send_message(message.from_user.id, str)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Tas")
    else:
        bot.send_message(message.from_user.id, "Что бы увидеть выполняемые рейсы в/из Ташкента отправь Tas")

bot.polling(none_stop=True, interval=0)
