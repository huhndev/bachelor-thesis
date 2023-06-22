import json
import matplotlib.pyplot as plt
import os
import glob
import csv

files = glob.glob('*.json')
files.sort()

csv_data = []

for file in files:
    with open('./' + file) as f:
        data = json.load(f)
        sum_sent = data['end']['sum_sent']
        size = sum_sent['bytes']
        duration = sum_sent['seconds']
        avg_speed = sum_sent['bits_per_second']
        row = [size, duration, avg_speed]
        csv_data.append(row)

with open('results.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csv_data)
