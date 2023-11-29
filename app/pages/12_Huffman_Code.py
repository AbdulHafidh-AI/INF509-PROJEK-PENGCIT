import streamlit as st
from bisect import insort_left, bisect_left
from graphviz import Digraph

class NodeTree(object):
    def __init__(self, symbol=None, order_val=None, frequency=None, left=None, right=None):
        self.symbol = symbol
        self.order_val = order_val
        self.frequency = frequency
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

def combine_tree(tree1, tree2):
    if tree1.frequency > tree2.frequency:
        return NodeTree(symbol=(tree1.symbol + tree2.symbol), order_val=tree2.order_val, frequency=(tree1.frequency + tree2.frequency), left=tree2, right=tree1)
    else:
        return NodeTree(symbol=(tree1.symbol + tree2.symbol), order_val=tree1.order_val, frequency=(tree1.frequency + tree2.frequency), left=tree1, right=tree2)
    
def initial_tree(string):
    freq = {}
    unique_letters = []

    for c in string:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
            unique_letters.append(c)

    freq = sorted(freq.items(), key=lambda x: (x[1], ord(x[0])), reverse=False)

    trees = [NodeTree(symbol=item[0], order_val=ord(item[0]), frequency=item[1]) for item in freq]

    return trees, unique_letters

def remove_tree(trees, tree_symbol):
    # Find the index of the tree with the specified symbol
    index_to_remove = next((index for index, tree in enumerate(trees) if tree.symbol == tree_symbol), None)

    # Remove the tree if found
    if index_to_remove is not None:
        del trees[index_to_remove]

def huffman_coding(trees):
    while len(trees) > 1:
        trees = sorted(trees, key=lambda x: (x.frequency, x.order_val))
        tree12 = combine_tree(trees[0], trees[1])
        del trees[0]
        del trees[0]

        trees.insert(bisect_left([node.frequency for node in trees], tree12.frequency), tree12)

    return trees


def print_huffman_codes_table(node, code='', huffman_table=None):
    if huffman_table is None:
        huffman_table = []

    if node is not None:
        if node.left is None and node.right is None:
            huffman_table.append({"Symbol": node.symbol, "Huffman Code": code})

        print_huffman_codes_table(node.left, code + '0', huffman_table)
        print_huffman_codes_table(node.right, code + '1', huffman_table)

    return huffman_table
    


def print_huffman_tree(node, code='', dot=None):
    if dot is None:
        dot = Digraph(comment='Huffman Tree')

    if node is not None:
        label = f"{node.symbol} ({node.frequency})"
        dot.node(node.symbol, label=label)
        if node.left is not None:
            dot.edge(node.symbol, node.left.symbol, label='0')
            print_huffman_tree(node.left, code + '0', dot)
        if node.right is not None:
            dot.edge(node.symbol, node.right.symbol, label='1')
            print_huffman_tree(node.right, code + '1', dot)

    return dot

# Streamlit App
st.title("Huffman Coding with Streamlit")

# Input
string = st.text_input("Enter a string:", "LOSSLESS-COMPRESSION")

# Generate Huffman Codes
trees, unique_letters = initial_tree(string)
trees2 = huffman_coding(trees)

# Print Huffman codes for each symbol and display the Huffman tree diagram
st.subheader("Huffman Codes:")

# Print Huffman codes as a table without index
huffman_table = print_huffman_codes_table(trees2[0])
# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)
st.table(huffman_table)

st.subheader("Huffman Tree:")

dot = Digraph(comment='Huffman Tree')
for tree in trees2:
    dot = print_huffman_tree(tree, dot=dot)

st.graphviz_chart(dot.source)
