import json
import os
import glob
import csv

csv_data = []

runs = os.listdir('.')
runs.sort()

for run in runs:
    sum_size = 0
    sum_duration = 0
    files = glob.glob('./' + run + '/*.json')
    files.sort()
    for file in files:
        with open('./' + file) as f:
            data = json.load(f)
            sum_sent = data['end']['sum_sent']
            sum_size += sum_sent['bytes']
            sum_duration += sum_sent['seconds']
    avg_speed = (sum_size*8)/sum_duration
    row = [sum_size, sum_duration, avg_speed]
    csv_data.append(row)

avg_size = sum([x[0] for x in csv_data]) / len(csv_data)
avg_duration = sum([x[1] for x in csv_data]) / len(csv_data)
avg_speed = (avg_size*8)/avg_duration
row = [avg_size, avg_duration, avg_speed]
csv_data.append(row)

with open('results_avg.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csv_data)
