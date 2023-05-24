import json
import matplotlib.pyplot as plt
import os

# get all filenames from results directory
files = os.listdir('experiments/results/')
files.sort()

table_data = []

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
        size = str(round(sum_sent['bytes']/(1000*1000),2))+'MB'
        start_time = str(round(timestamp - time_zero, 1))+'s'
        duration = str(round(sum_sent['seconds'],1))+'s'
        avg_speed = str(round(sum_sent['bits_per_second']/(1000*1000),2))+'Mbit/s'
        row = [src, dst, size, start_time, duration, avg_speed]
        table_data.append(row)

table = plt.table(cellText=table_data, colLabels=['src', 'dst', 'size', 'start time', 'duration', 'avg speed'], loc='center')
plt.axis('off')
#plt.show()
plt.savefig('results_table.png', bbox_inches='tight', dpi=150)
