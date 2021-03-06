import functools
import graphviz as gv

graph = functools.partial(gv.Graph, format='svg')
digraph = functools.partial(gv.Digraph, format='svg')
g3 = graph();
g4 = digraph()


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
list3 = [('A', {'label': 'Apple'}), ('B', {'label': 'Banana'}),
         ('C', {'label': 'Citron'}), ('D', {})]
list4 = [(('A', 'B'), {'label': 'Summer fruit'}),
         (('A', 'C'), {'label': 'Sour flavor'}),
         (('B', 'C'), {'label': 'Yellow like'}),
         (('B', 'D'), {})]
add_edges(add_nodes(g5, list3), list4).render('image/g5')
