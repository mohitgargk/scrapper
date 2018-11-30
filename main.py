import json
import time
from scrap.NSEScrapper import NSEScrapper
import calendar
import datetime
import requests

with open('./config.json') as json_data_file:
    cfg = json.load(json_data_file)
print(cfg)

# with open('./probability.json') as json_data_file:
#     days = daysLeft()
#     pcfg = json.load(json_data_file)
#     npcfg = [d for d in pcfg if d['day']==days]
#
#     head = {'Content-type': 'application/json'}
#     ret = requests.post("http://localhost:8081/lsconfig", data=json.dumps(json.dumps(npcfg)), headers=head)
#     print ret
#
# print(npcfg)

frequency = cfg['frequency']
activeDuringDay = cfg['activeDuringDay']
scrappers = list()

while True :

    hour = datetime.datetime.now().hour

    if (hour<9 and hour>16) and activeDuringDay==False :

        print("Skipping because market not open")
        time.sleep(60*60)

    else:
        ts = long(time.time())

        # Add NSE
        nseConfig = cfg["nse"]
        for nconf in nseConfig:
            nScrapper = NSEScrapper(cfg, nconf, cfg["basePath"], ts)
            scrappers.append(nScrapper)

        for scrapper in scrappers:
            scrapper.start()

        for scrapper in scrappers:
            scrapper.join()

        print("Completed Scrapping at ts=" + str(ts))
        scrappers = list()

        time.sleep(frequency)

print("Exiting...")




# def getLastThurdayPrivate(m, y):
#     cc = calendar.Calendar(firstweekday=calendar.SUNDAY).monthdatescalendar(y, m)
#     last = cc[len(cc) - 1][4]
#     if last.month != m:
#         last = last + datetime.timedelta(days=-7)
#     return last
#
# def getLastThurday(m, y):
#
#     last = getLastThurdayPrivate(m, y)
#
#     if last < datetime.datetime.now().date():
#         if m < 12:
#             last = getLastThurdayPrivate(m + 1, y)
#         else:
#             last = getLastThurdayPrivate(1, y + 1)
#
#     return last
#
# def daysLeft() :
#
#     upcomingExpiry = getLastThurday(datetime.datetime.now().date().month, datetime.datetime.now().date().year)
#     today = datetime.datetime.now().date()
#     left = (upcomingExpiry - today).days
#
#     left = left * 5 /7
#
#     if left == 0: left = left+1
#     if left >25 : left = 25
#
#     return left

