import pdb
import os
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'


def load_memory_unit_result(file_path):
    graph_sizes = np.load('output/graph_sizes.npy')
    
    data = np.load(file_path)   # [repeats, graph, queries, memory_type]
    data = data.mean(axis=0)    # [graph, queries, mean_memory_type]
    data /= 1024                # To MB
    data = data.sum(axis=-3)    # [graph, sumed_mean_memory_type_for_queries]
    data = data[:, 1]           # Only mean_peak_memory
  
    return data, graph_sizes


fig = plt.figure(figsize=(10, 4))
plt.xlabel('Graph Size')
plt.ylabel('Peak Memory Usage (MB)')

legends = []

for name in os.listdir('./output'):
    if not name.startswith('memory_unit_test'):
        continue
    file_path = os.path.join('./output', name)
    loc = file_path.rfind('_') + 1
    file_path_code = file_path[loc:-4]
    legends.append(file_path_code)
    mean_time_unit, graph_sizes = load_memory_unit_result(file_path=file_path)
    
    plt.scatter(graph_sizes, mean_time_unit, alpha=0.5)

plt.legend(legends)
plt.tight_layout()
plt.savefig('visualize/memory_unit_analysis.png', dpi=400)

