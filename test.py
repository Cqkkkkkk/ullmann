from ullmann import Ullmann
import numpy as np

class Vertex:
    def __init__(self, vid, label):
        self.vid = vid      # Vertex ID
        self.label = label      # Vertex label
        self.neighbors = []

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, vid, label):
        vertex = Vertex(vid, label)
        self.vertices.append(vertex)
        return vertex

    def add_edges(self, v1, v2):
        self.vertices[v1].neighbors.append(self.vertices[v2])
        self.vertices[v2].neighbors.append(self.vertices[v1])
        self.edges.append((v1, v2))

    def get_matrix(self):
        size = len(self.vertices)
        matrix = [[0 for _ in range(size)] for _ in range(size)]
        for edge in self.edges:
            matrix[edge[0]][edge[1]] = 1
            matrix[edge[1]][edge[0]] = 1
        return np.array(matrix)

# 例子1
G1 = Graph()
G1.add_vertex(0, 'a')
G1.add_vertex(1, 'b')
G1.add_vertex(2, 'a')
G1.add_edges(0, 1)
G1.add_edges(1, 2)

H1 = Graph()
H1.add_vertex(0, 'a')
H1.add_vertex(1, 'b')
H1.add_edges(0, 1)

# 例子2
G2 = Graph()
G2.add_vertex(0, 'x')
G2.add_vertex(1, 'y')
G2.add_vertex(2, 'z')
G2.add_vertex(3, 'x')
G2.add_edges(0, 1)
G2.add_edges(1, 2)
G2.add_edges(2, 3)

H2 = Graph()
H2.add_vertex(0, 'x')
H2.add_vertex(1, 'y')
H2.add_edges(0, 1)

# 使用Ullmann算法进行测试
ullmann1 = Ullmann(H1, G1)
ullmann1.search()

ullmann2 = Ullmann(H2, G2)
ullmann2.search()
