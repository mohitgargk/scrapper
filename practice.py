import pandas as pd
import requests
import pandas as pd
from scrap.Scrapper import Scrapper
from bs4 import BeautifulSoup
import numpy as np

import json

data = pd.DataFrame(columns=['a', 'b'])
data.loc[0] = [1,2]
data.loc[1] = [3,2]


json_str = data.to_json(orient='records')

data2 = json.loads(json_str)

with open('data.json', 'w') as f:
    json.dump(data2, f)

pass



