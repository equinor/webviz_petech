import pandas as pd
import numpy as np

from webviz import Webviz
from webviz.page_elements import HistoryMatch


def generate_iterations(num_groups, num_iter):
    obs_group_names = ['Obs. group ' + str(i) for i in range(num_groups)]

    data = []
    for i in range(num_iter):
        # Random test data following
        # chisquared distribution (i.e. normal distribution squared):

        misfits = np.random.chisquare(df=1, size=(num_groups, 1))
        split = np.random.rand(num_groups, 1)

        pos = misfits*split
        neg = misfits*(1-split)

        df = pd.DataFrame(np.hstack((pos, neg)),
                          columns=['pos', 'neg'],
                          index=obs_group_names)

        data.append(df)

    return data


def generate_labels(num_iter):
    obs_group_names = ['Iteration ' + str(i) for i in range(num_iter)]

    return obs_group_names


iterations = generate_iterations(100, 4)
iterations_labels = generate_labels(4)

web = Webviz('History matching', theme='equinor')

web.index.add_content(HistoryMatch(iterations=iterations,
                                   iterations_labels=iterations_labels))

web.write_html("./webviz_example", overwrite=True, display=True)
