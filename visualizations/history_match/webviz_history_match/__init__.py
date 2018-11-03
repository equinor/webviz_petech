import jinja2
from os import path
from webviz.page_elements import PetechPageElement
import numpy as np
from scipy.stats import chi2


env = jinja2.Environment(
    loader=jinja2.PackageLoader('webviz_history_match', 'templates'),
    trim_blocks=True,
    lstrip_blocks=True,
    undefined=jinja2.StrictUndefined
)


def _get_unsorted_edges():
    """P10 - P90 unsorted edge coordinates"""

    retval = {
        'low': chi2.ppf(0.1, 1),
        'high': chi2.ppf(0.9, 1)
    }

    return retval


def _get_sorted_edges(number_observation_groups):
    """P10 - P90 sorted edge coordinates"""

    monte_carlo_iterations = 100000

    sorted_values = np.empty((number_observation_groups,
                              monte_carlo_iterations))

    for i in range(monte_carlo_iterations):
        sorted_values[:, i] = np.sort(np.random.chisquare(
                                      df=1,
                                      size=number_observation_groups))

    sorted_values = np.flip(sorted_values, 0)

    P10 = np.percentile(sorted_values, 90, axis=1)
    P90 = np.percentile(sorted_values, 10, axis=1)

    # Dictionary with two arrays (P10, P90). Each array of length equal
    # to number of observation groups i.e. number of items along y axis.
    # These values are to be used for drawing the stair stepped
    # sorted P10-P90 area:

    coordinates = {'low': list(P10), 'high': list(P90)}

    return coordinates


class HistoryMatch(PetechPageElement):
    def __init__(self, data):
        super(HistoryMatch, self).__init__()

        self['data'] = self._prepareData(data)

    def _prepareData(self, data):
        data = data.copy().reset_index()

        ensemble_labels = data.ensemble_name.unique().tolist()
        num_obs_groups = len(data.obs_group_name.unique())

        data['avg_pos'] = data['total_pos'] / data['number_data_points']
        data['avg_neg'] = data['total_neg'] / data['number_data_points']

        iterations = []
        for ensemble in ensemble_labels:
            df = data[data.ensemble_name == ensemble]
            iterations.append(df.groupby('obs_group_name').mean())

        sorted_iterations = self._sortIterations(iterations)

        iterations_dict = self._iterations_to_dict(sorted_iterations,
                                                   ensemble_labels)

        confidence_sorted = _get_sorted_edges(num_obs_groups)
        confidence_unsorted = _get_unsorted_edges()

        data = {}
        data['iterations'] = iterations_dict
        data['confidence_interval_sorted'] = confidence_sorted
        data['confidence_interval_unsorted'] = confidence_unsorted

        return data

    def _sortIterations(self, iterations):
        sorted_data = []

        for df in iterations:
            sorted_df = df.copy()

            sorted_data.append(
                sorted_df.assign(f=sorted_df['avg_pos'] + sorted_df['avg_neg'])
                         .sort_values('f', ascending=False)
                         .drop('f', axis=1)
            )

        return sorted_data

    def _iterations_to_dict(self, iterations, labels):
        retval = []

        for iteration, label in zip(iterations, labels):
            retval.append({
                'name': label,
                'positive': iteration['avg_pos'].tolist(),
                'negative': iteration['avg_neg'].tolist(),
                'labels': iteration.index.tolist()
            })

        return retval

    def get_template(self):
        """
        Overrides :meth:`webviz.PageElement.get_template`.
        """
        return env.get_template('history_match.html')
