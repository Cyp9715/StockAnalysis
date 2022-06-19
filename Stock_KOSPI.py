from pykrx import stock
import StockName
import Date 
import Graph

class KOSPI:
    __graph = Graph.Graph

    def __init__(self):
        KOSPI.__graph = Graph.Graph()

    def search(self, title):
        stockPrice = stock.get_market_ohlcv_by_date(Date.GetDefaultDate(), Date.GetNowYMD(), StockName.KOSPI.NAME[title])
        fundermental = stock.get_market_fundamental(Date.GetDefaultDate(), Date.GetNowYMD(), StockName.KOSPI.NAME[title])
        KOSPI.__graph.Draw_separate(title, stockPrice['종가'], fundermental['PER'], fundermental['PBR'])
