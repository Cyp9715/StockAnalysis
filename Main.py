#%%
import pykrx.stock as stock
import Date 
import StockName
from Graph import Graph


stockPrice = stock.get_market_ohlcv_by_date(Date.GetDefaultDate(), Date.GetNowYMD(), StockName.KOSPI['삼성전자보통주'])
fundermental = stock.get_market_fundamental(Date.GetDefaultDate(), Date.GetNowYMD(), StockName.KOSPI['삼성전자보통주'])

graph = Graph()
graph.draw_separate("SUMSANG", stockPrice['종가'], fundermental['PER'], fundermental['PBR'])

#%%