"""       
# Constraints 
- The number of nodes in the graph is in the range [0, 100].
- 1 <= Node.val <= 100
- Node.val is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The Graph is connected and all nodes can be visited starting from the given node.

# Task
Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

"""

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

def log_nodes(n, node_list):
    # print("checking node " , n.val)
    if n not in node_list:
        node_list.append(n) 
        # print('current nodelist: ', node_list)
    else:
        return node_list
    
    for node in n.neighbors:
        # print("throw into recursion node ", node.val)
        log_nodes(node, node_list)
        
def clone_nodes(n, node_list, r):
    print("Im here")
    print("Checking ", n.val)
    if n not in node_list:
        node_list.append(n) 
        r = n
        
        print("Neighbors: ")
        print(n.neighbors)
        print(r.neighbors)
        # for node in n.neighbors:
            
        #     r.neighbors.append(node)
    else:
        return node_list
    
    for node in n.neighbors:
        # print("throw into recursion node ", node.val)
        clone_nodes(node, node_list, r)
         

# Input graph
input = []

# Write input graph
length = 4
for i in range(1, length + 1):
    n = Node(i)
    input.append(n)
    if i >= length + 1:
        break

# Create neighbors lists
input[0].neighbors = [ input[1] , input[3] ]
input[1].neighbors = [ input[0] , input[2] ]
input[2].neighbors = [ input[1] , input[3] ]
input[3].neighbors = [ input[0] , input[2] ]
    
# Display input graph
for node in input:
    print(node.val, ' | neighbors: ', node.neighbors[0].val, node.neighbors[1].val)       
    
print("[LOG] Log nodes: \n")

nodes = []


log_nodes(input[0], nodes)

print(nodes)

for node in nodes:
    print(node.val, ' | neighbors: ', node.neighbors[0].val, node.neighbors[1].val)   
    
    
result = Node()

nodes = []

clone_nodes(input[0], nodes, result)

print(nodes)
print(result)
print(result.neighbors)

log_nodes(result, nodes)

# print("Show results: ")

# print(nodes)

# for node in nodes:
#     print(node, node.neighbors)
    # print(node.val, ' | neighbors: ', node.neighbors[0].val, node.neighbors[1].val)   
    