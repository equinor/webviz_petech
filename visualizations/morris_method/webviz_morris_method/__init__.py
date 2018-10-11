import jinja2
from os import path
from webviz import JSONPageElement
from abc import ABCMeta, abstractmethod
from datetime import datetime
from collections import defaultdict

env = jinja2.Environment(
    loader=jinja2.PackageLoader('webviz_morris_method', 'templates'),
    trim_blocks=True,
    lstrip_blocks=True,
    undefined=jinja2.StrictUndefined
)


class MorrisMethod(JSONPageElement):
    """
    An interactive display of main and interaction effects on sets of
    parameters when scanning through the span of a plot. The plot contains a
    line for min, mean, and max on the y-axis, and timestep on the x-axis. For
    each timestep on the x-axis there is a different value for each parameter.

    :param data: ``Pandas.DataFrame``. A dataframe with columns for `min`,
          `mean`, and `max` to show in the plot. The index of the column is
          time. For each parameter there should be two columns with the names
          `main PARAMETERNAME` and `interactions PARAMETERNAME`, listing the
          main an interactions effect respectively for parameter
          `PARAMETERNAME`. There is also a column `name` which is the name
          of the response vector studied.
    """

    def __init__(self, data):
        super(MorrisMethod, self).__init__()

        self.data = data.copy()

        self.data['time'] = self.data.index.values
        self.data['time'] = self.data['time'] \
            .apply(lambda x: datetime.strptime(x, '%Y-%m-%d')
                   .isoformat())

        self['output'] = self.data[['time', 'min', 'max', 'mean']]\
                             .to_dict('records')

        param_dict = defaultdict(dict)
        for column in self.data.columns:
            if 'main ' in column or 'interactions ' in column:
                param_name = " ".join(column.split(" ")[1:])
                estimator = column.split()[0]  # main or interactions

                param_dict[param_name]['name'] = param_name
                param_dict[param_name][estimator] = self.data[column].tolist()

        self['parameters'] = list(param_dict.values())

        if len(self.data['name'].unique()) > 1:
            raise NotImplemented("Not yet support for multiple "
                                 "response vectors")
        self['response_name'] = self.data['name'].unique()[0]

        self.add_js_file(path.join(
            path.dirname(__file__),
            'resources',
            'js',
            'morris_method.js'))

        self.add_css_file(path.join(
            path.dirname(__file__),
            'resources',
            'css',
            'morris_method.css'))

    def get_template(self):
        """
        Overrides :meth:`webviz.PageElement.get_template`.
        """
        return env.get_template('morris_method.html')
