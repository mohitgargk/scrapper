import time
import json
import pandas as pd
from scrap.Scrapper import Scrapper
from arbitrage.FutureSpot import FutureSpot
from option.LongStraddle import LongStraddle
from bs4 import BeautifulSoup
import calendar
import datetime
import requests

class NSEScrapper(Scrapper):

    def run(self):

        try:

            (baseData, optData ) = self.fetchOpt()
            futData = self.fetchFut()
            data = pd.DataFrame(columns=['ts', 'underlying', 'future', 'option'])
            data.loc[0] = [self.timestamp,  baseData,  futData,  optData]

            today = datetime.datetime.fromtimestamp(self.timestamp)
            exDayTS = self.getLastThurdayTS(today.month, today.year)

            # TODO Make arbitrage finders via base classes
            FS = FutureSpot(self.cfg['rbiRate'], self.name, self.timestamp, exDayTS, data, self.cfg['futArbThreshold'])
            trade = FS.getTrade()

            #if True:
               #print(trade)
               #self.postToWebapp('http://localhost:8080/arbitrage', trade)

            # TODO Find close spreads for long straddle
            LS = LongStraddle(self.name, data)
            tradeOp = LS.getTrade();

            print(tradeOp)
            self.postLSToWebapp('http://localhost:8081/ls', tradeOp)

            self.save(data)
        except Exception as ex:
            print ex
            pass

    def fetchFut(self):

        page = requests.get(self.urlFut)
        page.status_code
        page.content
        soup = BeautifulSoup(page.content, 'html.parser')
        dict = json.loads(soup.find(id="responseDiv").contents[0])['data'][0]
        #print(self.name)
        cols = dict.keys()
        vals = dict.values()

        df = pd.DataFrame( columns=cols)
        df.loc[0] = vals
        return df

    def fetchOpt(self):
        page = requests.get(self.urlOpt)
        page.status_code
        page.content
        soup = BeautifulSoup(page.content, 'html.parser')

        table_cls_1 = soup.find_all(id="octable")

        underlying = soup.find('b').contents[0].split(' ')[1]

        col_list = []

        # The code given below will pull the headers of the Option Chain table
        for mytable in table_cls_1:
            table_head = mytable.find('thead')

            try:
                rows = table_head.find_all('tr')
                for tr in rows:
                    cols = tr.find_all('th')
                    for th in cols:
                        er = th.text
                        ee = er.encode('utf8')
                        col_list.append(ee)

            except:
                print "no thead"

        col_list_fnl = [e for e in col_list if e not in ('CALLS', 'PUTS', 'Chart', '\xc2\xa0')]

        for i, s in enumerate(col_list_fnl):
            if i<10:
                col_list_fnl[i] = 'c_'+s
            if i>10 :
                col_list_fnl[i] = 'p_' + s

        table_cls_2 = soup.find(id="octable")
        req_row = table_cls_2.find_all('tr')

        new_table = pd.DataFrame(index=range(0, len(req_row) - 3), columns=col_list_fnl)

        row_marker = 0

        for row_number, tr_nos in enumerate(req_row):

            # This ensures that we use only the rows with values
            if row_number <= 1 or row_number == len(req_row) - 1:
                continue

            td_columns = tr_nos.find_all('td')

            # This removes the graphs columns
            select_cols = td_columns[1:22]
            cols_horizontal = range(0, len(select_cols))

            for nu, column in enumerate(select_cols):
                utf_string = column.get_text()
                utf_string = utf_string.strip('\n\r\t": ')
                tr = utf_string.encode('utf8')
                tr = tr.replace(',', '')
                new_table.ix[row_marker, [nu]] = tr

            row_marker += 1

        return (underlying, new_table)


    def postFSToWebapp(self, url, payloadDF):

        head = {'Content-type': 'application/json'}

        outDF = pd.DataFrame(columns = ['timestamp', 'trade'])
        outDF.loc[0] = [self.timestamp, payloadDF.to_json(orient='records')]
        payld = json.loads(outDF.to_json(orient='records'))[0]
        payld = json.dumps(payld, indent=4, sort_keys=True)
        ret = requests.post(url, data=payld)
        print(ret.status_code)
        return ret.status_code

    def postLSToWebapp(self, url, trade):

        print "POSTING: " + json.dumps(trade)
        head = {'Content-type': 'application/json'}

        ret = requests.post(url, data=json.dumps(trade), headers=head)
        print(ret.status_code)
        return ret.status_code

    def getLastThurdayTS(self, m, y):

        cc = calendar.Calendar(firstweekday=calendar.SUNDAY).monthdatescalendar(y, m)
        last = cc[len(cc) - 1][4]
        if last.month != m:
            last = last + datetime.timedelta(days=-7)
        return time.mktime(last.timetuple())
