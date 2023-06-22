import json
import matplotlib.pyplot as plt
import os
import glob
import csv

files = glob.glob('*.json')
files.sort()

csv_data = []
sum_size = 0
sum_duration = 0
avg_speed = 0

for file in files:
    with open('./' + file) as f:
        data = json.load(f)
        sum_sent = data['end']['sum_sent']
        sum_size += sum_sent['bytes']
        sum_duration += sum_sent['seconds']

avg_speed = (sum_size*8)/sum_duration
row = [sum_size, sum_duration, avg_speed]
csv_data.append(row)

with open('results_sum.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csv_data)
