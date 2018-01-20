import pandas as pd
import requests
import pandas as pd
from scrap.Scrapper import Scrapper
from bs4 import BeautifulSoup
import numpy as np

import json

json = "\"{name}\"  : {    \"urlBase\" : \"\", \"urlFut\"  : \"https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuoteFO.jsp?underlying={name}&instrument=FUTSTK\", \"urlOpt\"  : \"https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbol={name}\", \"name\"    : \"{name}\" }";
stocks = "ADANIPORTS,AMBUJACEM,ASIANPAINT,AUROPHARMA,AXISBANK,BAJAJ-AUTO,BAJFINANCE,BPCL,BHARTIARTL,INFRATEL,BOSCHLTD,CIPLA,COALINDIA,DRREDDY,EICHERMOT,GAIL,HCLTECH,HDFCBANK,HEROMOTOCO,HINDALCO,HINDPETRO,HINDUNILVR,HDFC,ITC,ICICIBANK,IBULHSGFIN,IOC,INDUSINDBK,INFY,KOTAKBANK,LT,LUPIN,M&M,MARUTI,NTPC,ONGC,POWERGRID,RELIANCE,SBIN,SUNPHARMA,TCS,TATAMOTORS,TATASTEEL,TECHM,UPL,ULTRACEMCO,VEDL,WIPRO,YESBANK,ZEEL"
stocks = stocks.split(",")

jsonList = []

for s in stocks :
    jsonList.append(json.replace("{name}", s))



for j in jsonList:
    print(j)


    pass



