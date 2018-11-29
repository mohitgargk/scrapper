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
        spread_min = 100;

        for index, row in optionChain.iterrows():

            s  = float(row['Strike Price'].replace('-', ''))
            ce = float(row['c_LTP'].replace('-', '0'))
            pe = float(row['p_LTP'].replace('-', '0'))
            if ce<0.01 or pe<0.01 :
                continue;

            spread = 100*(ce+pe)/u;

            if spread_min > spread :

                spread_min = spread
                trade["scrip"] = self.name
                trade["price"] = u
                trade["strike"] = s
                trade["ce"] = ce
                trade["pe"] = pe
                trade["spread"] = spread

        return trade