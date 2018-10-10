import os
import json
import pandas as pd
from datetime import datetime

from webviz import Webviz
from webviz.page_elements import MorrisMethod

thisdir = os.path.abspath(os.path.dirname(__file__))

data = json.load(open(os.path.join(thisdir, './example_data.json')))
config = data['FOPT']

output = pd.DataFrame(
        config['output'],
        map(lambda x: datetime.strptime(x, '%d.%m.%Y'),
            config['output']['time']))

parameters = config['parameters']

web = Webviz('MorrisMethod')

web.index.add_content(MorrisMethod(output,
                                   parameters,
                                   'Parameter name'))

web.write_html("./webviz_example", overwrite=True, display=False)
