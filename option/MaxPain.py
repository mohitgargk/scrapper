import datetime
import pandas as pd

class MaxPain:

    def __init__(self, name, optionDF):
        self.name = name
        self.data = optionDF

    def getTrade(self):

        optionChain = self.data.loc[0]['option']
        u = float(self.data.loc[0]['underlying'].replace(',', ''))

        trade = {}

        max_c_OI_Change = 0;
        max_p_OI_Change = 0;

        dataList = []

        for index, row in optionChain.iterrows():

            s  = float(row['Strike Price'])

            try :
                c_OI = float(row['c_OI'])
            except Exception as ex:
                c_OI = 0
                pass

            try:
                p_OI = float(row['p_OI'])
            except Exception as ex:
                p_OI = 0
                pass

            try :
                c_change_OI = float(row['c_Chng in OI'])
            except Exception as ex:
                c_change_OI = 0
                pass

            try :
                p_change_OI = float(row['p_Chng in OI'])
            except Exception as ex:
                p_change_OI = 0
                pass

            dataList.append((s, c_OI, p_OI))

            if c_change_OI > max_c_OI_Change:
                max_c_OI_Change = c_change_OI

            if p_change_OI > max_p_OI_Change:
                max_p_OI_Change = p_change_OI

        maxPain = self.getMaxPain(dataList)

        trade["max_c_OI_Change"] = max_c_OI_Change
        trade["max_p_OI_Change"] = max_p_OI_Change
        trade["maxpain_at"] = maxPain[0]
        trade["maxpain_total"] = maxPain[1]

        return trade

    def getPainAtStrike(self, stPrice, expPrice, c_oi, p_oi):

        pain = 0
        iv = 0
        if expPrice > stPrice :
            iv = expPrice - stPrice
            pain = iv * c_oi
        else :
            iv = -expPrice+stPrice
            pain = iv * p_oi

        return pain

    def getPainAtAllStrikes(self, price, data):
        pain = 0;
        for d in data :
            pain = pain + self.getPainAtStrike(price, d[0], d[1], d[2])
        return pain

    def getMaxPain(self, dataList) :
        result = map( lambda x : (x[0], self.getPainAtAllStrikes(x[0], dataList))  ,dataList)
        return min(result,key=lambda item:item[1])


# data = [(100, 1, 1), (110, 2, 2), (120, 3, 3), (130, 4, 4)]
# MP = MaxPain("", data) ;
# print MP.getMaxPain()