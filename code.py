from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time
import telebot
import redis
#
#
#
def link():
        req = Request('https://techcrunch.com/', headers={'User-Agent': 'Mozilla/55.0'})
        time.sleep(1)
        page=urlopen(req).read()
        time.sleep(1)
        soup = BeautifulSoup(page,"html.parser")
        time.sleep(1)
        link = soup.find("a", {"class":"post-block__title__link"}).get("href")
        time.sleep(1)
        return link

def post():
        BOT_TOKEN ="700530653:AAHLS3cuFe1pOKuE4c2nLWiviE7KDvtJOE8"
        CHANNEL_NAME = "@techcrunch_news" 
        time.sleep(1)
        bot = telebot.TeleBot(BOT_TOKEN)
        time.sleep(1)
        bot.send_message(CHANNEL_NAME, link())
        time.sleep(180)

def getlastpost():
#        redis_host = "redis-server"
        redis_host = "tc-redis.q6xu0a.0001.usw2.cache.amazonaws.com"
        redis_port = 6379
        r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
        msg = r.get("msg:last")
        return msg
def setlastpost():
#        redis_host = "redis-server"
        redis_host = "tc-redis.q6xu0a.0001.usw2.cache.amazonaws.com"
        redis_port = 6379
        r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
        r.set("msg:last", link())
        
while True:
        time.sleep(1)
        if link() == getlastpost():
                print("The url is already posted")
                time.sleep(5)
                link()
                time.sleep(5)
                time.sleep(360)
        else:
                print("The strings are not the same")
                post()
                setlastpost()
                print (link())
