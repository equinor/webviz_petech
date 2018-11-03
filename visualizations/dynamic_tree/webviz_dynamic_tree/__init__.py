import jinja2
from six import iteritems
from os import path
from webviz.page_elements import PetechPageElement

env = jinja2.Environment(
    loader=jinja2.PackageLoader('webviz_dynamic_tree', 'templates'),
    trim_blocks=True,
    lstrip_blocks=True,
    undefined=jinja2.StrictUndefined
)


class DynamicTree(PetechPageElement):
    """
    Creates a group tree visualization

    :param iterations: group tree datastructure as a json-dictionary.
        The layout of the data is as follows:

        ::

            { iteration_name : { date: tree } }

        where the date is a datetime.datetime object,
        and tree is a dictionary with the following keys:

        ::

            {
                name,
                children: [tree],
                pressure,
                oilrate,
                waterrate,
                gasrate,
                grupnet
            }

    :param iteration_order: `Optional argument.` An optional order of
        the iterations given as list of iteration names.
    """

    def __init__(self, iterations, iteration_order=None):
        super(DynamicTree, self).__init__()

        self['iterations'] = (
            {name: {
                'timesteps': [
                    date.isoformat() for date in iteration.keys()
                    ],
                'trees': {
                    date.isoformat(): tree
                    for date, tree in iteritems(iteration)
                    }
                }
             for name, iteration in iteritems(iterations)
             }
        )
        if iteration_order is None:
            self['iteration_names'] = list(iterations.keys())
        else:
            self['iteration_names'] = iteration_order

    def get_template(self):
        """
        Overrides :meth:`webviz.PageElement.get_template`.
        """
        return env.get_template('dynamic_tree.html')
