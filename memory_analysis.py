import pdb, os
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'



def load_memory_result(file_path):
    data = np.load(file_path)   # [repeats, trials(graphsxquerys), memory_type]
    data = data.mean(axis=0)    # [trials, mean_memory_type]
    data /= 1024                # To MB
    mean_cur_memory = data[:, 0]
    mean_peak_memory = data[:, 1]

    return mean_cur_memory, mean_peak_memory


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
# fig.suptitle('Title')
ax1.set_title('Instant Memory Usage (MB)')
ax1.set_xlabel('Trials')
ax1.set_ylabel('Memory Usage (MB)')
ax2.set_title('Peak Memory Usage (MB)')
ax2.set_xlabel('Trials')
ax2.set_ylabel('Memory Usage (MB)')

legends = []

for name in os.listdir('./output'):
    if not name.startswith('memory_test'):
        continue
    file_path = os.path.join('./output', name)
    loc = file_path.rfind('_') + 1
    file_path_code = file_path[loc:-4]
    legends.append(file_path_code)
    mean_cur_memory, mean_peak_memory = load_memory_result(file_path=file_path)

    ax1.plot(mean_cur_memory)
    ax2.plot(mean_peak_memory)

ax1.legend(legends)
ax2.legend(legends)

plt.tight_layout()
plt.savefig('visualize/memory_analysis.png', dpi=400)

