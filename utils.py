from graph import Graph


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
                        current_graph.add_vertex(*map(int, tokens[1:]))
                    elif tokens[0] == 'e':
                        current_graph.add_edges(*map(int, tokens[1:]))
        return graphs
