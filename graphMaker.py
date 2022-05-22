import matplotlib.pyplot as plt
import json
import restApiTalker
import matplotlib
from pywaffle import Waffle
def makeGraph(data):
    #preparing data
    dataPlot={}
    for x in data:
        name=x['slug']
        volume = x['quote']['USD']['volume_24h']
        actPrice = x['quote']['USD']['price']
        print(name," volume: ",volume)
        dataPlot.update({name: volume})
    print(dataPlot)
    fig = plt.figure(
        FigureClass=Waffle,
        rows=15,
        columns=27,
        values=dataPlot,
        rounding_rule='nearest',
        title={
            'label': 'Udział kryptowalut na rynku po 24h obrotu',
            'loc': 'left',
            'fontdict': {
                'fontsize': 20
            }
        },
        labels=[f"{k} ({round(v / sum(dataPlot.values()) * 100,2)}%)" for k, v in dataPlot.items()],
        legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1)}
    )
    plt.show()