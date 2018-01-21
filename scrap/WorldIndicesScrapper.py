import time
import requests
import json
import pandas as pd
from scrap.Scrapper import Scrapper
from bs4 import BeautifulSoup


class WorldIndicesScrapper(Scrapper):

    def run(self):
        df = self.fetch()
        self.save(df)


    def fetch(self):

        page = requests.get(self.urlBase)
        page.status_code
        page.content
        soup = BeautifulSoup(page.content, 'html.parser')

        rows = soup.find("tbody", {"data-reactid": "45"}).find_all('tr')
        row_marker = 0

        cols = []
        vals = []

        for row_number, tr_nos in enumerate(rows):

            td = tr_nos.find_all('td')
            select_cols = td[0:3]
            cols_horizontal = range(0, len(select_cols))

            for nu, column in enumerate(select_cols):
                utf_string = column.get_text()
                utf_string = utf_string.strip('\n\r\t": ')
                tr = utf_string.encode('utf8')
                tr = tr.replace(',', '')

                if nu == 0:
                    cols.append(tr)
                if nu == 2:
                    vals.append(tr)

            row_marker += 1

        df = pd.DataFrame(columns=cols)
        df.loc[0] = vals

        return df



