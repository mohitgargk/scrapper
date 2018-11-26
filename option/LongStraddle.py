import datetime
import pandas as pd

class LongStraddle:

    def __init__(self, name, optionDF, threshold=1.5):

        self.name = name
        self.data = optionDF
        self.threshold = threshold


    def getTrade(self):

        counter = 0
        cols = ['name', 'U', 'S', 'CE', 'PE', 'Spread', 'GoNoGo']
        df = pd.DataFrame(columns=cols)

        optionChain = self.data.loc[0]['option']

        u = float(self.data.loc[0]['underlying'].replace(',', ''))

        for index, row in optionChain.iterrows():
            s  = float(row['Strike Price'].replace('-', ''))
            ce = float(row['c_LTP'].replace('-', '0'))
            pe = float(row['p_LTP'].replace('-', '0'))

            if ce<0.01 or pe<0.01 :
                continue;

            spread = 100*(ce+pe)/u;

            goNoGo = False
            if spread < self.threshold:
                goNoGo = True

            if goNoGo == True:
                vals = [self.name, u, s, ce, pe, spread, goNoGo]
                df.loc[counter] = vals
                counter = counter +1

        return df