import matplotlib.pyplot as plt
import matplotlib as mlp
import os
import shutil

class Graph:
    __nanumBarunGothic = "NanumBarunGothic.ttf"
    fontRepo = mlp.matplotlib_fname().rstrip("matplotlibrc") + "fonts\\ttf\\" + __nanumBarunGothic

    def __init__(self):
        Graph.__checkFont()
        Graph.__SetFont()

    def __checkFont():
        if(os.path.isfile(Graph.fontRepo) == False):
            Graph.__installFont()

    def __installFont():
        fontInstallPath = os.getcwd() + "\\Font\\" + Graph.__nanumBarunGothic
        shutil.copyfile(fontInstallPath, Graph.fontRepo)    

    def __SetFont():
        plt.rcParams["font.family"] = "nanumBarunGothic"

    # standard 값에 맞추어 value 평균의 비율을 구한 뒤에 data 를 보정합니다.
    def __correctStock(avg_standard, avg_value, data):
        coefficient = avg_standard / avg_value
        avg_value *= coefficient
        data *= coefficient

    def draw_separate(self, title, stock, per, pbr):
        plt.figure(figsize=(10,10), dpi=150)
        plt.subplots_adjust(top=1.1)

        plt.subplot(3,1,1)
        plt.title(title + " STOCK")
        plt.plot(stock)

        plt.subplot(3,1,2)
        plt.title(title + " PER")
        plt.plot(per)

        plt.subplot(3,1,3)
        plt.title(title + " PBR")
        plt.plot(pbr)

        plt.show()
    
    def draw_combine(self, title, stock, per, pbr):
        Graph.__correctStock(stock.mean(), per.mean(), per);
        Graph.__correctStock(stock.mean(), pbr.mean(), pbr);

        plt.title(title + " STOCK & FINANCE")
        plt.plot(stock, label = "STOCK")
        plt.plot(per, label = "PER")
        plt.plot(pbr, label = "PBR")       
        plt.legend() 
        
        