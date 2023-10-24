import time, pdb, random
import numpy as np
from ullmann import Ullmann
from utils import read_file

if __name__ == '__main__':

    test_name = 'Q4'
    graphs = read_file('./graphDB/mygraphdb.data')
    queries = read_file('./graphDB/{}.my'.format(test_name))

    repeat = 5
    num_graphs_used = 300
    num_queries_used = 300
    print('Num graphs: ', num_graphs_used)
    print('Num queries:', num_queries_used)
    print('Num repeats:', repeat)

    time_array = []

    for _ in range(repeat):

        # random.shuffle(graphs)
        # random.shuffle(queries)
        cur_graphs = graphs[:num_graphs_used]
        cur_queries = queries[:num_queries_used]

        start = time.time()
        for q in cur_queries:
            for g in cur_graphs:
                solver = Ullmann(q, g, verbose=False)
                solver.search()
        end = time.time()
        time_spent = float(end - start)
        time_array.append(time_spent)

    print(f'Avg time spent: {np.mean(time_array)}')
        
