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
        checked = {} 
        
        def clone(n):
            # print("Cloning node ", n.val)
            # print("Current checked: ", checked.keys())
            if n in checked:
                # print("Already exists, out")
                return checked[n]
            else:
                
                result = Node(n.val)
                checked[n] = result
                
                for neighbor in n.neighbors:
                    result.neighbors.append(clone(neighbor))
                    
            return result 
        
        return clone(node)
    
def print_graph(n):
    checked = []
    
    def recursive(n):
        if n not in checked:
            print(n.val, end='| neighbors: ')
            for node in n.neighbors:
                print(node.val, end=';  ')
            print('')
                
            checked.append(n)
        else:
            return
        for node in n.neighbors:
            recursive(node)
    
    recursive(n)

# Input graph and create neighbors lists
input = [Node(1), Node(2), Node(3), Node(4)]
input[0].neighbors = [ input[1] , input[3] ]
input[1].neighbors = [ input[0] , input[2] ]
input[2].neighbors = [ input[1] , input[3] ]
input[3].neighbors = [ input[0] , input[2] ]

sol = Solution()
output = sol.cloneGraph(input[0])
# print(sol.cloneGraph(input[0]))

print_graph(input[0])

print("RESULT:\n")
print_graph(output)
