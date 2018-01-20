import json
import time
from scrap.NSEScrapper import NSEScrapper
from scrap.WorldIndicesScrapper import WorldIndicesScrapper

with open('./config.json') as json_data_file:
    cfg = json.load(json_data_file)
print(cfg)

frequency = cfg['frequency']
scrappers = list()

while True :

    ts = long(time.time())


    #Add world idxes
    worldIdxConfig = cfg['worldIndices']
    worldIdxScrapper = WorldIndicesScrapper(worldIdxConfig, cfg['basePath'], ts)
    scrappers.append(worldIdxScrapper)

    # Add NSE
    nseConfig = cfg["nse"]
    for nconf in nseConfig:
        nScrapper = NSEScrapper(nconf, cfg["basePath"], ts)
        scrappers.append(nScrapper)

    for scrapper in scrappers:
        scrapper.start()

    for scrapper in scrappers:
        scrapper.join()

    print("Completed Scrapping at ts=" + str(ts))
    scrappers = list()

    time.sleep(frequency)


print("Exiting...")




