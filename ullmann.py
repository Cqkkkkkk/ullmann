import pdb
import numpy as np
from graph import Graph


class Ullmann:
    def __init__(self, graph1, graph2):
        self.graph1 = graph1
        self.graph2 = graph2

    @staticmethod
    def check_mat(graph1, graph2, mat):
        matrix1 = graph1.adjacency_matrix()
        matrix2 = graph2.adjacency_matrix()
        intermediate_matrix = mat.dot(mat.dot(matrix2).T)

        for i, j in np.ndindex(matrix1.shape):
            if matrix1[i, j] and not intermediate_matrix[i, j]:
                return False
        return True

    @staticmethod
    def refinement(graph1, graph2, mat):
        matrix1 = graph1.adjacency_matrix()
        matrix2 = graph2.adjacency_matrix()

        for i, j in np.ndindex(mat.shape):
            if mat[i, j]:
                for x in range(matrix1.shape[0]):
                    if matrix1[i][x]:
                        if not any(mat[x][y] * matrix2[y][j] for y in range(matrix2.shape[0])):
                            mat[i][j] = 0
                if not mat[i][j]:
                    break
        return mat

    @staticmethod
    def matrix_failed(mat):
        return any(sum(row) == 0 for row in mat)

    @staticmethod
    def get_transformation_matrix(graph1, graph2):

        trans_matrix = np.zeros((len(graph1.vertices), len(graph2.vertices)))
        for vertex1 in graph1.vertices:
            for vertex2 in graph2.vertices:
                if vertex1.label == vertex2.label and len(vertex1.neighbors) <= len(vertex2.neighbors):
                    trans_matrix[vertex1.vid][vertex2.vid] = 1
        return trans_matrix


    @staticmethod
    def read_file(path):
        graphs = []

        with open(path) as file:
            current_graph = Graph()
            for line in file:
                tokens = line.strip().split()
                if len(tokens) > 0: 
                    if tokens[0] == 't':
                        if current_graph.vertices:
                            graphs.append(current_graph)
                            current_graph = Graph()
                    elif tokens[0] == 'v':
                        current_graph.add_vertex(*tokens[1:])
                    elif tokens[0] == 'e':
                        current_graph.add_edges(*tokens[1:])
        return graphs

    def search(self):
        num_vertices1 = len(self.graph1.vertices)
        num_vertices2 = len(self.graph2.vertices)

        trans_matrix = self.get_transformation_matrix(self.graph1, self.graph2)
        trans_matrix = self.refinement(self.graph1, self.graph2, trans_matrix)

        if self.matrix_failed(trans_matrix):
            return

        depth_matrices = [trans_matrix.copy() for _ in range(num_vertices1)]
        columns_used = [0 for _ in range(num_vertices2 + 1)]
        depth = 0
        column_id = 0
        depth_markers = [-1 for _ in range(num_vertices1 + 1)]

        column_id = depth_markers[0] if depth == 0 else -1
        matches_count = 0

        while depth >= 0:
            can_move_deeper = False

            for j in range(column_id + 1, num_vertices2):
                if trans_matrix[depth][j] and not columns_used[j]:
                    can_move_deeper = True
                    columns_used[j] = 1
                    depth_markers[depth] = j

                    for col in range(num_vertices2):
                        if col != j:
                            trans_matrix[depth][col] = 0

                    refined_matrix = self.refinement(self.graph1, self.graph2, trans_matrix.copy())
                    if self.matrix_failed(refined_matrix):
                        can_move_deeper = False
                        trans_matrix = depth_matrices[depth]
                        continue
                    break

            if can_move_deeper:
                depth += 1
                if depth == num_vertices1:
                    if self.check_mat(self.graph1, self.graph2, trans_matrix.copy()):
                        matches_count += 1
                        print(trans_matrix)
                    can_move_deeper = False
                else:
                    depth_matrices[depth] = trans_matrix.copy()
                    column_id = depth_markers[depth]

            if not can_move_deeper:
                if depth == 0:
                    print(f'total: {matches_count}')
                    return

                depth_markers[depth] = -1
                depth -= 1
                trans_matrix = depth_matrices[depth].copy()
                column_id = depth_markers[depth]
                columns_used[depth_markers[depth]] = 0
