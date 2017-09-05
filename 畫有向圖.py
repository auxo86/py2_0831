#  encoding=utf-8
import graphviz as gv
import itertools

g2 = gv.Digraph(format='svg')
list1 = list('ABCD')
for node in list1:
    g2.node(node)

#list2 = itertools.combinations(list1, 2)
list2 = itertools.permutations(list1, 2)
# print [item1 + str(',') + str(item2) for item1, item2 in list2]
for item1, item2 in list2:
    g2.edge(item1, item2)
g2.render('image/g2pic')