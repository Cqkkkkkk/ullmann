from ullmann import Ullmann
from utils import read_file


if __name__ == '__main__':

    graphs = read_file('./graphDB/mygraphdb.data')
    queries = read_file('./graphDB/Q4.my')

    print('Num graphs: ', len(graphs))
    print('Num queries:', len(queries))


    for q in queries:
        for g in graphs:
            solver = Ullmann(q, g)
            solver.search()
        
        