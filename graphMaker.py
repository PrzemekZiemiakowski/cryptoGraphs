import matplotlib.pyplot as plt

import restApiTalker
import matplotlib
from pywaffle import Waffle
def makeGraph(data):
    #preparing data
    dataPlot={}

    for x in data:
        name=x['slug']
        actPrice = x['quote']['USD']['price']
        dataPlot.update({name: actPrice})
    print(dataPlot)
    fig=plt.Figure(

        FigureClass=Waffle,
        row=5,
        values=dataPlot,
        title={
            'label': 'Example plot',
            'loc': 'left',
            'fontdict': {
                'fontsize': 20
            }
        },
        labels=[f"{k} ({int(v / sum(dataPlot.values()) * 100)}%)" for k, v in dataPlot.items()],
    )