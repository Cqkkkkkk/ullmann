import pdb, os
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'



def load_time_unit_result(file_path):
    data = np.load(file_path)   # [repeat, num_graphs, unit_time_cost]
    data = data.mean(axis=0)    # [num_graphs, mean_unit_time_cost]
    data = data.sum(axis=-1)
    graph_sizes = np.load('output/graph_sizes.npy')

    return data, graph_sizes


fig = plt.figure(figsize=(10, 4))
plt.xlabel('Graph Size')
plt.ylabel('Time Cost (Second)')

legends = []

for name in os.listdir('./output'):
    if not name.startswith('time_unit_test'):
        continue
    file_path = os.path.join('./output', name)
    loc = file_path.rfind('_') + 1
    file_path_code = file_path[loc:-4]
    legends.append(file_path_code)
    mean_time_unit, graph_sizes = load_time_unit_result(file_path=file_path)
    
    plt.scatter(graph_sizes, mean_time_unit, alpha=0.5)

plt.legend(legends)
plt.tight_layout()
plt.savefig('visualize/time_unit_analysis.png', dpi=400)

