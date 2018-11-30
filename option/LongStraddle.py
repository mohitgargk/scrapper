import datetime
import pandas as pd

class LongStraddle:

    def __init__(self, name, optionDF):

        self.name = name
        self.data = optionDF


    def getTrade(self):

        optionChain = self.data.loc[0]['option']
        u = float(self.data.loc[0]['underlying'].replace(',', ''))

        trade = {}
        trade["scrip"] = self.name
        trade["price"] = u
        trade["date"] = datetime.datetime.now().replace(microsecond=0).isoformat()

        trade["strike"] = 0
        trade["ce"] = 0
        trade["pe"] = 0
        trade["spread"] = 100

        spread_min = 100;

        for index, row in optionChain.iterrows():

            s  = float(row['Strike Price'].replace('-', ''))
            ce = float(row['c_LTP'].replace('-', '0'))
            pe = float(row['p_LTP'].replace('-', '0'))

            spread = 100 * (ce + pe) / u;

            if ce > 0.01 and pe > 0.01 :
                if spread_min > spread :

                    spread_min = spread
                    trade["strike"] = s
                    trade["ce"] = ce
                    trade["pe"] = pe
                    trade["spread"] = spread


        return trade