import json
import matplotlib.pyplot as plt
import os

# get all filenames from results directory
files = os.listdir('experiments/results/')
files.sort()

table_data = []
src_data = {}

time_zero = 0

for file in files:
    with open('experiments/results/' + file) as f:
        data = json.load(f)
        timestamp = data['start']['timestamp']['timesecs']
        if (time_zero == 0):
            time_zero = timestamp
        src = file.split('-')[1]
        dst = file.split('-')[2].split('.')[0]
        sum_sent = data['end']['sum_sent']
        if (src not in src_data):
            src_data[src] = []
        sum_sent['dst'] = dst
        sum_sent['start_time'] = timestamp - time_zero
        sum_sent['end_time'] = timestamp - time_zero + sum_sent['seconds']
        src_data[src].append(sum_sent)

for src in src_data:
    total_size = 0
    total_duration = 0
    total_avg_speed = 0
    lowest_start_time = -1
    highest_end_time = -1
    for traffic in src_data[src]:
        total_size = total_size + traffic['bytes'] 
        if (lowest_start_time == -1 or traffic['start_time'] < lowest_start_time):
            lowest_start_time = traffic['start_time']
        if (traffic['end_time'] > highest_end_time):
            highest_end_time = traffic['end_time']
    total_size = total_size / (1000*1000)
    total_duration = highest_end_time - lowest_start_time
    total_avg_speed = (total_size / total_duration)*8
    table_data.append([src, str(round(total_size,2))+'MB', str(round(total_duration,1))+'s', str(round(total_avg_speed,2))+'Mbit/s'])


table = plt.table(cellText=table_data, colLabels=['src', 'total size', 'total duration', 'total avg speed'], loc='center')
plt.axis('off')
#plt.show()
plt.savefig('results_table_per_node.png', bbox_inches='tight', dpi=150)
