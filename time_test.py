import time, pdb, random
import numpy as np
from ullmann import Ullmann
from utils import read_file
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
    
    num_graphs_used = 300
    num_queries_used = 300
    print('Test on query set: ', test_name)
    print('Num graphs: ', num_graphs_used)
    print('Num queries:', num_queries_used)
    print('Num repeats:', repeat)
    print('Shuffle:', args.shuffle)

    time_array = []

    for i in range(repeat):
        if args.shuffle:
            random.seed(42 + i * 100)
            random.shuffle(graphs)
            random.shuffle(queries)
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
        
