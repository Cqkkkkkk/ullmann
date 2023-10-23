import numpy as np


class Vertex:
    def __init__(self, vid, label):
        self.vid = vid
        self.label = label
        self.neighbors = []

    def add_neighbor(self, vertex):
        if vertex not in self.neighbors:
            self.neighbors.append(vertex)

    def __repr__(self):
        return f"Vertex(vid={self.vid}, label={self.label})"
    


class Edge:
    def __init__(self, start_vertex, end_vertex, label):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex

    def __repr__(self):
        return f"Edge(start={self.start_vertex.vid}, end={self.end_vertex.vid}, label={self.label})"





class Graph(object):

    def __init__(self):
        self.vertices = []
        self.edges = []
        self._adjacency_matrix = None
        self._adjacency_matrix = None

    # def add_vertex(self, vid, label):
    #     self.vertices.append(Vertex(int(vid), label))
    def add_vertex(self, vid, label):
        vertex = Vertex(int(vid), label)
        self.vertices.append(vertex)
        return vertex

    # def add_edges(self, start, end, label):
    #     start = int(start)
    #     end = int(end)
    #     self.edges.append(Edge(start, end, label))
    #     self.vertices[start].add_neighbor(self.vertices[end])
    #     self.edges.append(Edge(end, start, label))
    #     self.vertices[end].add_neighbor(self.vertices[start])
    def add_edges(self, start_vid, end_vid, label):
        start_vertex = self.vertices[int(start_vid)]
        end_vertex = self.vertices[int(end_vid)]
        
        edge = Edge(start_vertex, end_vertex, label)
        self.edges.append(edge)
        
        start_vertex.add_neighbor(end_vertex)
        end_vertex.add_neighbor(start_vertex)
    
    def adjacency_matrix(self):
        if self._adjacency_matrix is not None:
            return self._adjacency_matrix
        else:
            size_t = len(self.vertices)
            self._adjacency_matrix = np.zeros((size_t, size_t))
            for v_from in self.vertices:
                for v_to in v_from.neighbors:
                    self._adjacency_matrix[v_from.vid][v_to.vid] = 1
            return self._adjacency_matrix

    def show(self):
        for i in self.vertices:
            print(i.vid, i.label,)
            for j in i.neighbors:
                print((j.vid, j.label), )
        print((self.adjacency_matrix()))
