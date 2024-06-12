import uuid
import networkx as nx
import matplotlib.pyplot as plt
import colorsys

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 7))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def array_to_heap(array):
    if not array:
        return None

    nodes = [Node(val) for val in array]
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]

    return nodes[0]

def get_color(value, max_value):
    hue = value / max_value
    lightness = (1 - hue) / 2 + 0.5
    return '#' + ''.join(f'{int(c * 255):02X}' for c in colorsys.hls_to_rgb(hue, lightness, 1))

def dfs_visualize(root):
    stack = [root]
    visited = set()
    order = 1
    while stack:
        node = stack.pop()
        if node and node not in visited:
            visited.add(node)
            node.color = get_color(order, 100)
            draw_tree(root)
            order += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

def bfs_visualize(root):
    from collections import deque
    queue = deque([root])
    visited = set()
    order = 1
    while queue:
        node = queue.popleft()
        if node and node not in visited:
            visited.add(node)
            node.color = get_color(order, 100)
            draw_tree(root)
            order += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

def visualize_heap(array, method='dfs'):
    root = array_to_heap(array)
    if method == 'dfs':
        dfs_visualize(root)
    elif method == 'bfs':
        bfs_visualize(root)
    else:
        print(f"Unknown method: {method}")

# Приклад використання:
heap_array = [4, 5, 10, 1, 3]
visualize_heap(heap_array, 'dfs')
visualize_heap(heap_array, 'bfs')
