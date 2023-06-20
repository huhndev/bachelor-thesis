import json
import os
import glob
import csv

csv_data = []

runs = glob.glob('run*')
runs.sort()

for run in runs:
    files = glob.glob('./' + run + '/*.json')
    files.sort()
    time_zero = 9999999999
    longest_completion_time = 0

    for file in files:
        with open('./' + file) as f:
            data = json.load(f)
            timestamp = data['start']['timestamp']['timesecs']
            if (timestamp < time_zero):
                time_zero = timestamp

    for file in files:
        with open('./' + file) as f:
            data = json.load(f)
            timestamp = data['start']['timestamp']['timesecs']
            start_time = timestamp - time_zero
            sum_sent = data['end']['sum_sent']
            duration = sum_sent['seconds']
            completion_time = start_time + duration 
            if (completion_time > longest_completion_time):
                longest_completion_time = completion_time

    row = [longest_completion_time]
    csv_data.append(row)

avg_longest_completion_time = sum([x[0] for x in csv_data]) / len(csv_data)
row = [avg_longest_completion_time]
csv_data.append(row)

with open('results_average_longest_completion_time.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csv_data)
