from coinapi_rest_v1.restapi import CoinAPIv1

import graphMaker
import restApiTalker
data=restApiTalker.readData()
graphMaker.makeGraph(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
