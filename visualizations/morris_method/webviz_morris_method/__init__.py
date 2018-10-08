import jinja2
from os import path
from webviz import JSONPageElement
from abc import ABCMeta, abstractmethod


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

    :param output: ``Pandas.DataFrame``. A dataframe with columns for min,
          mean, and max to show in the plot. The index of the column is time.
    :param parameters: List of Dictionaries. Each dictionary has three keys:
          ``name``, ``main`` and ``interaction``. The value for key ``name`` is
          the name of the parameter. ``main`` and ``interaction`` contains a
          list of parameter values, one for each time step.
    """

    def __init__(self, output, parameters, parameter_name=''):
        super(MorrisMethod, self).__init__()

        _output = output.copy()
        _output['time'] = _output.index
        _output['time'] = _output['time'].apply(lambda x: x.isoformat())

        self['output'] = _output.to_dict('records')

        self['parameters'] = parameters
        self['parameter_name'] = parameter_name

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
