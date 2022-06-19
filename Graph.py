import matplotlib.pyplot as plt
import matplotlib as mlp
import os
import shutil

class Graph:
    __nanumBarunGothic = "NanumBarunGothic.ttf"
    fontRepo = mlp.matplotlib_fname().rstrip("matplotlibrc") + "fonts\\ttf\\" + __nanumBarunGothic

    def __init__(self):
        plt.figure(figsize=(10,10), dpi=150)
        plt.subplots_adjust(top=1.1)
        Graph.__checkFont()

    def __checkFont():
        if(os.path.isfile(Graph.fontRepo) == False):
            Graph.__installFont()

    def __installFont():
        includeFontPath = os.getcwd() + "\\Font\\" + Graph.__nanumBarunGothic
        shutil.copyfile(includeFontPath, Graph.fontRepo)    

    def Draw_separate(self, title, stock, per, pbr):
        plt.subplot(311)
        plt.title(title)
        plt.plot(stock)

        plt.subplot(312)
        plt.title(title + " PER")
        plt.plot(per)

        plt.subplot(313)
        plt.title(title + " PBR")
        plt.plot(pbr)

        plt.show()
    
    # def draw_combine(title, per, pbr):
        
        
        