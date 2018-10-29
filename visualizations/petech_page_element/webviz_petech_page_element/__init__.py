from os import path
from webviz import JSONPageElement

class PetechPageElement(JSONPageElement):
    """The base class for a webviz petech page element.
    """

    def __init__(self):
        super(PetechPageElement, self).__init__()

        self.add_js_file(path.join(
            path.dirname(__file__),
            'resources',
            'js',
            'webviz_petech.js'))
