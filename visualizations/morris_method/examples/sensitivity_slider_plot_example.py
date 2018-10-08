import json
import pandas as pd
from datetime import datetime

from webviz import Webviz
from webviz.page_elements import MorrisMethod


data = json.load(open('./example_data.json'))
config = data['FOPT']

output = pd.DataFrame(
        config['output'],
        map(lambda x: datetime.strptime(x, '%d.%m.%Y'),
            config['output']['time']))

parameters = config['parameters']

web = Webviz('MorrisMethod', theme='equinor')

web.index.add_content(MorrisMethod(output,
                                   parameters,
                                   'Parameter name'))

web.write_html("./webviz_example", overwrite=True, display=True)
