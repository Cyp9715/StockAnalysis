import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        plt.figure(figsize=(10,10), dpi=150)
        plt.subplots_adjust(top=1.1)
    # def correctGraph(stock, per, pbr):

    def draw_separate(self, title, stock, per, pbr):
        plt.subplot(311)
        plt.title(title)
        plt.plot(stock)

        plt.subplot(312)
        plt.title(title + " PER")
        plt.plot(per)

        plt.subplot(313)
        plt.title(title + " PBR")
        plt.plot(pbr)
    
    # def draw_combine(title, per, pbr):
        
        
        