from ullmann import *
import sys


if __name__ == '__main__':

    graphs = Ullmann.read_file('./graphDB/mygraphdb.data')
    queries = Ullmann.read_file('./graphDB/Q4.my')

    print('Num graphs: ', len(graphs))
    print('Num queries:', len(queries))

    for i in queries:
        for j in graphs:
            solver = Ullmann(i, j)
            solver.search()
        
