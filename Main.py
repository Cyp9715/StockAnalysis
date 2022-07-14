#%%
import Stock_KOSPI
import Graph

kospi = Stock_KOSPI.KOSPI()
graph = Graph.Graph()
kospi.search_multi(["케이티보통주", "삼성전자보통주"], graph.draw_separate)
#%%
