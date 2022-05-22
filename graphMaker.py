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
        dataPlot.update({name: int(volume)})
    print(dataPlot)
    fig = plt.figure(
        FigureClass=Waffle,
        rows=5,
        columns=10,
        values=dataPlot,
        title={
            'label': 'Example plot',
            'loc': 'left',
            'fontdict': {
                'fontsize': 20
            }
        },
        labels=[f"{k} ({int(v / sum(dataPlot.values()) * 100)}%)" for k, v in dataPlot.items()],
        legend={
            # 'labels': [f"{k} ({v}%)" for k, v in data.items()],  # lebels could also be under legend instead
            'loc': 'lower left',
            'bbox_to_anchor': (0, -0.4),
            'ncol': len(data),
            'framealpha': 0,
            'fontsize': 12
        }
    )
    plt.show()