from pykrx import stock
import StockName
import Date 
import Graph
import CheckType

class KOSPI:
    __graph = Graph.Graph

    def __init__(self):
        KOSPI.__graph = Graph.Graph()

    # v
    def __correctStock(standard, value):
        coefficient = standard / value
        value *= coefficient # value 값에 적용안되는 문제있음.
        print(value)

    def search(self, titles) -> bool:
        for iter in titles:
            stockPrice = stock.get_market_ohlcv_by_date(Date.GetDefaultDate(), Date.GetNowYMD(), StockName.KOSPI.NAME[iter])
            fundermental = stock.get_market_fundamental(Date.GetDefaultDate(), Date.GetNowYMD(), StockName.KOSPI.NAME[iter])
            KOSPI.__graph.draw_separate(iter, stockPrice['종가'], fundermental['PER'], fundermental['PBR'])
        
    def search2(self, titles) -> bool:
        if CheckType.isList(titles) == False:
            raise Exception("Only the type of titles is allowed.")

        for iter in titles:
            stockPrice = stock.get_market_ohlcv_by_date(Date.GetDefaultDate(), Date.GetNowYMD(), StockName.KOSPI.NAME[iter])
            fundermental = stock.get_market_fundamental(Date.GetDefaultDate(), Date.GetNowYMD(), StockName.KOSPI.NAME[iter])
            avg_stockPrice = stockPrice['종가'].mean();
            avg_fundermantal_PER = fundermental['PER'].mean();
            avg_fundermantal_PBR = fundermental['PBR'].mean();

            KOSPI.__correctStock(avg_stockPrice, avg_fundermantal_PBR)
            KOSPI.__correctStock(avg_stockPrice, avg_fundermantal_PBR)

            KOSPI.__graph.draw_combine(iter, stockPrice['종가'], fundermental['PER'], fundermental['PBR'])
