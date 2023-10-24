import time, pdb, random, os
import numpy as np
from ullmann import Ullmann
from utils import read_file
import tracemalloc
import argparse

if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--name', type=str)
    arg_parser.add_argument('--repeat', type=int, default=1)
    arg_parser.add_argument('--shuffle', action='store_true')
    args = arg_parser.parse_args()

    test_name = args.name
    repeat = args.repeat

    graphs = read_file('./graphDB/mygraphdb.data')
    queries = read_file('./graphDB/{}.my'.format(test_name))


    num_graphs_used = 100
    num_queries_used = 100

    print('Test on query set: ', test_name)
    print('Num graphs: ', num_graphs_used)
    print('Num queries:', num_queries_used)
    print('Num repeats:', repeat)
    print('Shuffle:', args.shuffle)

    memory_monitors = []

    for i in range(repeat):
        memory_monitor = []
        tracemalloc.start()

        if args.shuffle:
            random.seed(42 + i * 100)
            random.shuffle(graphs)
            random.shuffle(cur_queries)

        cur_graphs = graphs[:num_graphs_used]
        cur_queries = queries[:num_queries_used]

        for q in cur_queries:
            for g in cur_graphs:
                solver = Ullmann(q, g, verbose=False)
                solver.search()
                memory_monitor.append(tracemalloc.get_traced_memory())
        tracemalloc.stop()
        memory_monitors.append(memory_monitor)

    memory_monitors = np.array(memory_monitors)

    if not os.path.exists('./output'):
        os.makedirs('./output')

    np.save('output/memory_test_{}'.format(test_name), memory_monitors)

        
