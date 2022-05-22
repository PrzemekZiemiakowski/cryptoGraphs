import matplotlib.pyplot as plt
import json
import restApiTalker
import matplotlib
import squarify
from pywaffle import Waffle
def makeGraph(data):
    #preparing data
    dataPlot={}
    sizes=[]
    for x in data:
        name=x['slug']
        volume = x['quote']['USD']['volume_24h']
        sizes.append(volume)
        actPrice = x['quote']['USD']['price']

        print(name," volume: ",volume)
        dataPlot.update({name: volume})
    print(dataPlot)
    labels = [f"{k} ({round(v / sum(dataPlot.values()) * 100, 2)}%)" for k, v in dataPlot.items()]
    plt.figure(figsize=(32, 18), dpi=80)
    squarify.plot(sizes, label=labels,alpha=.8)

    plt.axis('off')
    plt.show()
    fig = plt.figure(
        figsize=(16,9), dpi=80,alpha=.8,
        FigureClass=Waffle,
        rows=10,
        columns=11,
        values=dataPlot,
        rounding_rule='nearest',
        plot_anchor='S',
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
    fig.set_facecolor('#DDDDDD')
    plt.show()