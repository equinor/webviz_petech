from collections import OrderedDict
import pandas as pd
import numpy as np

from webviz import Webviz
from webviz.page_elements import HistoryMatch


def generate_synthetic_data(num_groups, num_iter, num_realizations):
    """Create synthetic test data. In reality, this data will
    come from  an assisted history matching run.
    """

    obs_group_names = ['Obs. group ' + str(i) for i in range(num_groups)]
    number_dp = np.random.randint(low=10, high=100, size=num_groups)

    df = pd.DataFrame()

    for i in range(num_iter):
        ensemble_name = 'Iteration ' + str(i)

        # Random test data following
        # chisquared distribution (i.e. normal distribution squared):
        misfits = np.random.chisquare(df=1, size=num_groups)
        misfits *= number_dp

        split = np.random.rand(num_groups)

        pos = misfits * split
        neg = misfits * (1 - split)

        for j in range(num_realizations):
            realization_name = 'Realization ' + str(j)

            scale = 1.0 + np.random.rand() * 0.4
            realization_pos = scale * pos
            realization_neg = scale * neg

            df = df.append(pd.DataFrame(
                OrderedDict([
                    ('obs_group_name', obs_group_names),
                    ('ensemble_name', ensemble_name),
                    ('realization', realization_name),
                    ('total_pos', realization_pos),
                    ('total_neg', realization_neg),
                    ('number_data_points', number_dp)
                ])))

    return df.set_index(['obs_group_name', 'ensemble_name', 'realization'])


data = generate_synthetic_data(num_groups=50,
                               num_iter=4,
                               num_realizations=100)

web = Webviz('History matching', theme='equinor')

web.index.add_content(HistoryMatch(data))

web.write_html("./webviz_example", overwrite=True, display=False)
