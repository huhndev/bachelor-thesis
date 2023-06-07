import json
import matplotlib.pyplot as plt
import os
import glob

# get all filenames from results directory
files = glob.glob('*.json')
files.sort()

table_data = []
time_stamp_exists = False
time_zero = 0

for file in files:
    with open('./' + file) as f:
        data = json.load(f)
        if ('start' in data):
            time_stamp_exists = True
            timestamp = data['start']['timestamp']['timesecs']
            if (time_zero == 0):
                time_zero = timestamp
            start_time = str(round(timestamp - time_zero, 1))+'s'
        src = file.split('-')[1]
        dst = file.split('-')[2].split('.')[0]
        sum_sent = data['end']['sum_sent']
        size = str(round(sum_sent['bytes']/(1000*1000),2))+'MB'
        duration = str(round(sum_sent['seconds'],1))+'s'
        avg_speed = str(round(sum_sent['bits_per_second']/(1000*1000),2))+'Mbit/s'
        row = [src, dst, size, duration, avg_speed]
        if (time_stamp_exists):
            row = [src, dst, size, start_time, duration, avg_speed]
        table_data.append(row)

#table = plt.table(cellText=table_data, colLabels=['src', 'dst', 'size', 'duration', 'avg speed'], loc='center')
if (time_stamp_exists):
    table = plt.table(cellText=table_data, colLabels=['src', 'dst', 'size', 'start time', 'duration', 'avg speed'], loc='center')
plt.axis('off')
#plt.show()
plt.savefig('results_table.png', bbox_inches='tight', dpi=150)
