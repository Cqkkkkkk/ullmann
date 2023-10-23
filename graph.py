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
        return f"Edge(start={self.start_vertex.vid}, end={self.end_vertex.vid})"



class Graph(object):

    def __init__(self):
        self.vertices = []
        self.edges = []
        self._adjacency_matrix = None
        self._adjacency_matrix = None

    def add_vertex(self, vid, label):
        vertex = Vertex(vid, label)
        self.vertices.append(vertex)
        return vertex

    def add_edges(self, start_vid, end_vid, label):
        start_vertex = self.vertices[start_vid]
        end_vertex = self.vertices[end_vid]
        
        edge = Edge(start_vertex, end_vertex, label)
        self.edges.append(edge)
        
        start_vertex.add_neighbor(end_vertex)
        end_vertex.add_neighbor(start_vertex)
    
    def adjacency_matrix(self):
        if self._adjacency_matrix is None:
            size_t = len(self.vertices)
            self._adjacency_matrix = np.zeros((size_t, size_t))
            for edge in self.edges:
                self._adjacency_matrix[edge.start_vertex.vid][edge.end_vertex.vid] = 1
                self._adjacency_matrix[edge.end_vertex.vid][edge.start_vertex.vid] = 1            
        return self._adjacency_matrix

    def show(self):
        for i in self.vertices:
            print(i.vid, i.label,)
            for j in i.neighbors:
                print((j.vid, j.label), )
        print((self.adjacency_matrix()))
