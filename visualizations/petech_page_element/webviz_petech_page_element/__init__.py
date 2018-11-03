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

    def get_template(self):
        """
        Overrides :meth:`webviz.PageElement.get_template`.
        """
        pass

    def _repr_html_(self):
        html = ""

        for elem in self.header_elements:
            if not any(key in ["href", "src"] for key, _ in elem.attributes):
                html += str(elem)
                html += "\n"

        return html + self.get_template().render(element=self, root_folder='.')
