#%%
import Stock_KOSPI
import Graph

kospi = Stock_KOSPI.KOSPI()
graph = Graph.Graph()
kospi.search_single("케이티보통주", graph.draw_combine)
#%%
