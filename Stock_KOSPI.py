from pykrx import stock
from pykrx import bond

df = stock.get_market_trading_volume_by_date("20210115", "20210122", "005930")
