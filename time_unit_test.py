import time, pdb, random, os
import numpy as np
from ullmann import Ullmann
from utils import read_file
import argparse


if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--name', type=str, default='Q4')
    arg_parser.add_argument('--repeat', type=int, default=5)
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

    time_arrays_repeat = []
    graphs_sizes = []

    for i in range(repeat):
        time_arrays = []
        if args.shuffle:
            random.seed(42 + i * 100)
            random.shuffle(graphs)
            random.shuffle(queries)
        cur_graphs = graphs[:num_graphs_used]
        cur_queries = queries[:num_queries_used]

        if i == 0:
            for g in cur_graphs:
                graphs_sizes.append(len(g.vertices))

        for g in cur_graphs:
            time_array = []
            for q in cur_queries:
                start = time.time()
                solver = Ullmann(q, g, verbose=False)
                solver.search()
                end = time.time()
                time_spent = float(end - start)
                time_array.append(time_spent)
            time_arrays.append(time_array)
        time_arrays_repeat.append(time_arrays)
    # pdb.set_trace()
    graphs_sizes = np.array(graphs_sizes)
    time_arrays_repeat = np.array(time_arrays_repeat)
    if not os.path.exists('./output'):
        os.makedirs('./output')

    np.save('output/time_unit_test_{}'.format(test_name), time_arrays_repeat)
    np.save('output/graph_sizes', graphs_sizes)

