from types import MethodType
from pykrx import stock
import StockName
import Date 

class KOSPI:
    def search_single(self, title : str, drawFunc : MethodType):
        if isinstance(title, str) == False:
            raise Exception("The titles variable can only be in the Str Type.")

        stockPrice = stock.get_market_ohlcv_by_date(Date.GetDefaultDate(), Date.GetNowYMD(), StockName.KOSPI.NAME[title])
        fundermental = stock.get_market_fundamental(Date.GetDefaultDate(), Date.GetNowYMD(), StockName.KOSPI.NAME[title])

        drawFunc(title, stockPrice['종가'], fundermental['PER'], fundermental['PBR'])
    
    def search_multi(self, titles : list, drawFunc : MethodType):
        if isinstance(titles, list) == False:
            raise Exception("The titles variable can only be in the List Type.")

        for iter in titles:
            stockPrice = stock.get_market_ohlcv_by_date(Date.GetDefaultDate(), Date.GetNowYMD(), StockName.KOSPI.NAME[iter])
            fundermental = stock.get_market_fundamental(Date.GetDefaultDate(), Date.GetNowYMD(), StockName.KOSPI.NAME[iter])

            drawFunc(iter, stockPrice['종가'], fundermental['PER'], fundermental['PBR'])
