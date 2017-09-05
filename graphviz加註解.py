#  encoding=utf-8
import graphviz as gv
import functools

graph = functools.partial(gv.Graph, format='svg')
digraph = functools.partial(gv.Digraph, format='svg')

g3 = graph(); g4 = digraph()


def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n[0])
        return graph
def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph

list1 = list("ABCDE")
list2 = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('B', 'E')]
add_edges(add_nodes(g3, list1), list2).render('image/g3')
add_edges(add_nodes(g4, list1), list2).render('image/g4')
g5 = graph()
list3 = [('A', {'label':'Apple'}), ('B', {'label':'Banana'}),
         ('C', {'label':'Citron'}), ('D', {})]

list4 = [(('A', 'B'), {'label':'Summer fruit'}),
         (('A', 'C'), {'label': 'Sour flaver'}),
         (('B', 'C'), {'label': 'Yellow like'}),
         (('B', 'D'), {})]

add_edges(add_nodes(g5, list3), list4).render('image/g5')

styles = {
    'graph':{
        'label':u'我的圖形',
        'fontsize':'24',
        'fontcolor':'#442200',
        'bgcolor':'#FFAAFF',
        'rankdir':'TB',
        'fillcolor':'#AA66AA'
    },
    'nodes':{
        'fontname': 'Consolas',
        'shape': 'box',
        'fontcolor':'#00FF00',
        'color':'white',
        'style':'filled',
        'fillcolor':'#66AAAA'
    },
    'edges':{
        'style':'dotted',
        'color':'#004488',
        'arrowhead':'open',
        'fontname':'Courier',
        'fontsize':'16',
        'fontcolor':'#440088'
    }
}

def apply_style(graph, styles):
    graph.graph_attr.update(('graph' in styles and styles['graph']) or {})
    graph.node_attr.update(('nodes' in styles and styles['nodes']) or {})
    graph.edge_attr.update(('edges' in styles and styles['edges']) or {})
    return graph
g5 = apply_style(g5, styles)
g5.render('image/g5p')