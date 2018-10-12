import random
from datetime import datetime
from webviz import Webviz
from webviz.page_elements import DynamicTree


def create_node(depth, child_no):
    is_inactive = random.randint(0, 10)
    return {'name': '{}_{}'.format(depth, child_no),
            'children': [],
            'pressure': random.randint(8, 16) * is_inactive,
            'oilrate': random.randint(1, 200) * is_inactive,
            'waterrate': random.randint(1, 20) * is_inactive,
            'gasrate': random.randint(1, 20) * is_inactive,
            'grupnet': grupnetchars[random.randint(0, len(grupnetchars) - 1)]
                    if is_inactive == 0
                    else random.randint(1, 60) * is_inactive
            }


def grow_tree(root, depth, max_width):
    depth -= 1
    if depth > 0 and random.randint(0, 10) > 1:
        for c in range(0, random.randint(1, max_width)):
            root['children'].append(grow_tree(create_node(depth, c),
                                    depth,
                                    max_width))

    return root


iteration_names = ["Iter_{}".format(i) for i in range(0, 5)]
iteration_names.append('pred')

grupnetchars = ['Z', 'M', 'F']

web = Webviz('Dynamic tree test')

iterations = {n: {datetime(2000 + d, 1, 1): grow_tree(create_node(4, 0), 4, 5)
                  for d in range(0, random.randint(3, 12))}
              for n in iteration_names}

web.index.add_content(DynamicTree(iterations))

web.write_html("./webviz_example", overwrite=True, display=True)
