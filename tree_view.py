import pydot

menu = {'dinner':
            {'chicken':'good',
             'beef':'average',
             'vegetarian':{
                   'tofu':'good',
                   'salad':{
                            'caeser':'bad',
                            'italian':'average'}
                   },
             'pork':'bad'}
        }

def draw(parent_name, child_name, graph):
    edge = pydot.Edge(parent_name, child_name)
    graph.add_edge(edge)

def visit(graph, node, parent=None):
    for k,v in node.items():
        if isinstance(v, dict):
            # We start with the root node whose parent is None
            # we don't want to graph the None node
            if parent:
                draw(parent, k, graph)
            visit(graph,v, k)
        elif isinstance(v, list):
            if parent:
                draw(parent, k, graph)
            for i in v:
                draw(k,i, graph)
        else:
            draw(parent, k, graph)
            # drawing the label using a distinct name
            draw(k, k+'_'+v, graph)
            
def save_file(graph, file_path):
    graph.write_png(file_path)

# creating tree for above dict
graph = pydot.Dot(graph_type='graph')
visit(graph, menu)
save_file(graph, 'vowel_tree.png')

# creating square noded tree
graph = pydot.Dot()
graph.set_node_defaults(color='lightgray', style='filled', shape='box',
                            fontname='Courier', fontsize='10')
visit(graph, menu)
save_file(graph, 'square_tree.png')
