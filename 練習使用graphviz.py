#  encoding=utf-8
import graphviz as gv

g1 = gv.Graph(format='svg')
g1.node('A')
g1.node('B')
g1.node('C')
g1.node('D')
g1.node('E')


g1.edge('A', 'B')
g1.edge('A', 'C')
g1.edge('B', 'D')
g1.edge('C', 'D')
g1.edge('C', 'E')

print g1.source
g1.render()

listnode = ['A','B','C','D','E']

for i in range(0, len(listnode)):
    for j in range(0,len(listnode)):
        g1.edge(listnode[i], listnode[j])

print g1.source
g1.render()

