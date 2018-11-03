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
        html = """<style>.slider,
.slider-inset,
.slider-overlay {
    stroke-linecap: round;
}

.slider {
    stroke-width: 8px;
}

.slider-inset {
    stroke: #b20276;
    stroke-width: 8px;
}

.slider-overlay {
    pointer-events: stroke;
    cursor: pointer;
}

.handle {
    fill: #fff;
    stroke: #b20276;
    stroke-opacity: 0.5;
    stroke-width: 1.25px;
}</style>
"""

        return html + self.get_template().render(element=self, root_folder='.')
