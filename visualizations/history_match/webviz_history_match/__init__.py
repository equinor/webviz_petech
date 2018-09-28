import jinja2
from os import path
from webviz import JSONPageElement
from abc import ABCMeta, abstractmethod
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

    sorted_values = np.empty((number_observation_groups, monte_carlo_iterations))

    for i in range(monte_carlo_iterations):
        sorted_values[:, i] = np.sort(np.random.chisquare(df=1, size=number_observation_groups))

    sorted_values = np.flip(sorted_values, 0)

    P10 = np.percentile(sorted_values, 90, axis=1)
    P90 = np.percentile(sorted_values, 10, axis=1)

    # Dictionary with two arrays (P10, P90). Each array of length equal to number of observation groups
    # i.e. number of items along Y axis. These values are to be used for drawing the stair stepped
    # sorted P10-P90 area:

    coordinates = {'low': list(P10), 'high': list(P90)}

    return coordinates

class HistoryMatch(JSONPageElement):
    def __init__(self, iterations, iterations_labels):
        super(HistoryMatch, self).__init__()

        self['data'] = self._prepareData(iterations, iterations_labels)

    def _prepareData(self, iterations, labels):
        data = {}

        sorted_iterations = self._sortIterations(iterations)

        iterations_dict = self._iterations_to_dict(sorted_iterations, labels)

        confidence_sorted = _get_sorted_edges(len(iterations_dict[0]['positive']))
        confidence_unsorted = _get_unsorted_edges()

        data['iterations'] = iterations_dict
        data['confidence_interval_sorted'] = confidence_sorted
        data['confidence_interval_unsorted'] = confidence_unsorted

        return data

    def _sortIterations(self, iterations):
        sorted_data = []

        for df in iterations:
            sorted_df = df.copy()
            sorted_df = sorted_df.assign(f=sorted_df['pos'] + sorted_df['neg']).sort_values('f', ascending=False).drop('f', axis=1)
            sorted_data.append(sorted_df)

        return sorted_data

    def _iterations_to_dict(self, iterations, labels):
        retval = []

        for iteration, label in zip(iterations, labels):
            retval.append({
                'name': label,
                'positive': iteration['pos'].tolist(),
                'negative': iteration['neg'].tolist(),
                'labels': iteration.index.tolist()
            })

        return retval

    def get_template(self):
        """
        Overrides :meth:`webviz.PageElement.get_template`.
        """
        return env.get_template('history_match.html')

    def get_css_dep(self):
        """Extends :meth:`webviz.PageElement.get_css_dep`."""
        deps = super(HistoryMatch, self).get_css_dep()
        history_match_css = path.join(
            path.dirname(__file__),
            'resources',
            'css',
            'slider.css')
        deps.append(history_match_css)
        return deps

    def get_js_dep(self):
        """Extends :meth:`webviz.PageElement.get_js_dep`."""
        deps = super(HistoryMatch, self).get_js_dep()
        history_match_js = path.join(
            path.dirname(__file__),
            'resources',
            'js',
            'history_match.js')
        deps.append(history_match_js)
        return deps
