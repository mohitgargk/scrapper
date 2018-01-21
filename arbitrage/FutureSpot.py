import datetime
import pandas as pd

class FutureSpot:

    def __init__(self, rate, name, timestamp, expiryTimestamp, futureDF, threshold):

        self.name = name
        self.rate = rate
        self.now = timestamp
        self.expiry = expiryTimestamp
        self.data = futureDF
        self.threshold = threshold


    def getTrade(self):

        today = datetime.datetime.fromtimestamp(int(self.now)).timetuple().tm_yday
        exDay = datetime.datetime.fromtimestamp(int(self.expiry)).timetuple().tm_yday


        futureDF = self.data.loc[0]['future']

        s = float(futureDF.loc[0]['underlyingValue'].replace(',', ''))
        f = float(futureDF.loc[0]['lastPrice'].replace(',', ''))
        r = float(self.rate)
        t = float(exDay - today)

        fv = self.getFairValue(s, r, t)

        fSell = float(futureDF.loc[0]['sellPrice1'].replace(',', ''))
        sBuy = s
        fPs = (f - s) * 100 / s
        fPfv = (fv - f) * 100 / f

        goNoGp = False
        if fPs>self.threshold :
            goNoGp = True

        cols = ['name', 'S', 'F', 'FV', 'Fsell', 'Sbuy', 'F%S', 'F%FV', 'GoNoGo']
        vals = [self.name, s, f, fv, fSell, sBuy, fPs, fPfv, goNoGp ]

        df = pd.DataFrame(columns=cols)
        df.loc[0] = vals
        return df

    def getFairValue(self, s, r, t, d=0):

        effRate = r*t/365
        fairValue = s * (1 + effRate/100 - d)
        return  fairValue


