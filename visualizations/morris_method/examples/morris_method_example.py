import os
import pandas as pd

from webviz import Webviz
from webviz.page_elements import MorrisMethod

thisdir = os.path.abspath(os.path.dirname(__file__))
df = pd.read_csv(os.path.join(thisdir, './example.csv'), index_col='index')

web = Webviz('MorrisMethod')
web.index.add_content(MorrisMethod(df))

web.write_html("./webviz_example", overwrite=True, display=False)
