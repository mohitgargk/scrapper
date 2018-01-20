import json
import time
from scrap.Nifty50Scrapper import Nifty50Scrapper
from scrap.WorldIndicesScrapper import WorldIndicesScrapper

with open('./config.json') as json_data_file:
    cfg = json.load(json_data_file)
print(cfg)

frequency = cfg['frequency']
scrappers = list()

while True :

    ts = long(time.time())

    # Add nifty50
    nifty50config = cfg["nifty50"]
    niftyScrapper = Nifty50Scrapper(nifty50config, cfg["basePath"], ts )

    #Add world idxes
    worldIdxConfig = cfg['worldIndices']
    worldIdxScrapper = WorldIndicesScrapper(worldIdxConfig, cfg['basePath'], ts)

    scrappers.append(niftyScrapper)
    scrappers.append(worldIdxScrapper)

    for scrapper in scrappers:
        scrapper.start()

    for scrapper in scrappers:
        scrapper.join()

    print("Completed Scrapping at ts=" + str(ts))
    scrappers = list()

    time.sleep(frequency)


print("Exiting...")




